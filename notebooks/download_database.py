import os
import shutil
import urllib.request
from zipfile import ZipFile
import numpy as np

# --> Function to download the dataset.
download_data = lambda url, fname : urllib.request.urlretrieve(url, fname)

# --> Process data.
def format_database(fname):

    # --> Unzip the dataset.
    with ZipFile(fname, "r") as zf:
        zf.extractall("data")

    # --> Load the data.
    nt = 3000 # Number of snapshots.
    name = lambda i : "data" + os.sep + "Res%05d"%(i+1) + ".dat"
    data = np.array([np.genfromtxt(name(i))[1:].flatten(order="F") for i in range(nt)]).T

    # --> Load the mesh.
    name = "data" + os.sep + "MESH.dat"
    mesh = np.genfromtxt(name)[1:]

    # --> Save data using npz format.
    np.savez("vki_cylinder_dataset.npz", mesh=mesh, data=data)

    # --> Clean-up the folder.
    os.remove(fname)
    shutil.rmtree("data", ignore_errors=True)

def main(url, fname="tmp.zip"):

    # --> Download data.
    download_data(url, fname)

    # --> Format the database for the tutorial.
    format_database(fname)


if __name__ == "__main__":

    # --> URL from which to download the data.
    url = "https://osf.io/47ftd/download"

    # --> Proceeds.
    main(url)



