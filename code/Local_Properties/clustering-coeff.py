import networkx as nx

start = 0
end = -1
diff = -1

for i in xrange( start,  end, diff ):
    print "Loading graph"
    adjlist = str(i)+"-subgraph.adjlist"
    G = nx.read_adjlist("../subgraphs/"+adjlist)

    print "Computing clustering"
    bc = nx.clustering( G )

    print "Writing to file " + str(i)
    # write dictionary to file
    import json
    with open('../clustering/'+adjlist+'-cc.json', 'w') as fp:
        json.dump( bc, fp, sort_keys=True, indent=4)
