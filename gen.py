import sys
import random
from PIL import Image
import numpy as np
from noise import pnoise2
import utils

w, h = 1024, 1024

data = np.zeros((h, w), dtype=np.uint8)


r = random.randint(0,255)
print(r)
shape = (1024,1024)
scale = 200.0
octaves = 6
persistence = 0.5
lacunarity = 2.0
a = []

world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = pnoise2(i/scale, 
                                    j/scale, 
                                    octaves=octaves, 
                                    persistence=persistence, 
                                    lacunarity=lacunarity, 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=r) +0.5

# print(max(data.all()))
data = utils.landify(world, w, h)
img = Image.fromarray(data, 'RGB')
img.save('out\world.png')
# img.show()@
