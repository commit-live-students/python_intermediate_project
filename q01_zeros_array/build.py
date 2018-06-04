
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def extras_runs(data=data):

    first_innings_deliveries = data['innings'][0]['1st innings']['deliveries']
    extras_1st_innings = [delivery_info
                          for delivery in first_innings_deliveries
                          for delivery_number, delivery_info in delivery.items()
                          if 'extras' in delivery_info]
    print(len(extras_1st_innings))

    second_innings_deliveries = data['innings'][1]['2nd innings']['deliveries']
    extras_2nd_innings = [delivery_info
                          for delivery in second_innings_deliveries
                          for delivery_number, delivery_info in delivery.items()
                          if 'extras' in delivery_info]
    print(len(extras_2nd_innings))

    difference = len(extras_2nd_innings) - len(extras_1st_innings)

    return difference


