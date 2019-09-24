#!/usr/bin/env python
import h5py, pprint, argparse, glob


def h5ls():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, default=glob.glob("*h5")[0],
            help="file to be checked (str)")
    parser.add_argument("-g", "--group", type=str, default="/",
            help="group to be checked (str)")
    parser.add_argument("-m", "--mode", type=int, default=0,
            help="check mode: 0->dataset; other->attributes.")
    args = parser.parse_args()
    with h5py.File(args.file, "r") as f:
        if args.mode == 0:
            res = list(f[args.group])
        else:
            res = list(f[args.group].attrs)
    pprint.pprint(res)



if __name__ == "__main__":
    h5ls()
