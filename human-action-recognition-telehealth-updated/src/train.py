import argparse
import torch
from torch import nn, optim
from torch.utils.data import DataLoader, TensorDataset
from models.simple_cnn_lstm import CNNLSTM

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--epochs", type=int, default=5)
    p.add_argument("--batch", type=int, default=2)
    p.add_argument("--debug", action="store_true")
    return p.parse_args()

def main():
    args = parse_args()

    # Dummy dataset for quick test runs
    x = torch.randn(8, 10, 3, 224, 224)
    y = torch.randint(0, 5, (8,))

    dataset = TensorDataset(x, y)
    loader = DataLoader(dataset, batch_size=args.batch, shuffle=True)

    model = CNNLSTM()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=5e-4)

    for epoch in range(args.epochs):
        for data, target in loader:
            optimizer.zero_grad()
            out = model(data)
            loss = criterion(out, target)
            loss.backward()
            optimizer.step()
        if args.debug:
            print(f"Epoch {epoch+1} Loss {loss.item():.4f}")

    torch.save(model.state_dict(), "model.pth")
    print('Saved model.pth')

if __name__ == "__main__":
    main()
