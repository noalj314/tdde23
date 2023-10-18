
import cv2
import os
import numpy as np
import math
import random
from cvlib import *
from lab5a import *

os.chdir("/Users/noahljungberg/PycharmProjects/tdde23-2023-labbar-05-u1-b-02/lab5")

def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """Takes upper and lower values for hsv then returns 1 or 0 depending on the function is_in_range_color """
    def is_in_range_color(hsv_pixel):
        # Raise an exception om hsv_pixel inte är en tuple som är längd tre
        if not isinstance(hsv_pixel, tuple) or len(hsv_pixel) != 3:
            raise TypeError("Invalid pixel input in pixel_constraint")
        hue, saturation, value = hsv_pixel
        if not (isinstance(hue, numpy.uint8) and isinstance(saturation, numpy.uint8) and isinstance(value, numpy.uint8)):
            raise TypeError("Invalid pixel input in pixel_constraint")
        if not (0 <= hue <= 255 and 0 <= saturation <= 255 and 0 <= value <= 255 ):
            raise ValueError("Invalid pixel input in pixel_constraint")
        return 1 if (hlow <= hue <= hhigh and slow <= saturation <= shigh and vlow <= value <= vhigh) else 0


    return is_in_range_color

def generator_from_image(image_list):
    """Returns the color value of a pixel for a given index in a image_list"""
    def pixel(index):
        # lägg till en check om indexet är för stort
        if index >= len(image_list):
            raise IndexError("Index out of range in generator_from_image.")
        return image_list[index]
    return pixel
"""
### lab 5b1
hsv_plane = cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_BGR2HSV)

plane_list = cvimg_to_list(hsv_plane)

is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)
sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))

#cv2.imshow('sky', greyscale_list_to_cvimg(sky_pixels, hsv_plane.shape[0], hsv_plane.shape[1]))
#cv2.waitKey(0)


#labb5b2
orig_img = cv2.imread("plane.jpg")
orig_list = cvimg_to_list(orig_img)

generator = generator_from_image(orig_list)

new_list = [generator(i) for i in range(len(orig_list))]

#cv2.imshow('original', orig_img)
#cv2.imshow('new', rgblist_to_cvimg(new_list, orig_img.shape[0], orig_img.shape[1]))
#cv2.waitKey(0)



"""

#lab5 b3

# Skapa en generator som gör en stjärnhimmel
def generator1(index):
    """Returns a value of (0,0,0) or a white colored tuple with one perecent"""
    val = random.random() * 255 if random.random() > 0.99 else 0
    random_hsv_color = cv2.cvtColor(np.array([[(val,val,val)]], dtype=np.uint8), cv2.COLOR_BGR2HSV)
    return random_hsv_color[0][0]

def hsv_pixel_to_bgr_pixel(pixel_checker):
    """Makes a hsv pixel into a bgr pixel"""
    bgr_array = cv2.cvtColor(np.array([[pixel_checker]], dtype=np.uint8), cv2.COLOR_HSV2BGR)
    return tuple(map(int, bgr_array[0][0]))

def pixel_checker(pixel_index):
    """checks if a pixel is within the pixel constraints given by the condition"""
    return generator1(generator1(pixel_index)) if condition(generator2(pixel_index)) == 1 else generator2(pixel_index)

def combine_images(plane_hsv_list, condition, generator1, generator2):
    """Replaces the sky with black and then adds randomly generated stars to the night sky"""
    try:
        # Använd list comprehension med en try-except block för att hantera exceptions per pixel
        bgr_list = [hsv_pixel_to_bgr_pixel(pixel_checker(pixel_index)) for pixel_index in range(len(plane_hsv_list))]
    except (TypeError, IndexError):
        # fånga om exceptions som uppstår inuti list comprehension
        raise Exception("An error occurred while combining images: check the input ")
    return bgr_list


# Läs in en bild
plane_img = cv2.imread("plane.jpg")

# Skapa ett filter som identifierar himlen
condition = pixel_constraint(100, 150, 50, 200, 100, 255)

# Omvandla originalbilden till en lista med HSV-färger
plane_hsv_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))

# Skapa en generator för den inlästa bilden
generator2 = generator_from_image(plane_hsv_list) #bytte till plane_hsv_list från plane_img_list

# Kombinera de två bilderna till en, alltså använd himmelsfiltret som mask
result = combine_images(plane_hsv_list, condition, generator1, generator2)

# Omvandla resultatet till en riktig bild och visa upp den
new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])
#cv2.imshow('Final image', new_img)
#cv2.waitKey(0)



def mask_function(generator_plane, generator_flower, condition):
    """Combines pixels into one"""
    def inner_mask_function(index):
        return add_tuples(multiply_tuple(generator_plane(index), (1- condition(generator_gradiennt(index)))), multiply_tuple(generator_flower(index), (condition(generator_gradiennt(index)))))
    return inner_mask_function

def condition1(pixel):
    """Takes a pixel and divides it by 255 to get a value between 1 or 0"""
    return pixel /255

def combine_images2(mask):
    """Calls the mask_function for all index in the plane_bgr_list"""
    return [mask(index) for index in range(len(plane_bgr_list))]
"""
#Load all images
flowers = cv2.imread("flowers.jpg")
gradient = cv2.imread("gradient.jpg", cv2.IMREAD_GRAYSCALE)
plane_img = cv2.imread(("plane.jpg"))

#Create list for all colors
flowers_bgr_list = cvimg_to_list(flowers)
plane_bgr_list = cvimg_to_list(plane_img)
gradient_list = cvimg_to_list(gradient)


##Generates pixel values for a given index for the different lists
generator_plane = generator_from_image(plane_bgr_list) #Generates pixel values for a given index for the plane list
generator_flower = generator_from_image(flowers_bgr_list) #Generates pixel values for a given index  for the flower list
generator_gradiennt = generator_from_image(gradient_list)

#Make the calculated returned value of the mask_function
mask = mask_function(generator_plane, generator_flower, condition1)


#Call the function
resulted = combine_images2(mask)


#Make the resulted list into an image
new_img2 = rgblist_to_cvimg(resulted, plane_img.shape[0], plane_img.shape[1])

#Show the image
#cv2.#imshow("kejdjeid",new_img2)
#cv2.waitKey(0)

"""