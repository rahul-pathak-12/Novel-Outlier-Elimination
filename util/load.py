import pandas as pd 

def load_csv( path ):
    raw_file = pd.read_csv( path )
    dates = raw_file[raw_file.columns[0]]
    data = raw_file[raw_file.columns[1]]
    return list( zip(dates, data) )