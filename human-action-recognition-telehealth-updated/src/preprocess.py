import cv2
import os
import argparse

def extract_frames(video_path, out_dir, skip=5):
    os.makedirs(out_dir, exist_ok=True)
    vid = cv2.VideoCapture(video_path)
    count = 0
    saved = 0

    while True:
        ret, frame = vid.read()
        if not ret:
            break

        if count % skip == 0:
            cv2.imwrite(os.path.join(out_dir, f"frame_{saved:06d}.jpg"), frame)
            saved += 1

        count += 1

    print("Frames extracted:", saved)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="examples/sample_video.mp4")
    parser.add_argument("--out", default="data/frames")
    parser.add_argument("--skip", type=int, default=5)
    args = parser.parse_args()
    extract_frames(args.input, args.out, args.skip)
