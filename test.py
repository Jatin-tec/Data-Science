import pandas as pd
import csv
import re

# f = open('regular.csv', 'r')

# hacker_News = list(csv.reader(f))
# hacker_News  = taxi_list[1:2]

string = "The rain in Spain"

x = re.findall("[a-z]", string)
x = re.split("\s", string, 1)
x = re.split("\s", string)
x = re.sub("\s","9", string, 2)

print(x)