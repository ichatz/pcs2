import urllib.request
url = 'http://aima.cs.berkeley.edu/data/iris.csv'
u = urllib.request.urlopen(url)
rawdata = u.read()

localFile = open("iris.csv", "wb")
localFile.write(rawdata)
localFile.close()

import csv
f = open("iris.csv")
rawdata = []
for row in csv.reader(f, delimiter=','):
    rawdata.append(row)

for row in rawdata:
    for value in range(0, len(row)-1):
        row[value] = float(row[value])

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, init='random')
kmeans.fit([v[2:3] for v in rawdata])
c = kmeans.predict([v[2:3] for v in rawdata])

