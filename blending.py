import utils
from operator import mul

def multiply(base, new):    
    base = utils.normalise_many(list(base), 0, 255)
    base = list(map(lambda x:x*base[3], base[:3])) # Multiply by opacity

    new  = utils.normalise_many(list(new), 0, 255)
    new = list(map(lambda x:x*new[3], new[:3])) # Multiply by opacity    

    combined = list(map(mul, base, new))
    combined = list(map(lambda x:x*255, combined))
    combined.append(255)
    return combined

def overlay(base, new):
    base = utils.normalise_many(list(base), 0, 255)
    base = list(map(lambda x:x*base[3], base[:3])) # Multiply by opacity

    new = utils.normalise_many(list(new), 0, 255)
    new = list(map(lambda x:x*new[3], new[:3])) # Multiply by opacity    
    blended = []
    for i in range(3):
        if base[i] > 0.5:
            c = 1 - (1 - 2 * (base[i] / 2) * (1 - new[i]))
        else:
            c = (2 * base[i]) * new[i]
        blended.append(c)
    blended = list(map(lambda x:x*255, blended))
    blended.append(255)
    return blended