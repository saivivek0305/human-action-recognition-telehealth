# Action Video Dataset (Included)

This folder contains a small demo dataset of 15 videos for quick testing and development.

Structure:
- synthetic/               : 5 synthetic motion videos (shapes)
- stick_walk/              : 5 stick-figure walking videos
- silhouette_exercise/     : 5 silhouette exercise videos

Usage:
- Preprocess with: `python src/preprocess.py --input examples/videos/<folder>/<video>.mp4 --out data/frames/<folder>`
- Train/infer scripts in `src/` expect small sample data for demos.

Notes:
- These videos are synthetic and intended only for prototyping.
- For production training, replace with larger, real-world datasets and provide proper annotations.
