# pisa-tutorials
A collection of tools and tutorials that will be useful for the presentation of the tool Astrovisio at Scuola Normale Superiore di Pisa

## generate_hdf5_file.py

This script generates a random example simulation file that can be read with `pynbody` and is compatible with Astrovisio. The output file contains a single gas family with random positions and masses, and is useful for testing or demonstration purposes.

### Usage

**From the command line:**
```bash
python generate_example_pynbody_file.py
```

This will create a file called test_me.hdf5 inside the test_data_folder/ directory.

**Output**

The generated file will contain arrays for x, y, z, and mass for a large number of gas particles.

The file can be loaded with pynbody:
```PYTHON
import pynbody
sim = pynbody.load("test_data_folder/test_me.hdf5")
```

## check_fits_cube.py

This file implements a simplified version of the script that is used in the Astrovisio API, if the script run successfully then the file should be compatible with Astrovisio. In general, any fits file with NDIM=3 should pass the test.

### Usage

**From the command line:**
```bash
python this_script.py path/to/file.fits
```

## check_hdf5_file.py

This file implements a simplified version of the script used in the Astrovisio API for checking HDF5 simulation files (e.g., Gadget, Tipsy, etc.). If the script runs successfully, the file should be compatible with Astrovisio. In general, any simulation file readable by `pynbody` in `.hdf5` format and containing the variables `x`, `y`, and `z` should pass the test.

### Usage

**From the command line:**
```bash
python this_script.py path/to/file.hdf5
```


## split_hdf5_family.py

This script extracts a specified particle family (e.g., `gas`, `dm`, or `star`) from a simulation HDF5 file using `pynbody`, and writes it to a new file. This can be used to create a file containing only a single family from a more complex simulation, this is necessary as currently there is no sub-family selector in astrovisio and only the first family found is loaded.

### Usage

**From the command line:**
```bash
python split_hdf5_family.py path/to/file.hdf5 family
```


# Requirements

using `pip` simply clone this repository and run `pip install -r requirements.txt` or using `uv` run `uv sync`.