# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
from pprint import pprint
data = read_data()
#pprint(data['innings'][0]['1st innings']['deliveries'])
'''run=0
lst_of_balls=data['innings'][0]['1st innings']['deliveries']
for balls in lst_of_balls:
    value_per_ball=balls.values()
    batsman=value_per_ball[0]['batsman']
    if batsman=="BB McCullum":
        print("BB McCullum")
        run=run+value_per_ball[0]['runs']['batsman']
print(run)

'''



# Your Solution
def BC_runs(data):
    runs=0
    lst_of_balls=data['innings'][0]['1st innings']['deliveries']
    for balls in lst_of_balls:
        value_per_ball=balls.values()
        batsman=value_per_ball[0]['batsman']
        if batsman=="BB McCullum":
            #print("BB McCullum")
            runs=runs+value_per_ball[0]['runs']['batsman']
    #print(run)


    # Write your code here


    return(runs)
#run=BC_runs(data)
#print(run)
