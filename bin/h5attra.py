#!/usr/bin/env python3
import h5py
import argparse


def list_attributes(name, obj):
    """Callback function to list attributes of an HDF5 object."""
    print(f"Object: {name}")
    for key, value in obj.attrs.items():
        print(f"  Attribute: {key}, Value: {value}")


def show_hdf5_attributes(file_path):
    """Open the HDF5 file and list attributes for all objects."""
    with h5py.File(file_path, 'r') as hdf_file:
        # List attributes of the root object
        print("Object: / (root)")
        for key, value in hdf_file.attrs.items():
            print(f"  Attribute: {key}, Value: {value}")
        hdf_file.visititems(list_attributes)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='List all attributes in an HDF5 file.')
    parser.add_argument('file_path', type=str, help='Path to the HDF5 file')

    args = parser.parse_args()
    show_hdf5_attributes(args.file_path)
