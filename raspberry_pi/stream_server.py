"""WebSocket server that streams ECG frames from an acquisition adapter.

Run on the Raspberry Pi:
    python stream_server.py

The acquisition adapter is intentionally a placeholder until the ECG AFE
and its safe, isolated interface have been selected and tested.
"""

import asyncio
import json
import os
import time
from typing import AsyncIterator

import websockets

HOST = "0.0.0.0"
PORT = int(os.getenv("CARDIOAI_PORT", "8765"))
SAMPLE_RATE = int(os.getenv("CARDIOAI_SAMPLE_RATE", "250"))
LEADS = [
    "I", "II", "III", "aVR", "aVL", "aVF",
    "V1", "V2", "V3", "V4", "V5", "V6",
]


async def acquire_frames() -> AsyncIterator[dict]:
    """Yield frames from the ECG acquisition hardware.

    Replace this placeholder with the selected AFE driver. Each frame should
    contain a synchronized list of samples for each lead. Do not connect
    electrodes directly to Raspberry Pi GPIO.
    """
    raise NotImplementedError(
        "ECG acquisition is not configured. Implement this adapter after "
        "selecting and validating the multichannel ECG front end."
    )
    yield  # Makes this function an async generator.


async def handler(websocket):
    """Send ECG frames to each connected laptop client."""
    await websocket.send(json.dumps({
        "type": "metadata",
        "device": "CardioAI-RaspberryPi",
        "sampling_rate": SAMPLE_RATE,
        "leads": LEADS,
        "units": "mV",
    }))

    async for frame in acquire_frames():
        payload = {
            "type": "ecg_frame",
            "timestamp": time.time(),
            "sampling_rate": SAMPLE_RATE,
            "leads": LEADS,
            "samples": frame,
        }
        await websocket.send(json.dumps(payload))


async def main():
    print(f"CardioAI ECG stream server listening on ws://{HOST}:{PORT}")
    async with websockets.serve(handler, HOST, PORT, max_size=2**20):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
