from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

import numpy as np
def get_total_extras():
    x=read_ipl_data_csv(path,'|S50')
    return int(sum(x[:,17].astype(np.float64)))
