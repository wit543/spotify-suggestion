import multiprocessing
import hdf5_getters
from sklearn.externals import joblib
import os
import glob
array = []

def get_attribute(f):
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
    h5.close()
def get_all_files_path(basedir,ext='.h5') :
    file_temp = []
    for root, dirs, files in os.walk(basedir):
        print("in")
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            file_temp.append(f)
    return file_temp

if __name__ == "__main__":
    p = multiprocessing.Pool()

    files = get_all_files_path("E:\data\million song data set")
    joblib.dump(files,"files.pkl")
    print("done")
    for f in files:
        p.apply_async(get_attribute, [f])
    print("donnnnnneeee")
    p.close()
    p.join() # Wait for all child processes to close.
    print(array)
    joblib.dump(array, 'data.pkl')
