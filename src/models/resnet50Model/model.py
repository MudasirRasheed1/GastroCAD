import torch
import torch.nn as nn
from torchvision import models

class PretrainedResNet50(nn.Module):
    def __init__(self, num_classes, weights_path):
        super(PretrainedResNet50, self).__init__()
        # Load ResNet-50 model
        self.model = models.resnet50(pretrained=False)
        # Load pretrained weights from the uploaded file
        self.model.load_state_dict(torch.load(weights_path))
        # Replace the final fully connected layer
        self.model.fc = nn.Linear(self.model.fc.in_features, num_classes)

    def forward(self, x):
        return self.model(x)
