import networkx as nx

start = 0
end = -1
diff = -1

for i in xrange( start,  end, diff ):
    print "Loading graph"
    adjlist = str(i)+"-subgraph.adjlist"
    G = nx.read_adjlist("../subgraphs/"+adjlist)

    print "Computing betweenness centrality"
    bc = nx.betweenness_centrality( G, normalized=True )

    print "Writing to file " + str(i)
    # write dictionary to file
    import json
    with open('../centrality/'+adjlist+'-bc.json', 'w') as fp:
        json.dump( bc, fp, sort_keys=True, indent=4)

