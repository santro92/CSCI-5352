import glob
import pandas as pd

path ='../../results' # use your path
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
cnt = 1
for file_ in allFiles:
    print file_
    df = pd.read_csv(file_,index_col=None, header=0)
    if cnt != 1:
        del df['id']
    cnt += 1
    print df.head()
    list_.append(df)
frame = pd.concat(list_, axis=1)
print frame.head()
frame.to_csv("../../results/ensemble.csv", separator=',', index=False)
print "Done"
