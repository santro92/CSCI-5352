import networkx as nx
import csv

G = nx.read_adjlist("../../fullgraphs/fullgraph.adjlist",  create_using=nx.DiGraph())

print "Calculating page rank"
pr = nx.pagerank_scipy(G)

print "Writing to file "
f = open( "../../results/page_rank.csv", 'wt' )
writer = csv.writer(f)
writer.writerow( ("node_id", "page_rank") )
for key in pr.keys():
    writer.writerow( ( key, pr[key] ) )
f.close()
