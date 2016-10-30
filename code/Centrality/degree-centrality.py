import networkx as nx

for i in [0]:#xrange( 10426, 0, -1 ):
    print "Loading graph"
    adjlist = str(i)+"-subgraph.adjlist"
    G = nx.read_adjlist("../subgraphs/"+adjlist)

    print "Computing degree centrality"
    dc = nx.degree_centrality( G )

    print "Writing to file"
    # write dictionary to file
    import json
    with open('../centrality/'+adjlist+'-dc.json', 'w') as fp:
        json.dump( dc, fp, sort_keys=True, indent=4)

