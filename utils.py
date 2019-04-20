import numpy as np

SNOW = [238,240,242]
MOUNTAIN = [108, 122, 137]
LAND = [30, 130, 76]
SAND = [255, 246, 143]
SEA = [44, 130, 201]
DEEP_SEA = [34, 110, 180]

def normalise(n,min, max):
    return (n - min) / (max - min)

def landify(data, w, h):
    retVal = np.zeros((h, w, 3), dtype=np.uint8)
    for x in range(0,w):
        for y in range(0,h):
            i = data[x,y]
            if i >= 0.9:
                retVal[x,y] = SNOW
            elif i >= 0.75:
                retVal[x,y] = MOUNTAIN
            elif i >= 0.6:
                retVal[x,y] = LAND
            elif i >= 0.55 and i < 0.6:
                retVal[x,y] = SAND
            elif i >= 0.25:
                retVal[x,y] = SEA
            else:
                retVal[x,y] = DEEP_SEA
    return retVal
