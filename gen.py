import sys
import random
from PIL import Image
import numpy as np
from noise import pnoise2
import utils

w, h = 512, 512

r = random.randint(0, 255)
print(r)

canvas = (w, h)
scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0

world = np.zeros(canvas)
for row in range(canvas[0]):
    for col in range(canvas[1]):
        world[row][col] = utils.normalise(pnoise2(row/scale,
                                                  col/scale,
                                                  octaves=octaves,
                                                  persistence=persistence,
                                                  lacunarity=lacunarity,
                                                  repeatx=1024,
                                                  repeaty=1024,
                                                  base=r), -0.5, 0.5)


data = utils.landify(world, w, h)
img = Image.fromarray(data, 'RGBA')
img.save('out\world.png')
# img.show()
