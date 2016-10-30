import networkx as nx

G = nx.read_adjlist("../../fullgraphs/fullgraph.adjlist")

print "Computing clustering"
bc = nx.clustering( G )

print "Writing to file "
with open('../../results/clustering_coefficient.csv', 'w') as f:
    [f.write('{0},{1}\n'.format(key, value)) for key, value in bc.items()]
