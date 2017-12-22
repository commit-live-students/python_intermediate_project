# Default imports
import numpy as np
import pandas as pd
from numpy import genfromtxt
def read_ipl_data_csv():
    path = "./data/ipl_matches_small.csv"
    ipl_matches_array = genfromtxt(path, delimiter=',',dtype = '|S50')
    return ipl_matches_array
