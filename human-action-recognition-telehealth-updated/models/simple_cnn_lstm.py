import torch
import torch.nn as nn

class CNNLSTM(nn.Module):
    def __init__(self, num_classes=5):
        super().__init__()

        self.cnn = nn.Sequential(
            nn.Conv2d(3, 16, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.lstm = nn.LSTM(32 * 56 * 56, 128, batch_first=True)
        self.fc = nn.Linear(128, num_classes)

    def forward(self, x):
        b, t, c, h, w = x.size()
        x = x.view(b * t, c, h, w)
        cnn_out = self.cnn(x)
        cnn_out = cnn_out.view(b, t, -1)
        lstm_out, _ = self.lstm(cnn_out)
        out = self.fc(lstm_out[:, -1, :])
        return out
