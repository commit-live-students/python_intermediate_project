
# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
import csv

def get_total_extras():
    ipl = []
    with open('data/ipl_matches_small.csv') as csvfile:
         reader = csv.reader(csvfile)
         for x in reader:
             ipl.append(x)
    
    #inning = [x[10] for x in ipl[1:]]
    extras =  [int(x[17]) for x in ipl[1:]]
    ext=[]
    #print(extras)
    #for x,y in zip(inning,extras):
    #    if len(y)!=0:
    #        ext.append(int(y))
            
    #extras = sum(ext)
    
    extras = sum(extras)
    #print (extras)
    return extras

#get_total_extras()



