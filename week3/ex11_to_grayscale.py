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

# The copied code
def to_grayscale(filename):  
    img = filename.copy()
    R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]
    img = 0.2126 * R + 0.7152 * G + 0.0722 * B 
    return img

def to_red(threeDArray):
    img = threeDArray.copy()
    img[:,:,1] = 0
    img[:,:,2] = 0
    return img 

def to_green(threeDArray):
    img = threeDArray.copy()
    img[:,:,0] = 0
    img[:,:,2] = 0
    return img 

def to_blue(threeDArray):
    img = threeDArray.copy()
    img[:,:,0] = 0
    img[:,:,1] = 0
    return img 

# The course solution

def to_grayscale(image):
    
    w=np.array([0.2126, 0.7152, 0.0722]).reshape(1, 1, 3)

    a = image * w

    return a.sum(axis=2)
 

def to_red(image):

    image2=image.copy()

    image2[:,:,[1,2]] = 0

    return image2

 

def to_green(image):

    image2=image.copy()

    image2[:,:,[0,2]] = 0

    return image2

 

def to_blue(image):

    image2=image.copy()

    image2[:,:,[0,1]] = 0

    return image2

 

def main():

    painting=plt.imread("src/painting.png")

    gray = to_grayscale(painting)

    red = to_red(painting)

    green = to_green(painting)

    blue = to_blue(painting)

    plt.imshow(painting)

    plt.figure()

    plt.gray()

    plt.imshow(gray)

    plt.subplot(3, 1, 1)

    plt.imshow(red)

    plt.subplot(3, 1, 2)

    plt.imshow(green)

    plt.subplot(3, 1, 3)

    plt.imshow(blue)

    plt.show()