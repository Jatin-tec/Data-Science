import csv
import numpy as np

f = open('nyc_taxi.csv', 'r')

taxi_list = list(csv.reader(f))
taxi_list = taxi_list[1:]


converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

Arr2D = np.array(converted_taxi_list)

pickup_month = Arr2D[:, 1]

jan_bool = pickup_month == 1

jan = pickup_month[jan_bool]

# jan_rides = jan.shape[0]

print(pickup_month)
print(jan_bool)
print(jan)