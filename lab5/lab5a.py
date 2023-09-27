import cv2
import os
import numpy
import math

os.chdir("/Users/noahljungberg/PycharmProjects/tdde23-2023-labbar-05-u1-b-02/lab5")


def cvimg_to_list(image):
    """Tar en bild och returnerar en lista av tupler med alla bilder för varje pixel i en bild"""
    rad, kolumn, _ = img.shape  # Vi ger rad första värdet (dvs höjden) av img.shape och kolumn (dvs bredden) andra värdet tredje värdet ignoreras genom _
    return [(tuple(image[y, x])) for y in range(rad) for x in range(kolumn)]  # skapa en lista med tupler för alla färger

# print(cvimg_to_list("image.jpg"))

def double_elements(int_list):
    """Takes a list of ints and return their value times two"""
    return [i * 2 for i in int_list]


def all_pairs_ordered(number):
    """Takes a number and makes ordered pairs"""
    return [(i, j) for i in range(number + 1) for j in range(number + 1)]


def disrtribute(anything, some_lists):
    return [i + [anything] for i in some_lists]


def rem_negative(list_of_int):
    return [i for i in list_of_int if (i >= 0)]


def int_first_letter(list_of_str):
    return [ord(i[0]) for i in list_of_str]


def unsharp_mask(N):
    """"Skapar en 2d lista, NxN, för att öka skärpan i en bild m.h.a. opencv"""
    S = 4.5  # konstant värde
    return \
        [
            [
                (-1 / (2 * math.pi * (S ** 2))) * math.exp(
                    -(x ** 2 + y ** 2) / (2 * (S ** 2)))  # formeln för negativ gaussisk blur
                if not (x == 0 and y == 0)
                else 1.5  # om x och y är 0 skapa en 2d lista med 1.5
                for x in range(-(N // 2), N // 2 + 1)
            ]
            for y in range(-(N // 2), N // 2 + 1)
        ]


print(unsharp_mask(1))
