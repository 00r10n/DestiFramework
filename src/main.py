import numpy as np

from src.interpolation import interp
from src.readData import readTable
from src.shugar_calculations import shugars


def main():
    # Reads T6 as np array from specified path. Format = Density, %vol, %mas, gA/100ml
    global t6
    t6 = readTable("./tables_raw/t6_nell.ods")
    # print("Desti helper:\n input datatype, value, output Datatype\n\n")
    while True:
        print("--- Desti helper main menue ---")
        print("A = Alcohol\nS = Shugar\nX = Exit")

        cmd = input()
        if len(cmd) != 1 or cmd not in "aAsSxX":
            print("invalid command\n-----------------\n\n")
            continue

        if cmd in "Aa":
            alcohol()
            print("\n\n")
            continue
        if cmd in "Ss":
            shugar()
            print("\n\n")
            continue
        if cmd in "Xx":
            break


def alcohol():
    while True:
        print("\n--- Alcohol calculations ---\n")
        print("What data is provided?\n0 = Density\n1 = %Vol\n2 = %mas\n3 = gA/100ml\n")
        try:
            inrow = int(input())
        except TypeError:
            print("invalid input")
            continue
        if not 0 <= inrow <= 3:
            print("invalid input")
            continue
        print("provided value:")
        try:
            value = float(input())
        except TypeError:
            print("invalid input")
            continue
        # if not 0<=value<=100:
        #    print("invalid input")
        #    continue
        print("Provide expected ouput Datatype (see input)")
        try:
            outrow = int(input())
        except TypeError:
            print("invalid input")
            continue
        if not 0 <= outrow <= 3:
            print("invalid input")
            continue
        retval = interp(t6, inrow, outrow, value)
        print(f"interpolated Value:  {retval}\n")
        print("n for next, x to return to Menu")
        cmd = input()
        if cmd == "x":
            return


def shugar():
    while True:
        print("---Under construction---")
        print(
            "\n---Shugar calculations---\ncurrently only %mas input allowed\n-------------------------\n"
        )
        print("Povide input data type:\n0 = Denity\n1 = %mas\n3 = gram/100ml\n")
        try:
            inType = int(input())
        except TypeError:
            print("invalid Input")
            continue
        print("Provide input value")
        try:
            inVal = float(input())
        except TypeError:
            print("invalid input")
            continue
        print("Provide output data type (see input)")
        outType = int(input())
        outVal = shugars(inType, outType, inVal)
        print(f"\nCalculation returned: {outVal}\n--------------")

        print("\n\nn for next, x to return to Menu")
        cmd = input()
        if cmd == "x":
            return


main()
