import csv
import numpy as np

def read_ipl_data_csv():
    ipl_matches_arrays = (','.join(i) for i in csv.reader(open('data/ipl_matches_small.csv','r')))   # ipl_matches_array=np.genfromtxt('/Users/saravanan/Documents/GIT/GreayAtom-Assignment/sara_Sheet1.csv',
    arrays=[]
    for row in ipl_matches_arrays:
        list1=row.split(',');
        arrays.append(list1)
        
    arrays=np.array(arrays)[1:]
    return arrays

def get_total_extras() :
    matchInfo=read_ipl_data_csv()
    extrasList=[int(s) for s in matchInfo[:,17:18]]
   # print ([int(s) for s in matchInfo[:,18:19]])
   # print(extrasList)
    extras=np.sum(extrasList)
    return extras
   # print(get_total_extras())

    
     








