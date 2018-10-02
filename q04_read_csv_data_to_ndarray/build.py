
import csv
import numpy as np
import matplotlib.pyplot as plt

def read_csv_data_to_ndarray(path, dtype):
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        # transform data into numpy array
        data = np.genfromtxt(path,dtype, delimiter=',', skip_header=1)
        return data
        

read_csv_data_to_ndarray('data/ipl_matches_small.csv',float)



