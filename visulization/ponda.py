import pandas as pd

who_time_series = pd.read_csv('WHO-COVID-19-global-data.csv')
# print(who_time_series.head())
# print(who_time_series['Country'], ['New_deaths'])
print(who_time_series.loc[:, 'Country'])