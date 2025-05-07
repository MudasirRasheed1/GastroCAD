import os
import pandas as pd
from PIL import Image
from torch.utils.data import Dataset
from sklearn.preprocessing import LabelEncoder
from collections import Counter

class GastroDataset(Dataset):
    def __init__(self, dataframe, img_root, transform=None):
        self.df = dataframe
        self.img_root = os.path.normpath(img_root)
        self.transform = transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        img_path = os.path.normpath(os.path.join(self.img_root, str(row['num patient']), row['filename']))
        try:
            image = Image.open(img_path).convert("RGB")
        except FileNotFoundError:
            print(f"Warning: Image not found at {img_path}. Skipping.")
            return torch.zeros(3, 224, 224), row['label_enc']
        except Exception as e:
            print(f"Error loading image {img_path}: {e}. Skipping.")
            return torch.zeros(3, 224, 224), row['label_enc']

        if self.transform:
            image = self.transform(image)
        return image, row['label_enc']

def load_data(csv_dir, img_root):
    # Load data
    df = pd.read_csv(os.path.join(csv_dir, "image_classification.csv"))

    # Encode labels from the `FG1 (Team A)` column
    le = LabelEncoder()
    df['label_enc'] = le.fit_transform(df['FG1 (Team A)'])
    
    return df, le
