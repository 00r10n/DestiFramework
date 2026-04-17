def getControl(legals, number=False, max_length=1):
    raw = input()
    if len(raw) > max_length:
        print("Please enter only one character!")
        return
    if (raw not in legals) or (number and raw not in "1234567890"):
        print("The provided Input matches no legal input")
        return
    else:
        return raw


def getInt(legals, max_length=1):
    cmd = getControl(legals, True, max_length)
    if cmd:
        return int(cmd)
    else:
        return


def getFloat(
    type, row
):  # type can be either alcohol or shugar (implement enum some time!)
    raw = input()
    raw = raw.replace(",", ".")
    try:
        san = float(raw)
    except ValueError:
        print("The provided value does not match the expected type")
        return

    if 1 <= row <= 2:  # percent type shugar and Alcohol
        bounds = [0, 100]
    elif type == "alcohol":
        if row == 0:  # Density type alcohol
            bounds = [789.3, 998.2]
        elif row == 3:  # g/100ml type alcohol
            bounds = [0, 78.91]
        else:
            raise ValueError("invalid expected type")
    elif type == "shugar":
        if row == 0:  # Density type shugar
            bounds = [1, 1.6]
        elif row == 3:  # g/100ml type shugar
            bounds = [0, 160]
        else:
            raise ValueError("invalid expected type")
    else:
        raise ValueError("invalid expected type")

    if not (bounds[0] <= san <= bounds[1]):
        print("The provided value is either to high or to low to be plausible")
        return

    return san
