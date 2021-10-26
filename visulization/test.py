import numpy as np
import pandas as pd

data = {
    'month':[14, 18, 14, 42],
    'heights':[121, 234, 121, 132]
}

df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])
# print(df['month'].value_counts())
print(df.groupby('month')['heights'])
# df = pd.DataFrame(data)
# df.set_index('ages', inplace=True) #sets index
# print(df)
