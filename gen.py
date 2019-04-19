import sys
from PIL import Image
import numpy as np

print(sys.version)

w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[0:,0:] = [0, 0, 255]
img = Image.fromarray(data, 'RGB')
img.save('out/world.png')
#img.show()