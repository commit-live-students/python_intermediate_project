# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
import numpy as np

unique_teams = read_ipl_data_csv(path, dtype = '|S50')
matches = []

def get_total_extras():
    run1 = 0
    for i in unique_teams:

        run1 = run1 + int(i[17])
    return run1

runs = get_total_extras()
