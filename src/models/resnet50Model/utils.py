import matplotlib.pyplot as plt
from sklearn.metrics import classification_report

def plot_loss_curve(train_losses, val_losses):
    plt.plot(range(1, len(train_losses)+1), train_losses, label='Train Loss')
    plt.plot(range(1, len(val_losses)+1), val_losses, label='Val Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig('loss_curve.png')
    plt.show()

def print_classification_report(y_true, y_pred, target_names):
    print(classification_report(y_true, y_pred, target_names=target_names, digits=4))
