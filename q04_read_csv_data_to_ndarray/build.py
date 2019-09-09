# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path,dtype):

    data = np.loadtxt( path , dtype = dtype , delimiter=',' , skiprows=1 )#, names = False)
    return data

#genfromtxt

#print read_csv_data_to_ndarray("data/ipl_matches_small.csv",float)
