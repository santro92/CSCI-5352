import networkx as nx
import csv

G = nx.read_adjlist("../../fullgraphs/fullgraph.adjlist",  create_using=nx.DiGraph())

print "Calculating Katz Centrality"
katz = nx.katz_centrality(G, max_iter=500)

print "Writing to file "
f = open( "../../results/katz.csv", 'wt' )
writer = csv.writer(f)
writer.writerow( ("node_id", "katz") )
for key in in_deg.keys():
    writer.writerow( ( key, katz[key] ) )
f.close()
