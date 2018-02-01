# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(data):
    ipl_matches_array = np.genfromtxt(BytesIO(data))
