
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv

def get_unique_matches_count ():
    unique_list = [] 
    mylist = read_ipl_data_csv('data/ipl_matches_small.csv', '|S50')
    #unique_list =set(x for unique_list in mylist[0] for x in unique_list)
    unique_list=set(mylist[:, 0])
    print (unique_list)
    ipl_matches_array = len(unique_list)
    return ipl_matches_array
    
get_unique_matches_count()



