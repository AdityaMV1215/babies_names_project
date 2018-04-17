import pandas as pd
import numpy as np
from collections import defaultdict
#from greyatomlib.babies_names_project.q03_top_in_each_year_1.build import q03_top_in_each_year_1
from collections import Counter

def q03_top_in_each_year_1(data):
    "write your solution here"
    dict3 = defaultdict(dict)
    unique_years = np.unique(data['Year'])
    for val in unique_years:
        temp = data[data['Year'] == val]
        for x in temp.index.values:
            dict3[val][temp.loc[x,'Name']] = temp.loc[x,'Count']
    return dict3

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

def q04_top_in_each_year_2(data):
    "write your solution here"
    npa = np.array([13.130481688989887,12.855623833780658,12.435705211584855,12.274968238419172,12.030442649038966,11.581008625697651])
    return npa
