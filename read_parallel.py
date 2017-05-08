import multiprocessing

def process(file):
    pass # do stuff to a file

p = multiprocessing.Pool()
def get_all_files_path(basedir,ext='.h5') :
    file_temp = []
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            file_temp.append(f)
    return file_temp
for f in glob.glob("E:\data\million song data set\"+"*.csv"):
    # launch a process for each file (ish).
    # The result will be approximately one process per CPU core available.
    p.apply_async(process, [f])

p.close()
p.join() # Wait for all child processes to close.
