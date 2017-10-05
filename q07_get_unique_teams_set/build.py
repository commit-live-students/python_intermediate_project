# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    ipl_matches_array=read_ipl_data_csv(path,'|S50')
    matchset=ipl_matches_array[:,3:5]
    lst=[]


    setmatchfinal=set(matchset.flat)
    return setmatchfinal

#m=get_unique_teams_set()
#print(type(m))
#print(m)
#li={1,2,3,4}
#print(li)
#print(type(li))
