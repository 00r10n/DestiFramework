import numpy as np
import pytest

from src.readData import readTable


def test_T6_import():
    path = "./tables_raw/t6_nell.ods"
    t6 = readTable(path)
    np.testing.assert_allclose([789.3, 99.99, 99.98, 78.914214], t6[-1, :])
