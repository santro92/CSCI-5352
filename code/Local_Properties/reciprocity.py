import networkx as nx
from collections import defaultdict
import csv

def reciprocity(G):
    recip = defaultdict(float)
    for node in G.nodes():
        pred = set(G.predecessors(node))
        succ = set(G.successors(node))
        overlap = pred & succ
        n_total = len(pred) + len(succ)

        # Reciprocity is not defined for isolated nodes.
        # Return None.
        if n_total == 0:
            recip[node] = -1
        else:
            reciprocity = 2.0*float(len(overlap))/float(n_total)
            recip[node] = reciprocity
    return recip

G = nx.read_adjlist("../../fullgraphs/fullgraph.adjlist",  create_using=nx.DiGraph())

print "Calculating Reciprocity"
recip = reciprocity(G)

print "Writing to file "
f = open( "../../results/reciprocity.csv", 'wt' )
writer = csv.writer(f)
writer.writerow( ("node_id", "reciprocity") )
for key in in_deg.keys():
    writer.writerow( ( key, recip[key] ) )
f.close()
