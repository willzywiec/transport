# Transport

These scripts were created for 'A Solid of Revolution Time Study using COG11.1 and MCNP6.1', a paper I wrote in 2016.

## COG Scripts
**slice.py**  
turns the first sphere in a COG input deck into a solid of revolution with a user-defined number of segments

**slicec.py**  
turns the first sphere in a COG input deck into a series of conical frustums with a user-defined number of segments

## MCNP Scripts
**cc.py**  
removes all MCNP 'comou', 'out', 'runtp', and 'srct' files from a directory

**slicem.py**  
turns the first sphere in an MCNP input deck into a series of conical frustums with a user-defined number of segments

## Misc
**batch.py**  
runs all files (in serial mode) in a directory as either COG11 or MCNP6 input decks

**find_keffs.py**  
reads all COG and/or MCNP output files in a directory and creates a .csv summary file in the following format: file name, keff, standard deviation

**param.py**  
imports dice, dicec, and dicem functions and creates a set of COG and MCNP input decks