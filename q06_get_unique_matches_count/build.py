import numpy as np
import csv
def get_unique_matches_count() :
    ipl_matches_arrays = (','.join(i) for i in csv.reader(open('data/ipl_matches_small.csv','r')))   # ipl_matches_array=np.genfromtxt('/Users/saravanan/Documents/GIT/GreayAtom-Assignment/sara_Sheet1.csv',
    arrays=[]
    for row in ipl_matches_arrays:
        list1=row.split(',');
        #del list1[0]
        #del list1[0]
        #del list1[10]
        #print(list1)
        arrays.append(list1)
    
    #clean= np.genfromtxt(arrays,invalid_raise=False,dtype=None,delimiter='\,')

    arrays=np.array(arrays)[1:]
    #print(np.unique(arrays[:,16:17],axis=0))
    ipl_matches_array=len(np.unique(arrays[:,1:2],axis=0))
    return ipl_matches_array



