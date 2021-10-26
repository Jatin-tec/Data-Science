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

tip_arr = Arr2D[:, 12]

bool_tip = tip_arr >0

tip_money = tip_arr[bool_tip] #This will only add those values to array tip_money which are true in bool tip i.e. values which are greater than 0 in tip arr

copy_array = Arr2D.copy()

replace = copy_array[:, 5] 
print(copy_array)