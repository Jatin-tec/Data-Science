import numpy as np
import csv

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
taxi_shape = Arr2D.shape

row_0 = Arr2D[0]

row_391_to_500 = Arr2D[391:501] 
# print(Arr2D)
col = Arr2D[:, 2]
temp=Arr2D[2 : 4]

sel_np = Arr2D[2, 1:3]

col1=Arr2D[:,0]
col2=Arr2D[:,1]

Sum = col1+col2
print(Arr2D)

