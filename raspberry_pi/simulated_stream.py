"""Synthetic 12-lead stream for testing the Wi-Fi viewer only.

This generates artificial waveforms. It is NOT real ECG and must never be
used for diagnosis, clinical evaluation, or hardware validation.
Run on the Raspberry Pi or laptop:
    python raspberry_pi/simulated_stream.py
"""
import asyncio
import json
import math
import time

import websockets

HOST = "0.0.0.0"
PORT = 8765
FS = 250
FRAME_SAMPLES = 25
LEADS = ["I", "II", "III", "aVR", "aVL", "aVF",
         "V1", "V2", "V3", "V4", "V5", "V6"]


def synthetic_sample(t, lead_index):
    """Produce a visibly ECG-like artificial waveform."""
    phase = (t * 1.2) % 1.0
    # Small P wave, sharp QRS-like complex, and broader T wave.
    p = 0.10 * math.exp(-((phase - 0.18) / 0.035) ** 2)
    q = -0.12 * math.exp(-((phase - 0.385) / 0.012) ** 2)
    r = (0.9 - 0.035 * lead_index) * math.exp(
        -((phase - 0.405) / 0.010) ** 2
    )
    s = -0.22 * math.exp(-((phase - 0.43) / 0.016) ** 2)
    tw = 0.25 * math.exp(-((phase - 0.68) / 0.09) ** 2)
    return p + q + r + s + tw


async def handler(websocket):
    await websocket.send(json.dumps({
        "type": "metadata", "device": "CardioAI-SYNTHETIC",
        "sampling_rate": FS, "leads": LEADS, "units": "arbitrary",
        "synthetic": True
    }))
    sample_index = 0
    while True:
        start = time.monotonic()
        frame = [[] for _ in LEADS]
        for _ in range(FRAME_SAMPLES):
            t = sample_index / FS
            for lead_index in range(len(LEADS)):
                frame[lead_index].append(synthetic_sample(t, lead_index))
            sample_index += 1
        await websocket.send(json.dumps({
            "type": "ecg_frame", "timestamp": time.time(),
            "sampling_rate": FS, "leads": LEADS,
            "samples": frame, "synthetic": True
        }))
        elapsed = time.monotonic() - start
        await asyncio.sleep(max(0, FRAME_SAMPLES / FS - elapsed))


async def main():
    print(f"SYNTHETIC TEST STREAM on ws://{HOST}:{PORT} — NOT REAL ECG")
    async with websockets.serve(handler, HOST, PORT, max_size=2**20):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
