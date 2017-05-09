import hdf5_getters
# import scikits.ann as ann
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn import preprocessing
from sklearn.preprocessing import Imputer
import numpy as np
import os
import glob
def count_all_files(basedir,ext='.h5') :
    cnt = 0
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        cnt += len(files)
    return cnt
def get_all_files_path(basedir,ext='.h5') :
    file_temp = []
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            file_temp.append(f)
    return file_temp
def get_all_titles(basedir,ext='.h5') :
    titles = []
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            h5 = hdf5_getters.open_h5_file_read(f)
            titles.append( hdf5_getters.get_title(h5) )
            h5.close()
    return titles

def get_attribute(files):
    array = []
    count =0
    for f in files:
        temp =[]
        count+=1
        print(f)
        h5 = hdf5_getters.open_h5_file_read(f)
        temp.append(hdf5_getters.get_num_songs(h5))
        temp.append(hdf5_getters.get_artist_familiarity(h5))
        temp.append(hdf5_getters.get_artist_hotttnesss(h5))
        temp.append(hdf5_getters.get_danceability(h5))
        temp.append(hdf5_getters.get_energy(h5))
        temp.append(hdf5_getters.get_key(h5))
        temp.append(hdf5_getters.get_key_confidence(h5))
        temp.append(hdf5_getters.get_loudness(h5))
        temp.append(hdf5_getters.get_mode(h5))
        temp.append(hdf5_getters.get_mode_confidence(h5))
        temp.append(hdf5_getters.get_tempo(h5))
        temp.append(hdf5_getters.get_time_signature(h5))
        temp.append(hdf5_getters.get_time_signature_confidence(h5))
        temp.append(hdf5_getters.get_title(h5))
        temp.append(hdf5_getters.get_artist_name(h5))
        temp = np.nan_to_num(temp)
        array.append(temp)
        # if count%100 ==0:
            # print(array[count-100:count-1])
            # kmean.fit(array[count-100:count-1])
        h5.close()
    return array
# print(get_all_files_path("C:\\Users\\wit54\MillionSongSubset"))
def compute_data(text):
    label = ""
    data = get_attribute(get_all_files_path(text+label))
    # data =joblib.load("C:\\Users\\wit54\\spotify-suggestion\\data.pkl")
    joblib.dump(data, "data"+label+".pkl")
    array =[]
    for i in data:
        array.append(i[:13])
    array = np.array(array,dtype=np.float32)
    array = np.nan_to_num(array)
    kmeans = KMeans(init='k-means++', n_clusters=5000).fit(array)
    return kmeans
def loadData(text):
    return joblib.load("kmeans.pkl")
kmeans = compute_data("C:\\Users\\wit54\\MillionSongSubset\\data")
data = joblib.load("C:\\Users\\wit54\\spotify-suggestion\\data.pkl")

# data = np.array(data )
# print(data.shape)
array =[]
label_map = []
mapped = {}
for i in range(5000):
    mapped[i]=[]
for i in data:
    array.append(i[:13])
    label_map.append([i[13],i[14]])

print(np.array(array,dtype= np.float64))
for i in range(len(kmeans.labels_)):
    mapped[kmeans.labels_[i]].append(label_map[i])
dataaaa =get_attribute(["C:\\Users\\wit54\\MillionSongSubset\\data\\A\\A\\A\\TRAAAAW128F429D538.h5"])[0][:13]
print(dataaaa)
print(mapped[kmeans.predict(np.array(dataaaa,dtype=np.float64))[0]])
print("finish reading data!!!!")
# joblib.dump(kmeans, 'kmeans.pkl')
