
# packages

from PIL import Image
from random import *
from math import *
import multiprocessing
from functions import *



# global variables

res_x = 1920
res_y = 1080

range_x = { "min": -1.920, "max": 1.920 }
range_y = { "min": -1.080, "max": 1.080 }
range_x["step"] = (range_x["max"] - range_x["min"]) / res_x
range_y["step"] = (range_y["max"] - range_y["min"]) / res_y
iterations = 20
breakpoint = 4



# functions

def calc_x (info):
    val_x = info["val_x"]
    val_y = info["val_y"]
    iterations = info["iterations"]
    breakpoint = info["breakpoint"]

    # create new imaginary number object with properties
    obj = Imaginary(val_x, val_y)
    cval = Imaginary(0, 0)
    # check if distance is between 0 and 2 on complex plane
    for i in range(0, iterations):
        cval = cval.pow(2).add(obj)
        if cval.get_distance_sq() > breakpoint:
            return (i / 50) if (i / 50) < 1 else 1
    # calculate the distance squared
    distance_sq = cval.get_distance_sq()
    if distance_sq <= 4:
        return -1
    else:
        return 1



if __name__ == "__main__":

    pool = multiprocessing.Pool()

    # get the total width and height of the image
    img_w = int((range_x["max"] - range_x["min"]) / range_x["step"])
    img_h = int((range_y["max"] - range_y["min"]) / range_y["step"])

    data = []

    for y in range(0, img_h):
        print(str(round(y / img_h * 100, 2)) + "% done")
        # calculate current x-coord
        val_y = range_y["min"] + (y * range_y["step"])
        x_list = [range_x["min"] + (x * range_x["step"]) for x in range(0, img_w)]
        list = [{"val_y": val_y, "val_x": x, "iterations": iterations, "breakpoint": breakpoint} for x in x_list]
        results = pool.map(calc_x, list)

        for r in results:
            if r == -1:
                data.append((0, 0, 0))
            else:
                data.append((255, (floor(r * 255)), (floor(r * 255))))


    img = Image.new('RGB', (img_w, img_h), "white")
    img.putdata(data)
    img.save("img.png")
