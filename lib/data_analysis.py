import matplotlib.pyplot as plt
from collections import defaultdict

def stale_val( data ):
    stale_data = []
    for i in range( len(data)-1 ):
        if ( data[i][1] == data[i+1][1]):
            stale_data.append( [ data[i][0], data[i][1], "STALE" ] )
    return stale_data

def graph_diff( original, results ):
    correct = []
    flat_list = [item for sublist in results for item in sublist]
    for elem in flat_list: 
        correct.append( elem[1] )
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Original vs Clean')
    ax1.plot(original)
    ax2.plot(correct)
    plt.show() 

def remove_singleton( clusters, graph=False ):
    k = 3
    track_outliers = defaultdict(list) # COUNTER
    
    original = []
    outliers = []
    for i in range( len(clusters) ):
        key = clusters[i][2]
        value = clusters[i]
        track_outliers[ key ].append( value )
        original.append( clusters[i][1] )

    results = []
    for elem in track_outliers:
        size =  len( track_outliers[elem] )
        if size > k:
            results.append( track_outliers[elem] )
        if size < k:
            for item in track_outliers[elem]:
                outliers.append( [ [item[0], item[1], "OUTLIER"] ] )
    if graph:
        graph_diff( original, results )
    return [item for sublist in outliers for item in sublist]

def outlier_val( data ):
    size = len(data)
    clusterCount = 0
    cluster = []
    error =  0.05

    initial_value = [ data[0][0], data[0][1], clusterCount ]
    cluster.append( initial_value )

    for i in range(0,size):
        prev = data[i-1][1]
        prevPlusTen = abs(prev) + ( error * abs(prev) )
        prevMinusTen = abs(prev) - ( error * abs(prev) )        

        if abs( data[i][1] ) > prevPlusTen or abs( data[i][1] ) < prevMinusTen :
            clusterCount  = clusterCount + 1
            cluster_value = [ data[i][0], data[i][1], clusterCount]
            cluster.append( cluster_value )
        else:
            cluster_value = [ data[i][0], data[i][1], clusterCount]
            cluster.append( cluster_value )
    return cluster