import numpy as np
from io import BytesIO
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():
    ipl_matches_array =np.genfromtxt(BytesIO(path), dtype="|S50", skip_header=1, delimiter=",")
print ipl_matches_array
