\# TrueVision AI



A multimodal deepfake detection system analyzing image, video, and audio 

together to produce an authenticity score with explainable results.



\## Status

Phase 0 complete — environment set up, FFmpeg verified, GPU (Colab) verified,

sample dataset (DFDC train\_sample\_videos) downloaded locally.



\## Setup

1\. `python -m venv venv`

2\. `venv\\Scripts\\activate`

3\. `pip install -r requirements.txt`



\## Project Structure

\- `data/` — datasets (not tracked in Git, too large)

\- `models/` — trained model files per module (visual, facial, audio, lipsync)

\- `fusion/` — score fusion logic

\- `backend/` — FastAPI service + async workers

\- `frontend/` — web dashboard

\- `scripts/` — preprocessing utilities

\- `notebooks/` — experiments

