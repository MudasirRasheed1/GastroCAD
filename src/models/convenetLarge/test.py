import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from models.convenetLarge.model import ConvenetLarge
from models.convenetLarge import config

def test():
    transform = transforms.Compose([
        transforms.Resize((config.image_size, config.image_size)),
        transforms.ToTensor()
    ])

    test_dataset = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
    test_loader = DataLoader(test_dataset, batch_size=config.batch_size, shuffle=False)

    model = ConvenetLarge(num_classes=config.num_classes)
    model.load_state_dict(torch.load("models/convenetLarge/convenet_large.pth"))
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()

    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)

    print(f"Accuracy: {100 * correct / total:.2f}%")

if __name__ == "__main__":
    test()
