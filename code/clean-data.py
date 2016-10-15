"""
Module to reduce size of edges file
"""
import csv
import networkx as nx
import pandas as pd

cleanDataDict = { 'Intermediaries': 3, 'Entities': 18,
                    'Officers': 2, 'Addresses': 2, 'all_edges': 4 }

for key in cleanDataDict:
    with open("data/"+str(key)+".csv","rb") as source:
        rdr= csv.reader( source )
        with open("fullgraphs/"+str(key)+".csv","wb") as result:
            wtr= csv.writer( result )
            for r in rdr:
                del r[cleanDataDict[key]]
                wtr.writerow(  r )
    print "Finished cleaning " + str(key) + " data"

