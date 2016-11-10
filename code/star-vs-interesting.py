import pandas
import os
import json

start = 2
stop = 3

source_folder = "../subgraphs/"
destination_folder = "../subgraphs/stargraphs/"

for i in range( start, stop):
    source_file = source_folder + str(i) + "-subgraph.adjlist"
    destination_file = destination_folder + str(i) + "-subgraph.adjlist"
    clustering_file = '../clustering/' + str(i) + '-cc.json'
    print clustering_file
    subdict = json.loads( clustering_file )
    print subdict
    
os.rename( source_folder, destination_folder)
