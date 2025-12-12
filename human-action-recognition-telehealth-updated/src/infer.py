import argparse
import torch
from models.simple_cnn_lstm import CNNLSTM

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", default="model.pth")
    args = p.parse_args()

    model = CNNLSTM()
    try:
        model.load_state_dict(torch.load(args.model, map_location="cpu"))
    except Exception as e:
        print("Could not load model:", e)
    model.eval()
    x = torch.randn(1, 10, 3, 224, 224)
    out = model(x)
    print("Logits:", out.detach().numpy())

if __name__ == "__main__":
    main()
