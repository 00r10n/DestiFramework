def getInput(expectedType, legals=[]):
    value = input()
    if expectedType == "int":
        try:
            sanVal = int(value)
        except TypeError:
            print("invalid Input provided, try again")
            return None
        if legals and sanVal not in legals:
            return None
            print("invalid Input provided, try again")
    elif expectedType == "float":
        try:
            sanVal = float(value)
        except TypeError:
            print("invalid Input provided, try again")
            return None
    elif expectedType == "char":
        if len(value) != 1 or value not in legals:
            print("invalid Input provided, try again")
            return None
        sanVal = value

    else:
        return None
    return sanVal
