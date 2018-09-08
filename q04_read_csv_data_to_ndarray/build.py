# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
import csv
path = './data/ipl_matches_small.csv'



def read_csv_data_to_ndarray(path,datatype=np.float64):
    data = np.genfromtxt(path, dtype=datatype,delimiter=',', skip_header=1)
    return data
read_csv_data_to_ndarray('./data/ipl_matches_small.csv')
import numpy as np
import csv
data_path = './data/ipl_matches_small.csv'
with open(data_path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    # get header from first row
    headers = next(reader)
    # get all the rows as a list
    data = list(reader)
    # transform data into numpy array
    data = np.array(data).astype(str)
type(data)
import csv
data_path = './data/ipl_matches_small.csv'
data = np.genfromtxt(data_path, delimiter=',', skip_header=1,dtype=np.float64)
data
type(data)


