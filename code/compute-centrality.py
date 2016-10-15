import networkx as nx

for i in range( 10427 ):
    print "Loading graph"
    adjlist = str(i)+"-subgraph.adjlist"
    G = nx.read_adjlist("subgraphs/"+adjlist)

    print "Computing betweenness centrality"
    bc = nx.betweenness_centrality( G, normalized=True )

    print "Writing to file"
    # write dictionary to file
    import json
    with open('centrality/'+adjlist+'-bc.json', 'w') as fp:
        json.dump( bc, fp, sort_keys=True, indent=4)

