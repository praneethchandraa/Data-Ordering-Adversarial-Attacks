import torch
import torchvision
import torchvision.transforms as transforms
import random
import torchvision.transforms.functional as TF


import pytorch_lightning as pl
import torchvision
import torch.nn as nn
import torch.nn.functional as F

from torchmetrics.functional import accuracy
from torch.optim import Adam
import numpy as np
from sklearn.metrics import classification_report



test_transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

train_transform = transforms.Compose(
    [
     torchvision.transforms.RandomCrop(32, padding=4),
#      torchvision.transforms.Resize(),
     torchvision.transforms.RandomHorizontalFlip(),
     transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])


batch_size = 64

trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=train_transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
                                          shuffle=True, num_workers=16)#, collate_fn=randomSizeCollate)

testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                       download=True, transform=test_transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
                                         shuffle=False, num_workers=16)

classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')


def resnet18CIFAR10():
    model = torchvision.models.resnet18(pretrained=False, num_classes=10)
    model.conv1 = nn.Conv2d(3, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
    model.maxpool = nn.Identity()
    
    return model

class BoilerPlate(pl.LightningModule):
    def __init__(self, train_l, val_l) -> None:
        super(BoilerPlate, self).__init__()

        self.train_l = train_l
        self.val_l = val_l
        
        self.model = resnet18CIFAR10()
        

    def forward(self, x):
        out = self.model(x)
        
        return F.log_softmax(out, dim=1)

    def training_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        
        loss = F.nll_loss(logits, y)
        self.log("train_loss", loss)
        
        return loss

    def evaluate(self, batch, stage=None):
        x, y = batch
        logits = self(x)
        loss = F.nll_loss(logits, y)
        preds = torch.argmax(logits, dim=1)
        acc = accuracy(preds, y)

        if stage:
            self.log(f"{stage}_loss", loss, prog_bar=True)
            self.log(f"{stage}_acc", acc, prog_bar=True)

    def validation_step(self, batch, batch_idx):
        self.evaluate(batch, "val")


    def configure_optimizers(self):
        return Adam([p for p in self.parameters() if p.requires_grad], lr=0.02, eps=1e-08)


    def train_dataloader(self):
        return self.train_l

    def val_dataloader(self):
        return self.val_l

    
model = BoilerPlate(trainloader, testloader)
trainer = pl.Trainer(
    progress_bar_refresh_rate=10,
    max_epochs=300,
    gpus=1,
    logger=pl.loggers.TensorBoardLogger("lightning_logs/", name="resnet18_cifar10_baseline"),
)
trainer.fit(model)


test_transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])


batch_size = 64
testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                       download=True, transform=test_transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
                                         shuffle=False, num_workers=16)

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
model.to(device)
model.eval()
preds, labels = [], []
for batch in testloader:
    x, y = batch
    x = x.to(device)
    logits = model(x)
    y_pred = torch.argmax(logits, dim=1)
    
    preds.append(y_pred.cpu().numpy())
    labels.append(y.cpu().numpy())

preds = np.concatenate(preds)
labels = np.concatenate(labels)
print(classification_report(labels, preds, target_names=classes))