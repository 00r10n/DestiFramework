import numpy as np



def interp(array, inrow, outrow, value):
    if value in array[inrow, :]:
        index = np.where(array[inrow, :] == value)
        return array[outrow, index]
    upper_index = np.searchsorted(array[inrow, :], value)
    lower_index = upper_index - 1
    upper_x = array[inrow, upper_index]
    lower_x = array[inrow, lower_index]
    fract = (value - lower_x) / (upper_x - lower_x)
    upper_y = array[outrow, upper_index]
    lower_y = array[outrow, lower_index]
    y = lower_y + (upper_y - lower_y) * fract
    return y
