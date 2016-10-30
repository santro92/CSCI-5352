import networkx as nx
import csv

G = nx.read_adjlist("../../fullgraphs/fullgraph.adjlist",  create_using=nx.DiGraph())

print "Calculating Out Degree"
out_deg = G.out_degree()

print "Writing to file "
f = open( "../../results/out_degree.csv", 'wt' )
writer = csv.writer(f)
writer.writerow( ("node_id", "out_degree") )
for key in in_deg.keys():
    writer.writerow( ( key, out_deg[key] ) )
f.close()
