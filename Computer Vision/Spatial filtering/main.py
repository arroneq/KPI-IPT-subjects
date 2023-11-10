from cmath import log
import skimage.exposure as ski
import matplotlib.pyplot as plt
import scipy.signal as scp

import numpy as np

from PIL import Image
from matplotlib.image import imread
import cv2 as cv

def negative(path):
    input_image = Image.open(path)

    plt.figure(figsize=(14, 7))

    plt.subplot(1,2,1)
    plt.title("Input image")
    plt.imshow(cv.imread(path))
    plt.xticks([])
    plt.yticks([])

    pixel_map = input_image.load()
    width, height = input_image.size

    def T(r):
        return 255-r

    for i in range(width):
        for j in range(height):
            r = input_image.getpixel((i, j))
            s = T(r)
            pixel_map[i, j] = s
    
    input_image.save("output images/pic1.png", format="png")

    plt.subplot(1,2,2)
    plt.title("Output image")
    plt.imshow(cv.imread("output images/pic1.png"))
    plt.xticks([])
    plt.yticks([])

    return plt.show()

# negative("input images/pic1.jpg")

def logarithm(path,c):
    input_image = Image.open(path)

    plt.figure(figsize=(14, 7))

    plt.subplot(1,2,1)
    plt.title("Input image")
    plt.imshow(cv.imread(path))
    plt.xticks([])
    plt.yticks([])

    pixel_map = input_image.load()
    width, height = input_image.size

    def T(r,c):
        return c*np.log10(1+r)

    for i in range(width):
        for j in range(height):
            r = input_image.getpixel((i, j))
            s = T(r,c)
            pixel_map[i, j] = int(s)
    
    input_image.save("output images/pic2.png", format="png")

    plt.subplot(1,2,2)
    plt.title("Output image")
    plt.imshow(cv.imread("output images/pic2.png"))
    plt.xticks([])
    plt.yticks([])

    return plt.show()

# logarithm("input images/pic2.jpg",50)

def exponentiation(path,c,gamma):
    input_image = Image.open(path)

    plt.figure(figsize=(14, 7))

    plt.subplot(1,2,1)
    plt.title("Input image")
    plt.imshow(cv.imread(path))
    plt.xticks([])
    plt.yticks([])

    pixel_map = input_image.load()
    width, height = input_image.size

    def T(r,c,gamma):
        return c*r**gamma

    for i in range(width):
        for j in range(height):
            r = input_image.getpixel((i, j))
            s = T(r,c,gamma)
            pixel_map[i, j] = int(s)
    
    input_image.save("output images/pic3.png", format="png")

    plt.subplot(1,2,2)
    plt.title("Output image")
    plt.imshow(cv.imread("output images/pic3.png"))
    plt.xticks([])
    plt.yticks([])

    return plt.show()

# exponentiation("input images/pic3.jpg",10,1)

def stretching(path,m,E):
    input_image = Image.open(path)

    plt.figure(figsize=(14, 7))

    plt.subplot(1,2,1)
    plt.title("Input image")
    plt.imshow(cv.imread(path))
    plt.xticks([])
    plt.yticks([])

    pixel_map = input_image.load()
    width, height = input_image.size

    def T(r,m,E):
        return 255/(1+pow(m/r,E))

    for i in range(width):
        for j in range(height):
            r = input_image.getpixel((i, j))
            s = T(r,m,E)
            pixel_map[i, j] = int(s)
    
    input_image.save("output images/pic4.png", format="png")

    plt.subplot(1,2,2)
    plt.title("Output image")
    plt.imshow(cv.imread("output images/pic4.png"))
    plt.xticks([])
    plt.yticks([])

    return plt.show()

# stretching("input images/pic4.jpg",100,5)

def equalize(path):
    input_image = imread(path) # imread: image -> ndarray, but Image.open: image -> JPG.object
    width, height = input_image.shape

    plt.figure(figsize=(14, 14))

    plt.subplot(2,2,1)
    plt.title("Input image")
    plt.imshow(cv.imread(path))
    plt.xticks([])
    plt.yticks([])

    # initial histogram
    plt.subplot(2,2,2)
    plt.hist(input_image.ravel(), bins=256, range=(0,255))
    plt.title("Initial histogram")

    equalized_image = ski.equalize_hist(input_image.ravel()) 
    # input_image.ravel(): ndarray -> array, ski.equalize_hist() onto (0,1)

    # equalized histogram
    plt.subplot(2,2,4)
    plt.hist(255*equalized_image, bins=256, range=(0,255))
    plt.title("Equalized histogram")

    output_image_array = np.uint8(255*equalized_image) # array -> uint8(array)  
    output_image_array = output_image_array.reshape((width, height)) # array -> ndarray

    output_image = Image.fromarray(output_image_array)
    output_image.save("output images/pic5.png", format="png")

    plt.subplot(2,2,3)
    plt.title("Output image")
    plt.imshow(cv.imread("output images/pic5.png"))
    plt.xticks([])
    plt.yticks([])

    return plt.show()

