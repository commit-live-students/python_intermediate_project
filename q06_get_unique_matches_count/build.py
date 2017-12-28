# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
dtype='|S50'
data=read_ipl_data_csv(path,dtype)
count=[]
def get_unique_matches_count():
    for i in data:
        count.append(i[0])
    return len(set(count))
# Enter Code Here
