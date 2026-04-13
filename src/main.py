import numpy as np

from src.readData import readTable


def main():
    # Reads T6 as np array from specified path. Format = Density, %vol, %mas, gA/100ml
    t6 = readTable("./tables_raw/t6_nell.ods")
    print(np.shape(t6))
    print(t6[:1, :])


main()
