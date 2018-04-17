import pandas as pd
from collections import Counter
#from greyatomlib.babies_names_project.q01_create_dict.build import q01_create_dict

def q01_create_dict(data):
    dict1 = {}
    for x in data.index.values:
        dict1[data.loc[x,'Name']] = data.loc[x,'Count']

    return dict1

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

def q02_top_names(data):
    dict1 = q01_create_dict(data)
    dict2 = {}
    var1 = Counter(dict1).most_common(25)
    '''for i in range(0,len(var1)):
        dict2[var1[i][0]] = var1[i][1]'''
    return var1[0]

print(q02_top_names(data))
