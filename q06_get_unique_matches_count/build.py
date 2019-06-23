import numpy as np


def array_zeros():
    zeros_array = np.array([3,4,2])
    return np.zeros(zeros_array) 

def array_reshaped_zeros():
	zeros_array_reshaped = ar_zeros.reshape([2,3,4])
	return zeros_array_reshaped 

def read_csv_data_to_ndarray(p_path,p_dtype):
	ndarray = np.genfromtxt(p_path, dtype=p_dtype, skip_header=1, delimiter=',')
	return ndarray
	
def read_ipl_data_csv(path,dtype):
	ar_ndarray = np.genfromtxt(path, dtype=dtype, skip_header=1, delimiter=',')
	return ar_ndarray

def get_unique_matches_count():
	#to get multiple columns 
	#print ('Specific columns : ',ipl_array[:,[2,3,4]])
	ipl_matches_array = read_ipl_data_csv('data/ipl_matches_small.csv','|S50')
	ipl_matches_array = np.unique(ipl_matches_array[1:,1])
	#.astype(np.float16)
	print('ipl_matches_array : ',len(ipl_matches_array))
	return len(ipl_matches_array)

ar_zeros = array_zeros()
#print(ar_zeros)
ar_zeros_reshaped = array_reshaped_zeros()
#print ('zeros_array_reshaped  : ',ar_zeros_reshaped )

ipl_csv = read_csv_data_to_ndarray('data/ipl_matches_small.csv',np.float64)
ipl_matches_array = read_ipl_data_csv('data/ipl_matches_small.csv','|S50')
print('ipl_matches_array : ', ipl_matches_array.size)
int_total_matches_played = get_unique_matches_count()
print ('int_total_matches_played : ', int_total_matches_played)


