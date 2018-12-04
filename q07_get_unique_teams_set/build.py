# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    teams = []
    for i in read_ipl_data_csv(path, dtype='|S100'):
        if not i[3] in teams:
            teams.append(i[3])
        if not i[4] in teams:
            teams.append(i[4])
    return set(teams)


