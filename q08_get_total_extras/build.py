# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

#Using the newly defined function get_total_extras
# Load the data into array using the existing module read_ipl_data_csv
# Using for loop add the extra into sum and return the same (Loop through since we need to calculate for whole match)
# Since element[17] is an Int (Append/Sum) functionality was throwing error
# Also note element[17] will be an Str so need to convert into Integer before performing the summation.

def get_total_extras():
    Sum=0
    array_f2 = read_ipl_data_csv(path, "|S50")
    for element in array_f2:
        Sum += int(element[17])
    return Sum
