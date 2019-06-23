import numpy as np

str_path='data/ipl_matches_small.csv'

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
	#print ('Specific columns : ',ipl_array[:,[2,3,4]])
	ipl_matches_array = read_ipl_data_csv(str_path,'|S50')
	ipl_matches_array = np.unique(ipl_matches_array[1:,1])
	return len(ipl_matches_array)

def get_unique_teams_set():
    ipl_unique_teams_array = read_ipl_data_csv(str_path,'|S50')
    ipl_team1 = np.unique(ipl_unique_teams_array[:,3])
    ipl_team2 = np.unique(ipl_unique_teams_array[:,4])
    unique_teams=set(np.concatenate((ipl_team1,ipl_team2), axis=0))
    return unique_teams
	
	
ar_zeros = array_zeros()
ar_zeros_reshaped = array_reshaped_zeros()
ipl_csv = read_csv_data_to_ndarray(str_path,np.float64)
ipl_matches_array = read_ipl_data_csv(str_path,'|S50')
int_total_matches_played = get_unique_matches_count()
ipl_unique_teams = get_unique_teams_set()




