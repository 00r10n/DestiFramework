import numpy as np
import pytest

from src.readData import readTable


def test_T6_import():
    path = "./tables_raw/t6_nell.ods"
    t6 = readTable(path)
    np.testing.assert_allclose(
        [789.3, 99.99, 99.98, 78.9], t6[0, :], rtol=1e-2, atol=1e-2
    )
