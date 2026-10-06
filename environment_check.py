import sys
import torch
import torchvision

print('Python:', sys.version.split()[0])
print('PyTorch:', torch.__version__)
print('Torchvision:', torchvision.__version__)
print('CUDA available:', torch.cuda.is_available())
if torch.cuda.is_available():
    print('GPU:', torch.cuda.get_device_name(0))
    print('CUDA runtime used by PyTorch:', torch.version.cuda)
