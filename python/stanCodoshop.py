"""
File: stanCodoshop.py
Name: Sung Mien huang
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    return ((pixel.red-red)**2+(pixel.blue - blue)**2+(pixel.green - green)**2)**0.5


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # lst_red = []
    # lst_blue = []
    # lst_green = []
    # lst_avg = []
    # for pixel in pixels:         # we separate red, blue, green into different list
    #     lst_red.append(pixel.red)
    #     lst_blue.append(pixel.blue)
    #     lst_green.append(pixel.green)
    # t_r = 0                      # we count red, blue, green list separately
    # for red_pixel in lst_red:
    #     t_r += red_pixel
    # avg_red = t_r // len(lst_red)
    # lst_avg.append(avg_red)
    # t_g = 0
    # for green_pixel in lst_green:
    #     t_g += green_pixel
    # avg_green = t_g // len(lst_green)
    # lst_avg.append(avg_green)
    # t_b = 0
    # for blue_pixel in lst_blue:
    #     t_b += blue_pixel
    # avg_blue = t_b // len(lst_blue)
    # lst_avg.append(avg_blue)
    # return lst_avg
    red_total = sum(pixel.red for pixel in pixels)
    green_total = sum(pixel.green for pixel in pixels)
    blue_total = sum(pixel.blue for pixel in pixels)
    return [red_total/len(pixels), green_total/len(pixels), blue_total/len(pixels)]

def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance",
    which has the closest color to the average.
    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # avg_color = get_average(pixels)          # first find the average distance in this image
    # lst_avg_color_distance = []
    # for pixel in pixels:                    # find the distance between the pixels input and average
    #     avg_color_distance = get_pixel_dist(pixel, avg_color[0], avg_color[1], avg_color[2])
    #     lst_avg_color_distance.append(avg_color_distance)
    # smallest_distance = lst_avg_color_distance[0]     # find the smallest distance
    # for color in lst_avg_color_distance:
    #     if color <= smallest_distance:
    #         smallest_distance = color
    # for pixel in pixels:                   # find which pixel contributed the smallest distance
    #     if get_pixel_dist(pixel, avg_color[0], avg_color[1], avg_color[2]) == smallest_distance:
    #         return pixel
    avg_color = get_average(pixels)
    lst =[]
    for pixel in pixels:
        avg_color_distance = get_pixel_dist(pixel, avg_color[0], avg_color[1], avg_color[2])
        lst.append((avg_color_distance, pixel))
    return min(lst, key=lambda t: t[0])[1]

def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for x in range(result.width):
        for y in range(result.height):
            lst_pixels = [image.get_pixel(x,y) for image in images]
            # for image in images:
            #     image_p = image.get_pixel(x, y)   # list the pixel at same (x,y) in different image
            #     lst_pixels.append(image_p)
            best = get_best_pixel(lst_pixels)     # find the best pixel
            result_f = result.get_pixel(x, y)     # put it at the (x,y) at the result image
            result_f.red = best.red
            result_f.blue = best.blue
            result_f.green = best.green
    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
