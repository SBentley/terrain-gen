import numpy as np

mountain = [108, 122, 137]
land = [30, 130, 76]
sand = [255, 246, 143]
sea = [44, 130, 201]
def normalise(n,min, max):
    return (n - min) / (max - min)

def landify(data, w, h):
    ret = np.zeros((h, w, 3), dtype=np.uint8)
    for x in range(0,w):
        for y in range(0,h):
            i = data[x,y]
            #print(i)
            if i > 0.75:
                ret[x,y] = mountain
            elif i >= 0.6:
                ret[x,y] = land
            elif i > 0.55 and i < 0.6:
                ret[x,y] = sand
            else:
                ret[x,y] = sea
            
    return ret
