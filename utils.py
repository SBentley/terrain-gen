import numpy as np
from operator import add
import blending

SNOW = [238, 240, 242, 255]
MOUNTAIN = [108, 122, 137, 255]
LAND = [30, 130, 76, 255]
SAND = [255, 246, 143, 255]
SEA = [44, 130, 201, 255]
DEEP_SEA = [34, 110, 180, 255]
COAST = [44, 150, 201, 255]

def normalise(n, min, max):
    return (n - min) / (max - min)

def normalise_many(data, min, max):
    for i in range(len(data)):
        data[i] = normalise(data[i], min, max)
    return data


def landify(data, w, h):
    retVal = np.zeros((h, w, 4), dtype=np.uint8)
    for row in range(0, w):
        for col in range(0, h):
            i = data[row, col]
            if i >= 0.9:
                retVal[row, col] = SNOW
            elif i >= 0.75:
                retVal[row, col] = MOUNTAIN
            elif i >= 0.58:
                retVal[row, col] = LAND
            elif i >= 0.55 and i < 0.58:
                retVal[row, col] = SAND
            elif i >= 0.50 and i < 0.55:
                #retVal[row, col] = list(map(add, SAND, COAST))
                #print(blending.multiply(SAND, COAST))
                retVal[row, col] = COAST #blending.overlay(SAND, COAST)
            elif i >= 0.25:
                retVal[row, col] = SEA
            else:
                retVal[row, col] = DEEP_SEA
    return retVal
