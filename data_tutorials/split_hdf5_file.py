import pynbody

import pynbody
import sys

# This is a simple script that shows how to extract a sub-family from a more complex hdf5 file.


def split_hdf5_file(path, family):

    if family is None:
        raise ValueError("Please pass a family to split.")
    else:
        sim = getattr(pynbody.load(path), family)

    # The block above is necessary to get the family from a string, usually just doing sim.gas or sim.dm or sim.star and then doing sim.write would be enough.

    sim.write(
        filename=f"{path.split('.hdf5')[0]}_{family}.hdf5",
        fmt=pynbody.snapshot.tipsy.TipsySnap,
    )


if __name__ == "__main__":
    # Accept file path as a command-line argument or from input
    if len(sys.argv) > 2:
        hdf5_path = sys.argv[1]
        family = sys.argv[2]

    split_hdf5_file(hdf5_path, family)
