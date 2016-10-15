import networkx as nx

for i in xrange( 10426, 0, -1 ):
    print "Loading graph"
    adjlist = str(i)+"-subgraph.adjlist"
    G = nx.read_adjlist("../subgraphs/"+adjlist)

    print "Computing harmonic centrality"
    hc = nx.harmonic_centrality( G )

    print "Writing to file"
    # write dictionary to file
    import json
    with open('../centrality/'+adjlist+'-hc.json', 'w') as fp:
        json.dump( hc, fp, sort_keys=True, indent=4)

