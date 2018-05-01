
import numpy as np
def read_ipl_data_csv(path):
    read_ipl = np.genfromtxt(path , dtype='|S50', skip_header=1, delimiter=',')
    return read_ipl
def get_unique_teams_set():
    var = read_ipl_data_csv('data/ipl_matches_small.csv')
    var1 = np.unique(var[:,3])
    var2 = np.unique(var[:,4])
    return set(var1) | set(var2)
get_unique_teams_set()



