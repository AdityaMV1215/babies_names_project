
import pandas as pd
import numpy as np
from collections import defaultdict
path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

def q03_top_in_each_year_1(data):
    "write your solution here"
    dict3 = defaultdict(dict)
    unique_years = np.unique(data['Year'])
    for val in unique_years:
        temp = data[data['Year'] == val]
        for x in temp.index.values:
            dict3[val][temp.loc[x,'Name']] = temp.loc[x,'Count']
    return dict3

q03_top_in_each_year_1(data)
