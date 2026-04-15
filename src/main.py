import numpy as np

from src.interpolation import interp
from src.readData import readTable
from src.shugar_calculations import masToDens


def main():
    # Reads T6 as np array from specified path. Format = Density, %vol, %mas, gA/100ml
    global t6
    t6 = readTable("./tables_raw/t6_nell.ods")
    # print("Desti helper:\n input datatype, value, output Datatype\n\n")
    while True:
        print("--- Desti helper main menue ---")
        print("A = Alcohol\nS = Shugar\nX = Exit")
        cmd = input()
        if cmd not in "AaSsXx":
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
        else:
            break


def alcohol():
    while True:
        print("\n--- Alcohol calculations ---\n")
        print("What data is provided?\n0 = Density\n1 = %Vol\n2 = %mas\n3 = gA/100ml\n")
        inrow = int(input())
        print("provided value:")
        value = float(input())
        print("Provide expected ouput Datatype (see input)")
        outrow = int(input())
        retval = interp(t6, inrow, outrow, value)
        print(f"interpolated Value:  {retval}\n")
        print("n for next, x to return to Menu")
        cmd = input()
        if cmd == "x":
            return


def shugar():
    while True:
        print("---Under construction---")
        print("\n---Shugar calculations---\n")
        print("Provide concentration of shugar soluion in %mas")
        mas = float(input())
        dens = masToDens(mas)
        print(f"Density = {dens}")

        print("n for next, x to return to Menu")
        cmd = input()
        if cmd == "x":
            return


main()
