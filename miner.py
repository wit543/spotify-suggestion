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
        temp = np.nan_to_num(temp)
        array.append(temp)
        # if count%100 ==0:
            # print(array[count-100:count-1])
            # kmean.fit(array[count-100:count-1])
        h5.close()
    return array
# print(get_all_files_path("C:\\Users\\wit54\MillionSongSubset"))

data = get_attribute(get_all_files_path("E:\data\million song data set"))
joblib.dump(data, 'data.pkl')
kmeans = KMeans(init='k-means++', n_clusters=50).fit(data)
print("finish reading data!!!!")

joblib.dump(kmeans, 'kmeans.pkl')
