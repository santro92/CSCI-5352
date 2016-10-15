"""
Store nodes ( keyed by ID )
in a fullgraphsbase

"""
import pandas as pd
import networkx as nx
import time

# load the raw fullgraphs into fullgraphsframes
print "Loading fullgraphs"
t = time.time()

adds = pd.read_csv("fullgraphs/Addresses.csv", low_memory=False)

ents = pd.read_csv("fullgraphs/Entities.csv", low_memory=False)

inter = pd.read_csv("fullgraphs/Intermediaries.csv", low_memory=False)

offi = pd.read_csv("fullgraphs/Officers.csv", low_memory=False)

print "Done loading fullgraphs, took time t = " + str( time.time() - t)

# add fullgraphs into dictionary
nodesDict = {}
print "Adding to dictionary"
t = time.time()

for n,row in adds.iterrows():
    nodesDict[row.node_id] = {'node_type': "address" }

for n,row in ents.iterrows():
    nodesDict[row.node_id] = {'node_type': "entitities"}
    
for n,row in inter.iterrows():
    nodesDict[row.node_id] = {'node_type': "intermediates"}
    
for n,row in offi.iterrows():
    nodesDict[row.node_id] = {'node_type': "officers"}

print "Done writing to dictionary, took time t = " + str( time.time() - t )

# write dictionary to file
import json
with open('fullgraphs/all_nodes_type.json', 'w') as fp:
    json.dump( nodesDict, fp, sort_keys=True, indent=4)
