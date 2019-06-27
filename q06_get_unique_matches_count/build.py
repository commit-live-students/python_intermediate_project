# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
#path = 'data/ipl_matches_small.csv'
import csv

# Enter Code Here
def get_unique_matches_count():
    ipl = []
    with open('data/ipl_matches_small.csv') as csvfile:
         reader = csv.reader(csvfile)
         for x in reader:
             ipl.append(x)
    match_code = list(set(x[0] for x in ipl[1:]))
    ipl_matches_array = len(match_code)
    return ipl_matches_array



