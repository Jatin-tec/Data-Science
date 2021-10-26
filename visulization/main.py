import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

f = open('WHO-COVID-19-global-data.csv', 'r', encoding='utf8')

covid_list = list(csv.reader(f))
cases=covid_list[1:364]

cases = np.array(cases)
# present_cases = cases[:,4]
deaths = cases[:,6]
dates = cases[:,0]

month = []
for date in dates:
    month.append(date[5:7])
# print(month)

# converted_present_cases=[]
# for i in present_cases:
#     converted_present_cases.append(int(i))

converted_deaths=[]
for i in deaths:
    converted_deaths.append(int(i))

month_list = ['01', '02', '03', '04', '05', '06', '07', '08']
for i in month_list:
    jan_deaths=[death for death in deaths if i=="01"]
    feb_deaths=[death for death in deaths if i=="02"]
    march_deaths=[death for death in deaths if i=="03"]
    apr_deaths=[death for death in deaths if i=="04"]
    may_deaths=[death for death in deaths if i=="05"]
    jun_deaths=[death for death in deaths if i=="06"]
    jul_deaths=[death for death in deaths if i=="07"]
    aug_deaths=[death for death in deaths if i=="08"]
    
Updated_deaths = [sum(jan_deaths), sum(feb_deaths), sum(march_deaths), sum(apr_deaths), sum(may_deaths), sum(jun_deaths), sum(jul_deaths), sum(aug_deaths)]
print(Updated_deaths)
month=[1, 2, 3, 4, 5, 6, 7, 8]

plt.title('New Reported Deaths By Month (Globally)')
plt.plot(month, Updated_deaths)
plt.xlabel("month") #labeling x axis
plt.ylabel("covid deaths") #labeling y axis
plt.show()