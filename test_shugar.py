import numpy as np
import pytest

from src.shugar_calculations import masToDens


@pytest.mark.parametrize("mas, dens", [(100, 1.6), (0, 1), (50, 1.2307692308)])
def test50(mas, dens):
    np.testing.assert_allclose(masToDens(mas), dens)