# equalize("input images/pic5.jpg")

def linear_filter(path, kind):
    input_image = cv.imread(path)

    plt.figure(figsize=(14, 7))

    plt.subplot(1,2,1)
    plt.title("Input image")
    plt.imshow(cv.imread(path))
    plt.xticks([])
    plt.yticks([])

    if (kind == "average"):
        kernel = np.array([[1/9,1/9,1/9],
                           [1/9,1/9,1/9],
                           [1/9,1/9,1/9]])

    if (kind == "Gaussian"):
        kernel = np.array([[1/16,2/16,1/16],
                           [2/16,4/16,2/16],
                           [1/16,2/16,1/16]])

    filtered_image = cv.filter2D(input_image, -1, kernel)
    # ddepth: It is the desirable depth of destination image
    # value -1 represents that the resulting image will have same depth as the source image

    output_image = Image.fromarray(filtered_image)
    output_image.save("output images/pic6.png", format="png")

    plt.subplot(1,2,2)
    plt.title("Output image")
    plt.imshow(cv.imread("output images/pic6.png"))
    plt.xticks([])
    plt.yticks([])

    return plt.show()

# linear_filter("input images/pic6.jpg", "average")

def laplacian(path):
    input_image = cv.imread(path, cv.IMREAD_GRAYSCALE).astype("int16")
    width, height = input_image.shape

    plt.figure(figsize=(15, 5))

    plt.subplot(1,3,1)
    plt.title("Input image")
    plt.imshow(cv.imread(path))
    plt.xticks([])
    plt.yticks([])

    filter = np.array([[0,1,0],
                       [1,-4,1],
                       [0,1,0]])

    laplacian_image = cv.filter2D(input_image, -1, filter)

    pixels = np.clip((input_image - laplacian_image), 0, 255).astype("uint8")

    laplacian_image = Image.fromarray(laplacian_image)
    laplacian_image.save("output images/pic7.png", format="png")

    plt.subplot(1,3,2)
    plt.title("laplacian image")
    plt.imshow(cv.imread("output images/pic7.png"))
    plt.xticks([])
    plt.yticks([])

    output_image = Image.fromarray(pixels)
    output_image.save("output images/pic7.png", format="png")

    plt.subplot(1,3,3)
    plt.title("Output image")
    plt.imshow(cv.imread("output images/pic7.png"))
    plt.xticks([])
    plt.yticks([])

    return plt.show()

# laplacian("input images/pic7.jpg")

def Sobel(path):
    input_image = cv.imread(path)

    plt.figure(figsize=(14, 7))

    plt.subplot(1,2,1)
    plt.title("Input image")
    plt.imshow(cv.imread(path))
    plt.xticks([])
    plt.yticks([])

    filter = np.array([[1,2,1],
                       [0,0,0],
                       [-1,-2,-1]])

    filtered_image = cv.filter2D(input_image, -1, filter)

    output_image = Image.fromarray(filtered_image)
    output_image.save("output images/pic8.png", format="png")

    plt.subplot(1,2,2)
    plt.title("Output image")
    plt.imshow(cv.imread("output images/pic8.png"))
    plt.xticks([])
    plt.yticks([])

    return plt.show()

# Sobel("input images/pic8.jpg")

def median_filter(path):
    input_image = Image.open(path) 

    plt.figure(figsize=(14, 7))

    plt.subplot(1,2,1)
    plt.title("Input image")
    plt.imshow(cv.imread(path))
    plt.xticks([])
    plt.yticks([])

    filtered_image = scp.medfilt(input_image)

    output_image = Image.fromarray(filtered_image)
    output_image.save("output images/pic9.png", format="png")

    plt.subplot(1,2,2)
    plt.title("Output image")
    plt.imshow(cv.imread("output images/pic9.png"))
    plt.xticks([])
    plt.yticks([])

    return plt.show()

# median_filter("input images/pic9.jpg")