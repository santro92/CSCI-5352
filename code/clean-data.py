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

"""
with open("data/Entities.csv","rb") as source:
    rdr= csv.reader( source )
    with open("fullgraphs/Entities.csv","wb") as result:
        wtr= csv.writer( result )
        for r in rdr:
            del r[18]
            wtr.writerow(  r )

with open("data/Officers.csv","rb") as source:
    rdr= csv.reader( source )
    with open("fullgraphs/Officers.csv","wb") as result:
        wtr= csv.writer( result )
        for r in rdr:
            del r[2]
            wtr.writerow(  r )

with open("data/Addresses.csv","rb") as source:
    rdr= csv.reader( source )
    with open("fullgraphs/Addresses.csv","wb") as result:
        wtr= csv.writer( result )
        for r in rdr:
            del r[2]
            wtr.writerow( r )

with open("data/all_edges.csv","rb") as source:
    rdr= csv.reader( source )
    with open("fullgraphs/all_edges.csv","wb") as result:
        wtr= csv.writer( result )
        for r in rdr:
            del r[4]
            wtr.writerow(  r )
"""
"""
edges = pd.read_csv("fullgraphs/all_edges.csv", low_memory=False)

G = nx.DiGraph()

for n,row in edges.iterrows():
    G.add_edge(row.node_1, row.node_2, rel_type=row.rel_type, details={})

nx.write_adjlist(G,"fullgraphs/fullgraph.adjlist")
"""
