import pandas as pd

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

def q01_create_dict(data):
    dict1 = {}
    for x in data.index.values:
        dict1[data.loc[x,'Name']] = data.loc[x,'Count']

    return dict1
