# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    temp = set()
    df = read_ipl_data_csv(path,'|S50')
    for item in df:
        temp.add(item[3])
        temp.add(item[4])
    return temp
