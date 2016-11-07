import networkx as nx

G = nx.read_adjlist("../../fullgraphs/fullgraph.adjlist")

print "Computing average neighbour degree"
nd = nx.average_neighbor_degree( G )

print "Writing to file "
with open('../../results/average_neighbour_degree.csv', 'w') as f:
    [f.write('{0},{1}\n'.format(key, value)) for key, value in nd.items()]