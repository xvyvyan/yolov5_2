import numpy as np
import cv2
from PIL import Image

if __name__ == '__main__':
    path="./data/images/bus.jpg"
    img=cv2.imread(path)
    Image.fromarray(img[:,:,::-1]).show()
    pass