import numpy as np

from scipy.linalg import svd

import matplotlib.pyplot as plt

from skimage import data

def plot_img(img, savename="tmp.png"):

    fig, ax = plt.subplots(1, 1, figsize=(4, 4))

    ax.imshow(img, cmap=plt.cm.gray)
    ax.axis(False)

    plt.savefig(savename, bbox_inches="tight", dpi=300, transparent=True)

    plt.show()

if __name__ == "__main__":

    #####
    #####
    #####
    #####
    #####

    # --> Get image from skimage.
    img = getattr(data, "camera")()

    plot_img(img, savename="../data/camera.png")

    # --> Compute its SVD.
    U, S, Vt = svd(img)

    # for i in range(18):
    #     x = np.outer(U[:, i], Vt[i])
    #     plot_img(x, "../imgs/camera_svd_{0}_comp.png".format(i+1))
    # plt.show()

    for i in range(0, 90, 5):
        if i == 0:
            x = np.outer(U[:, i], Vt[i])
        else:
            x = U[:, :i+1] @ np.diag(S[:i+1]) @ Vt[:i+1, :]

        plot_img(x, "../imgs/camera_svd_{0}_estimate.png".format(i+1))

    # --> Outpost singular spectrum.
    # out = np.c_[np.arange(1, len(S)+1), S / np.max(S)]
    # np.savetxt("../data/camera_svd.dat", out)

    # out = np.c_[np.arange(1, len(S)+1), np.cumsum(S/np.sum(S))]
    # np.savetxt("../data/camera_svd_bis.dat", out)
