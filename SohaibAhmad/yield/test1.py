import pandas as pd 
import datetime as dt 
import pandas_datareader as web 

open_file = read_csv("standard_csv_file.csv")
row_counter = 0

for row in open_file:
    row_count += 1

print("Row count is {}".format(row_count))

def read_csv(file_name):

    for row in open(file_name, "r"):
        yield row

import numpy as  np

