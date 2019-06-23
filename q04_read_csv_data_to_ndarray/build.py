import numpy as np


def array_zeros():
    zeros_array = np.array([3,4,2])
    return np.zeros(zeros_array) 

def array_reshaped_zeros():
	zeros_array_reshaped = ar_zeros.reshape([2,3,4])
	return zeros_array_reshaped 

def read_csv_data_to_ndarray(p_path, p_dtype):
	ndarray = np.genfromtxt(p_path, dtype=p_dtype, skip_header=1, delimiter=',')
	return ndarray
	

ar_zeros = array_zeros()
#print(ar_zeros)
ar_zeros_reshaped = array_reshaped_zeros()
#print ('zeros_array_reshaped  : ',ar_zeros_reshaped )

ndarray_ipl_csv = read_csv_data_to_ndarray('data/ipl_matches_small.csv',np.float64)
ndarray_ipl_csv.size


