import numpy as np
import matplotlib.pyplot as pp
from astropy.io.fits import open as fitsopen
from astropy.io.fits import writeto as fitswrite

DEBUG = 1

def fits_read(filename,ext=0):
    return fitsopen(filename)[ext].data

data = {"StrehlData": None, "LEPSF": None, "PupilMask": None,
        "N_TARGETS": None, "IM_XDIM": None}

def load_results(filename):
    global data
    data["StrehlData"] = fits_read(filename, ext=0)
    data["LEPSF"] = fits_read(filename, ext=1)
    data["PupilMask"] = fits_read(filename, ext=2)
    if DEBUG:
        print("StrehlData.shape ="+str(data["StrehlData"].shape),flush=True)
        print("LEPSF.shape      ="+str(data["LEPSF"].shape),flush=True)
        print("PupilMask.shape  ="+str(data["PupilMask"].shape),flush=True)
    data["N_TARGETS"] = data["StrehlData"].shape[0]
    data["IM_XDIM"] = data["LEPSF"].shape[1]

def plot(exposure="le",units="strehl",xlim=None,ylim=None):
    # Need some data to play with

