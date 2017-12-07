import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():
	match_codes1 = read_ipl_data_csv(path,dtype=np.int32)
	match_codes = match_codes1[...,0]
	ipl_matches_array=len(np.unique(match_codes))
	return ipl_matches_array
