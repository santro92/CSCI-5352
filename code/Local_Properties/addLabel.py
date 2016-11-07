import json
import pandas as pd

with open('../../fullgraphs/all_nodes_type.json') as data_file:
    data = json.load(data_file)

print "Done loading Json"

df = pd.read_csv('../../results/ensemble.csv',index_col=None, header=0)

lst = df['id']
labels = []

print "started reading"
for i in range(len(lst)):
    labels.append(data[str(lst[i])]['node_type'])
print "completed"

se = pd.Series(labels)
df['label'] = se.values

df.to_csv('../../ensemble.csv', separator=',', index=False)

print "Done"
