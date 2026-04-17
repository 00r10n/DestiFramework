from input_validation import getControl, getFloat, getInt
from interpolation import interp
from readData import readTable
from shugar_calculations import shugars


def main():
    # Reads T6 as np array from specified path. Format = Density, %vol, %mas, gA/100ml
    global t6
    t6 = readTable("./tables_raw/t6_nell.ods")

    while True:
        print("--- Desti helper main menue ---")
        print("A = Alcohol\nS = Shugar\nX = Exit")

        cmd = getControl("aAsSxX")
        if cmd is None:
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
        inrow = getInt("0123")
        if inrow is None:
            continue

        print("provided value:")
        value = getFloat("alcohol", inrow)
        if value is None:
            continue

        print("Provide expected ouput Datatype (see input)")
        outrow = getInt("0123")
        if outrow is None:
            continue
        retval = interp(t6, inrow, outrow, value)
        print(f"interpolated Value:  {retval}\n")
        print("n for next, x to return to Menu")
        cmd = getControl("nx")
        if cmd is None or cmd == "n":
            continue
        else:
            return


def shugar():
    while True:
        print("---Under construction---")
        print(
            "\n---Shugar calculations---\ncurrently only %mas input allowed\n-------------------------\n"
        )
        print("Povide input data type:\n0 = Density\n2 = %mas\n3 = gram/100ml\n")

        inType = getInt(
            "2"
        )  # Currently only %mas is done, add 0 and 3 as soon as its done!
        if inType is None:
            continue

        print("Provide input value")
        inVal = getFloat("shugar", inType)
        if inVal is None:
            continue

        print("Provide output data type (see input)")
        outType = getInt("023")
        if outType is None:
            continue
        outVal = shugars(inType, outType, inVal)
        print(f"\nCalculation returned: {outVal}\n--------------")

        print("\n\nn for next, x to return to Menu")
        cmd = getControl("nx")
        if cmd is None or cmd == "n":
            continue
        else:
            return


main()
