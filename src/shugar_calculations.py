dens_shugar = 1.6
dens_water = 1


def masToDens(mas):
    dens = 100 / (mas / dens_shugar + (100 - mas) / dens_water)
    return dens
