# CardioAI

A research and educational platform for multilead ECG acquisition, visualization, signal processing, and arrhythmia-analysis experiments.

## Architecture

- **ECG front end:** isolated multichannel ECG acquisition hardware.
- **Raspberry Pi:** acquires synchronized ECG samples and streams them over local Wi-Fi.
- **Laptop:** runs the CardioAI interface, displays live ECG traces, stores recordings, and runs analysis.
- **Transport:** WebSocket over a trusted local network.

## Current milestone: Wi-Fi live-view foundation

- `raspberry_pi/stream_server.py` — real-hardware server scaffold; acquisition adapter remains to be implemented for the selected ECG front end.
- `raspberry_pi/simulated_stream.py` — artificial 12-channel test stream for checking the laptop viewer and Wi-Fi connection. It is not physiological data.
- `laptop/live_viewer.py` — laptop-side 12-trace live plotting client.
- `src/cardioai/` — reusable signal-processing modules (under development).
- `tests/` — automated tests (under development).

## Run a software-only connection test

Install dependencies on both devices:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Raspberry Pi / Linux / macOS:
source .venv/bin/activate
pip install -r requirements.txt
```

On the Raspberry Pi, start the artificial stream:

```bash
python raspberry_pi/simulated_stream.py
```

Find the Pi's Wi-Fi IP address with:

```bash
hostname -I
```

On the laptop, connected to the same Wi-Fi network, run:

```bash
python laptop/live_viewer.py --host RASPBERRY_PI_IP
```

Replace `RASPBERRY_PI_IP` with the actual address, for example `192.168.1.50`. Allow TCP port 8765 through the Pi firewall if required.

## ECG lead and hardware design notes

A standard 12-lead ECG uses 10 electrodes. The limb and chest electrode potentials are used to derive the 12 displayed leads. The acquisition channel count and lead derivation must match the selected ECG analog front end; do not assume 12 independent ADC channels are required.

Do not connect electrodes or patient leads directly to Raspberry Pi GPIO. Use an ECG analog front end designed for biopotential acquisition, appropriate input protection, isolation, and a reviewed patient-safety design. This project is for research and education and is not a clinically validated diagnostic device.

Synthetic waveforms are only for software testing. They are not real ECG data and must not be used to validate a classifier or make medical decisions.
