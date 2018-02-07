# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray (path,dtype):
    dt=dtype

    arr=np.genfromtxt(path,delimiter=',',dtype=dt,skip_header=1)
    #arr= np.recfromcsv(path)
    #print arr
    return arr
#read_csv_data_to_ndarray(path,'|S50')
