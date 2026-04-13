import pandas as pd


# import numpy as np
def readT6(path):
    df = pd.read_excel(path, engine="odf")
    return df.to_numpy()
