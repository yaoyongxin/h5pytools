#!/usr/bin/env python
import h5py, argparse, glob


def h5del():
    h5files = glob.glob("*h5")
    if len(h5files) >= 1:
        h5file = h5files[0]
    else:
        h5file = ""
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, default=h5file,
            help="file to be edited (str)")
    parser.add_argument("-d", "--dataset", type=str, default="/",
            help="group to be deleted (str)")
    parser.add_argument("-a", "--attribute", type=str, default="",
            help="attribute to be deleted (str)")
    args = parser.parse_args()
    if args.file != "":
        with h5py.File(args.file, "a") as f:
            if args.attribute != "":
                del f[args.dataset].attrs[args.attribute]
                print(f"f['{args.dataset}'].attrs['{args.attribute}'] deleted.")
            else:
                del f[args.dataset]


if __name__ == "__main__":
    h5del()
