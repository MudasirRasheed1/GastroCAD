import os
import cv2
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models, transforms
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import LabelEncoder
from PIL import Image

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

# Constants
VIDEO_DIR = "../../data/gastroHUN/videoSequences"
IMG_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 10

# Read CSVs
df_train = pd.read_csv("processed_splits_csvs/train.csv")
df_val = pd.read_csv("processed_splits_csvs/val.csv")
df_test = pd.read_csv("processed_splits_csvs/test.csv")

# Encode labels
label_encoder = LabelEncoder()
label_encoder.fit(pd.concat([df_train["label"], df_val["label"], df_test["label"]]))
df_train["label_enc"] = label_encoder.transform(df_train["label"])
df_val["label_enc"] = label_encoder.transform(df_val["label"])
df_test["label_enc"] = label_encoder.transform(df_test["label"])

# Image transformations
transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

# Dataset class
class VideoDataset(Dataset):
    def __init__(self, dataframe, transform=None):
        self.data = dataframe.reset_index(drop=True)
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        video_name = self.data.loc[idx, "video_name"]
        label = self.data.loc[idx, "label_enc"]
        video_path = os.path.join(VIDEO_DIR, video_name)

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise IOError(f"Cannot open video: {video_path}")

        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        center_frame = frame_count // 2
        cap.set(cv2.CAP_PROP_POS_FRAMES, center_frame)
        success, frame = cap.read()
        cap.release()

        if not success:
            raise RuntimeError(f"Failed to read frame {center_frame} from {video_name}")

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame_rgb)

        if self.transform:
            image = self.transform(image)

        return image, label

# Data loaders
train_loader = DataLoader(VideoDataset(df_train, transform), batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(VideoDataset(df_val, transform), batch_size=BATCH_SIZE)
test_loader = DataLoader(VideoDataset(df_test, transform), batch_size=BATCH_SIZE)

# Model
model = models.resnet18(pretrained=True)
model.fc = nn.Linear(model.fc.in_features, len(label_encoder.classes_))
model.to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train function
def train(model, loader):
    model.train()
    running_loss = 0.0
    correct, total = 0, 0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
        correct += (outputs.argmax(1) == labels).sum().item()
        total += labels.size(0)
    print(f"Train Loss: {running_loss:.4f}, Accuracy: {100*correct/total:.2f}%")

# Eval function
def evaluate(model, loader, mode="Validation"):
    model.eval()
    loss_total, correct, total = 0.0, 0, 0
    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss_total += loss.item()
            correct += (outputs.argmax(1) == labels).sum().item()
            total += labels.size(0)
    print(f"{mode} Loss: {loss_total:.4f}, Accuracy: {100*correct/total:.2f}%")

# Training loop
for epoch in range(EPOCHS):
    print(f"Epoch {epoch+1}/{EPOCHS}")
    train(model, train_loader)
    evaluate(model, val_loader)

# Final test
evaluate(model, test_loader, mode="Test")
