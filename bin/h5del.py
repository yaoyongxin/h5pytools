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
    parser.add_argument("-d", "--dataset", type=str, default="",
            help="group to be deleted (str)")
    args = parser.parse_args()
    if args.dataset == "" or args.file == "":
        print("nothing to be deleted.")
        return
    else:
        ans = input(f"delete {args.dataset} from file {args.file}? [Y/n]")
        if "n" in ans.lower():
            print("nothing to be deleted.")
            return
    with h5py.File(args.file, "a") as f:
        del f[args.dataset]
        print(f"{args.dataset} deleted.")


if __name__ == "__main__":
    h5del()
