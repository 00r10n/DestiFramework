import numpy as np
import pytest

from src.shugar_calculations import masToDens, masToPer100


@pytest.mark.parametrize("mas, dens", [(100, 1.6), (0, 1), (50, 1.2307692308)])
def testMasDens(mas, dens):
    np.testing.assert_allclose(masToDens(mas), dens)


@pytest.mark.parametrize(
    "mas, per100", [(72.72727272727272, 100), (0, 0), (50, 61.5384615385)]
)
def testMasPer100(mas, per100):
    np.testing.assert_allclose(masToPer100(mas), per100)
