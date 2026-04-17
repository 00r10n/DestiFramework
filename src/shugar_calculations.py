dens_shugar = 1.6
dens_water = 1


def shugars(inType, outType, value):
    if inType == outType:
        return "you serious?"
    if inType == 2:
        if outType == 0:
            return masToDens(value)
        if outType == 3:
            return masToPer100(value)


def masToDens(mas):
    dens = 100 / (mas / dens_shugar + (100 - mas) / dens_water)
    return dens


def masToPer100(mas):
    per100 = mas / (mas / dens_shugar + (100 - mas) / dens_water) * 100
    return per100
