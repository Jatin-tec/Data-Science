import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style

plt.style.use('ggplot')

f = pd.read_csv('WHO-COVID-19-global-data.csv')

df = pd.DataFrame(f)

afghanistan = df[df['Country']=='Afghanistan']
death_afghanistan = afghanistan['Cumulative_deaths']
cases_afghanistan = afghanistan['Cumulative_cases']


plt.title('New Reported Deaths Vs Cases (Afghanistan)')
plt.plot(death_afghanistan, cases_afghanistan)
plt.xlabel("Death Afghanistan") #labeling x axis
plt.ylabel("Cases Afghanistan") #labeling y axis
plt.show()

# data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])

# Mean = np.mean(data)

# square_diff = (data-Mean)**2
# square_diff_mean = np.mean(square_diff)
# square_diff_mean = square_diff_mean**(1/2)
# print(square_diff_mean)

# daviated_data = data>square_diff_mean
# daviated_data = data[daviated_data]
# percentage = len(daviated_data)/len(data)
# percentage= percentage*100
# print(percentage)