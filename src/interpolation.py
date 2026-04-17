import numpy as np


def interp(array, inrow, outrow, value):
    if inrow == outrow:
        return "you serious?"
    if value in array[:, inrow]:
        index = np.where(array[:, inrow] == value)
        return array[index, outrow]
    upper_index = np.searchsorted(array[:, inrow], value)
    lower_index = upper_index - 1
    upper_x = array[upper_index, inrow]
    lower_x = array[lower_index, inrow]
    fract = (value - lower_x) / (upper_x - lower_x)
    upper_y = array[upper_index, outrow]
    lower_y = array[lower_index, outrow]
    y = lower_y + (upper_y - lower_y) * fract
    return y
