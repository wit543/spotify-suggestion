from sklearn.cluster import KMeans
from sklearn.externals import joblib
kmean = joblib.load('kmeans.pkl')

answer = kmean.predict([2.,0.10918199,0.5092431 ,1., 1.,2.,0.515,   -10.324     ,1111.        ,    0.906     ,  150.575     ,    1.        ,    0.417     ])

print(answer)
