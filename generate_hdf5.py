"""
  Generate an example file that can be read with pynbody & astrovisio
"""


def generate_random_data(n_data=int(10**5)):

    import numpy as np

    # generate a minimal dataset to be used for AstroVisio
    print("calling generate_random_data()")
    print("  generating arrays of length ", n_data)

    out_dict = {}

    pos = np.zeros((3, n_data))
    mass = np.zeros(n_data)

    for ii in range(3):
        pos[0, :] = np.random.normal(loc=0.0, scale=1.0, size=n_data)
    mass[:] = np.random.uniform(low=1.0, high=2.0, size=n_data)

    out_dict["x"] = pos[0, :]
    out_dict["y"] = pos[1, :]
    out_dict["z"] = pos[2, :]
    out_dict["mass"] = pos[2, :]

    print("  keys in the dataset")
    for kk in sorted(out_dict.keys()):
        print("   ", kk)

    return out_dict


def dump_data_to_pynbody_readable_file(
    dict_in={}, out_folder="test_data_folder/", out_name="test_me.hdf5"
):

    import os
    import pynbody

    print("calling dump_data_to_pynbody_readable_file()")

    # set paths
    if not os.path.isdir(out_folder):
        os.mkdir(out_folder)

    f_out = out_folder + out_name

    # check size
    n_dataset = -1
    n_dataset = None
    for key in dict_in.keys():
        if n_dataset is None:
            n_dataset = len(dict_in[key])
        else:
            assert n_dataset == len(
                dict_in[key]
            ), "Data set has arrays of different sizes"

    # prepare and write a typsy like file
    out_snap = pynbody.new(gas=n_dataset)
    for key in dict_in.keys():
        out_snap.gas[key] = dict_in[key]

    # dump data as hdf5
    print("  dump to")
    print("   ", f_out)

    # as an alternative format, use pynbody.snapshot.gadget.GadgetSnap, but the header is a bit trickier to set up
    out_snap.write(filename=f_out, fmt=pynbody.snapshot.tipsy.TipsySnap)


if __name__ == "__main__":

    data_example = generate_random_data(n_data=int(10**5))
    dump_data_to_pynbody_readable_file(
        dict_in=data_example, out_folder="test_data_folder/", out_name="test_me.hdf5"
    )
