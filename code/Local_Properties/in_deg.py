import networkx as nx
import csv

G = nx.read_adjlist("../../fullgraphs/fullgraph.adjlist",  create_using=nx.DiGraph())

print "Calculating In Degree"
in_deg = G.in_degree()

print "Writing to file "
f = open( "../../results/in_degree.csv", 'wt' )
writer = csv.writer(f)
writer.writerow( ("node_id", "in_degree") )
for key in in_deg.keys():
    writer.writerow( ( key, in_deg[key] ) )
f.close()
