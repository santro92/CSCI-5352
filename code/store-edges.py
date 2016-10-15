"""
Module to reduce size of edges file
"""
import csv
import networkx as nx
import pandas as pd

edges = pd.read_csv("fullgraphs/all_edges.csv", low_memory=False)

G = nx.DiGraph()

for n,row in edges.iterrows():
    G.add_edge(row.node_1, row.node_2, rel_type=row.rel_type, details={})

nx.write_adjlist(G,"fullgraphs/fullgraph.adjlist")
