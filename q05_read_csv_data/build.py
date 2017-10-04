# Default imports
import numpy as np
import csv
path = "./data/ipl_matches_small.csv"


def read_csv_data_to_ndarray(path,dtype=np.float64):

    with open(path,'r') as line:
        read_line = csv.reader(line)
        c=0
        array = np.array([1])
        for element in read_line:
            if c ==0:
                c=1
                pass
            else:
                #print(element)
                array = np.append(array,element)
    return array[1:]
# Enter code here
