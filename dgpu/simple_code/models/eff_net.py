import json
from PIL import Image

import torch
from torchvision import transforms
from efficientnet_pytorch import EfficientNet

class EffNet(nn.Module):
    def __init__(self):
        super(effnet,self).__init__()
        self.main_model = EfficientNet.from_pretrained('efficientnet-b0')
    
    def forward(self,x):
        x=  self.main_model(x)
        return x