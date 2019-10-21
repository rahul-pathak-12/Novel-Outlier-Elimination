from util.load import load_csv
from lib.data_analysis import stale_val, outlier_val,  remove_singleton
from pprint import pprint as pp
from datetime import datetime

def check_file_data( file_path ):
    data = load_csv( x )

    clusters = outlier_val( data )
    outliers = remove_singleton( clusters, graph=True )
    
    outliers.sort(key=lambda date: datetime.strptime(date[0], "%d/%m/%Y"))
    return outliers

x = "resources\\raw_series_3.csv"
results = check_file_data( x )
pp( results )
pp( len(results) )