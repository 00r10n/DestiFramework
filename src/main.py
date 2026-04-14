import numpy as np

from src.interpolation import interp
from src.readData import readTable


def main():
    # Reads T6 as np array from specified path. Format = Density, %vol, %mas, gA/100ml
    t6 = readTable("./tables_raw/t6_nell.ods")
    print("Desti helper:\n input datatype, value, output Datatype\n\n")
    while True:
        print("What data is provided?\n0 = Density\n1 = %Vol\n2 = %mas\n3 = gA/100ml\n")
        inrow = int(input())
        print("provided value:")
        value = float(input())
        print("Provide expected ouput Datatype (see input)")
        outrow = int(input())
        retval = interp(t6, inrow, outrow, value)
        print(f"interpolated Value:  {retval}\n")
        print("n for next, x for exit")
        cmd = input()
        if cmd == "x":
            break


main()
