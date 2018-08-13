# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'


def read_csv_data_to_ndarray (strpath,sType=np.float64):
    filedata = np.genfromtxt(strpath,delimiter=',',skip_header=1,dtype=sType)
    #filedata3=np.array(filedata)
    
    #print type(filedata3)
    #print filedata
    return filedata

print read_csv_data_to_ndarray(path,'|S20')
                               
                               
                               

