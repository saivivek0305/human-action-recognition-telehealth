# Human Action Recognition in Telehealth Systems

**Author:** Rapolu Sai Vivek  
**Contact:** +91 72070 82048 | cbitrapolu2003@gmail.com

## Project summary
Deep learning system to recognize patient actions in telehealth settings using a lightweight CNN+LSTM architecture.
Target: 90% accuracy on target dataset (research / demo).

## Repo contents
- `src/` — preprocessing, model, training, inference
- `models/` — model definitions
- `notebooks/` — experiments and EDA
- `examples/` — sample video and demo scripts
- `data/` — small sample data and instructions for downloading full datasets

## Quick start
1. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Run preprocessing on sample video:
   ```bash
   python src/preprocess.py --input examples/sample_video.mp4 --out data/frames --skip 5
   ```
3. Train quick demo (CPU):
   ```bash
   python src/train.py --epochs 2 --debug
   ```
4. Run inference:
   ```bash
   python src/infer.py --model model.pth --video examples/sample_video.mp4
   ```

## Data
- Do not include large datasets in the repo.
- Add download instructions to `data/README.md`.

## Model checkpoints
- Host large checkpoints externally (Google Drive / S3) and place links in `docs/CHECKPOINTS.md`.

## License
MIT © Rapolu Sai Vivek
