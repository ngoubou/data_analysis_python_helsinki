#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(painting):
    for i in painting[:,:,:]:
        for j in i:
            j[0] = 0.2126 * j[0]
            j[1] = 0.7152 * j[1]
            j[2] = 0.0722 * j[2]
    result = painting[:,:,0] # drop the last dimension of the array
    return result

def main():
    image = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part03-e11_to_grayscale/src/painting.png"
    painting = plt.imread(image)
    #print(to_grayscale(painting))
    plt.imshow(to_grayscale(painting));
    plt.gray()
    #pass

if __name__ == "__main__":
    main()

## Course Solution ----
# I did not at all understand what was asked.
# I copied someone else code on the discord server and realized how far off i was
# It was way simpler than i thought