import numpy as np
import pytest

from src.interpolation import interp

arr = np.array([[1, 2, 3, 4], [2, 4, 6, 8]])


@pytest.mark.parametrize(
    "arr, inrow, outrow, value, expected",
    [(arr, 0, 1, 2, 4), (arr, 0, 1, 1.5, 3), (arr, 0, 1, 3.4, 6.8)],
)
def test_value_exists(arr, inrow, outrow, value, expected):
    assert interp(arr, inrow, outrow, value) == expected
