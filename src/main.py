import numpy as np

from readData import readT6


def main():
    # Reads T6 as np array from specified path. Format = Density, %vol, %mas, gA/100ml
    t6 = readT6("../tables_raw/t6_nell.ods")
    print(np.shape(t6))
    print(t6[:5, :])


main()
