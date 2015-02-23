""" Recursive art, code generated as part of Software Design course, Spring 2015. Author: Celine Ta, scaffold provided by instructors."""

from math import *
import random
from PIL import Image
import pdb

def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list

                Nested list should consist of the following: 
                prod(a,b) = ab
                avg(a,b) = 0.5*(a+b)
                cos_pi(a) = cos(pi*a)
                sin_pi(a) = sin(pi*a)
                x(a,b) = a
                y(a,b) = b
                rnd(a) = round(a)
                rad(a) = sqrt(a**2 + b**2)

        ["cos_pi", ["prod", ["x", "y"] ] ] -> lambda x,y: cos(pi*(lambda x,y: (lambda x,y: x)(x,y)*(lambda x,y: y)(x,y))(x,y)).

        TODO: make doctests
    """
    depth = random.randint(min_depth, max_depth)
    if depth==1:
        choice = random.randint(1,2)
        if choice==1:
            return lambda x,y: x
        elif choice==2:
            return lambda x,y: y
    else:
        choice = random.randint(1,6)
        f = build_random_function(depth -1 , depth - 1)
        if choice==1: #cosine
            return lambda x, y: cos(pi*f(x,y))
        elif choice==2: #sine
            return lambda x, y: sin(pi * f(x,y))
        elif choice==3: #round
            return lambda x, y: round(f(x,y))
        elif choice==4: #avg
            g = build_random_function(depth-1, depth-1)
            return lambda x, y: (f(x,y)+g(x,y))*.5
        elif choice==5: #prod
            g = build_random_function(depth-1, depth-1)
            return lambda x, y: f(x,y)* g(x,y)
        elif choice==6: #distance
            g = build_random_function(depth - 1, depth - 1)
            return lambda x, y: sqrt((f(x,y))**2+(g(x,y))**2)

def evaluate_random_function(gen_func, x, y):
 
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        Using lambda functions will allow you to return a variable of type function from your build_random_function code.  In order to evaluate
        the function at a particular (x,y) pair all you have to do is pass (x,y) into your function variable (this obviates the need for 
        evaluate_random_function).  For instance,

        green = build_random_function(7,9)
        green_channel_pixel_for_x_y = green(x,y)


        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02
        >>> evaluate_random_function(["avg"],0.5,0.4)
        0.45
        >>> evaluate_random_function(["prod"],0.5,0.4)
        0.2
        >>> evaluate_random_function(["cos_pi"], 1)
        -1.0
        >>> evaluate_random_function(["sin_pi"], 1)
        0.0
        >>> evaluate_random_function(["rnd"],0.5)
        1.0
        >>> evaluate_random_function(["rad"],0.7,0.4)
        0.8062257748298549
    """

    a = gen_func(x,y)
    # print a
    return a

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
        >>> remap_interval(0.0,-1,1,0,255)
        127.5
    """
    proportion= float(val - input_interval_start)/(input_interval_end - input_interval_start)
    return proportion*(output_interval_end - output_interval_start) + output_interval_start

def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide

    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """ Generate test image with random pixels and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


def generate_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    red_func=build_random_function(7,9)
    green_func=build_random_function(7,9)
    blue_func=build_random_function(7,9)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            # print "i", i, "j", j
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(evaluate_random_function(red_func, x, y)),
                    color_map(evaluate_random_function(green_func, x, y)),
                    color_map(evaluate_random_function(blue_func, x, y))
                    )

    im.save(filename)


if __name__ == '__main__':
    import doctest

    #doctest.run_docstring_examples(remap_interval, globals())
    #doctest.testmod()
    
    # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #       implement remap_interval and evaluate_random_function
    generate_art("myart4_lambda.png")

    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
    #test_image("noise.png")
    