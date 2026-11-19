"""Laptop-side CardioAI 12-lead live ECG viewer.

Connects to the Raspberry Pi WebSocket server and plots incoming samples.
Run:
    python live_viewer.py --host 192.168.1.50
"""

import argparse
import asyncio
import json
import threading
from collections import deque
from queue import Queue, Empty

import matplotlib.pyplot as plt
import numpy as np
import websockets

LEAD_NAMES = [
    "I", "II", "III", "aVR", "aVL", "aVF",
    "V1", "V2", "V3", "V4", "V5", "V6",
]
WINDOW_SECONDS = 8


def network_worker(uri: str, frames: Queue, stop: threading.Event):
    async def receive():
        async with websockets.connect(uri, max_size=2**20) as ws:
            print(f"Connected to {uri}")
            async for message in ws:
                if stop.is_set():
                    break
                packet = json.loads(message)
                if packet.get("type") == "metadata":
                    print("Stream metadata:", packet)
                elif packet.get("type") == "ecg_frame":
                    frames.put(packet)

    asyncio.run(receive())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True, help="Raspberry Pi Wi-Fi IP")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()

    frames = Queue(maxsize=100)
    stop = threading.Event()
    uri = f"ws://{args.host}:{args.port}"
    thread = threading.Thread(
        target=network_worker, args=(uri, frames, stop), daemon=True
    )
    thread.start()

    sample_rate = 250
    window_size = sample_rate * WINDOW_SECONDS
    buffers = [deque([0.0] * window_size, maxlen=window_size)
               for _ in LEAD_NAMES]

    fig, axes = plt.subplots(6, 2, figsize=(15, 10), sharex=True)
    fig.suptitle("CardioAI — Live 12-Lead ECG (research prototype)")
    lines = []
    x = np.arange(window_size) / sample_rate
    for ax, name, buffer in zip(axes.flat, LEAD_NAMES, buffers):
        line, = ax.plot(x, list(buffer), linewidth=0.8)
        ax.set_title(name)
        ax.set_ylabel("mV")
        ax.grid(True, alpha=0.3)
        lines.append(line)
    axes[-1, 0].set_xlabel("Time (s)")
    axes[-1, 1].set_xlabel("Time (s)")
    status = fig.text(0.01, 0.01, "Waiting for ECG stream…")

    def update(_):
        nonlocal sample_rate, window_size, x, buffers
        received = 0
        while received < 20:
            try:
                packet = frames.get_nowait()
            except Empty:
                break
            sample_rate = int(packet.get("sampling_rate", sample_rate))
            samples = packet.get("samples", [])
            names = packet.get("leads", LEAD_NAMES)
            if len(samples) != len(names):
                status.set_text("Invalid frame: lead count does not match samples")
                continue
            if len(buffers[0]) != sample_rate * WINDOW_SECONDS:
                window_size = sample_rate * WINDOW_SECONDS
                buffers = [deque([0.0] * window_size, maxlen=window_size)
                           for _ in LEAD_NAMES]
                x = np.arange(window_size) / sample_rate
            for name, values in zip(names, samples):
                if name in LEAD_NAMES:
                    idx = LEAD_NAMES.index(name)
                    buffers[idx].extend(np.asarray(values, dtype=float).tolist())
            received += 1
            status.set_text(f"Receiving stream • {sample_rate} samples/s")

        for line, buffer in zip(lines, buffers):
            line.set_ydata(list(buffer))
        return lines + [status]

    timer = fig.canvas.new_timer(interval=100)
    timer.add_callback(update, None)
    timer.start()

    try:
        plt.show()
    finally:
        stop.set()


if __name__ == "__main__":
    main()
