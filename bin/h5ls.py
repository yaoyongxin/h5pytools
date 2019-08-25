#!/usr/bin/env python
import h5py, sys, pprint


def h5ls():
    fname = sys.argv[1]
    if '-g' in sys.argv:
        group = sys.argv[sys.argv.index('-g') + 1]
    else:
        group = "/"
    with h5py.File(fname, "r") as f:
        if '-a' in sys.argv:
            res = list(f[group].attrs)
        else:
            res = list(f[group])
    pprint.pprint(res)



if __name__ == "__main__":
    h5ls()
