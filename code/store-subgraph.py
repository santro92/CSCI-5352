import networkx as nx

print "Creating graph"
G = nx.DiGraph()
G = nx.read_adjlist("../fullgraphs/fullgraph.adjlist")

print "Finding Subgraphs"
subgraphs = [g for g in nx.connected_component_subgraphs(G.to_undirected())]
subgraphs = sorted(subgraphs, key=lambda x: x.number_of_nodes(), reverse=True)

print "Storing subgraphs for faster access times"
count = 0
for subg in subgraphs:
    nx.write_adjlist( subg ,"../subgraphs/"+str(count)+"-subgraph.adjlist")
    count+= 1

print([s.number_of_nodes() for s in subgraphs[:10]])

