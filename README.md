COG Scripts
==========
**find_keffs.py**  
reads all COG output files in a directory and creates a .csv summary file in the following format: filename, keff, standard deviation

**slice.py**  
turns the first sphere in a COG input deck into a solid of revolution with a user-defined number of segments

**slicec.py**  
turns the first sphere in a COG input deck into a series of conical frustums with a user-defined number of segments

MCNP Scripts
==========
**cc.py**  
removes all MCNP 'comou', 'out', 'runtp', and 'srct' files from a directory

**slicem.py**  
turns the first sphere in a MCNP input deck into a series of conical frustums with a user-defined number of segments

Misc
==========
**batch.py**  
runs all files (in serial mode) in a directory as either COG11 or MCNP6 input decks

**param.py**  
imports dice, dicec, and dicem functions and creates a set of COG and MCNP input decks