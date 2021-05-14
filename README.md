# Transport

These scripts were created for "A Solid of Revolution Time Study using COG11.1 and MCNP6.1", a paper I wrote in 2016.

## COG Scripts
**cog_slice.py**  
the **cog_solid** function turns the first sphere in a COG input deck into a solid of revolution with a user-defined number of segments  
the **cog_cone** function turns the first sphere in a COG input deck into a series of conical frustums with a user-defined number of segments

## MCNP Scripts
**cc.py**  
removes all MCNP 'comou', 'out', 'runtp', and 'srct' files from a directory

**mcnp_slice.py**  
the **mcnp_cone** function turns the first sphere in an MCNP input deck into a series of conical frustums with a user-defined number of segments  
the **mcnp_nounion** function turns the first sphere in an MCNP input deck into a series of conical frustums with a user-defined number of segments with no unions

## Misc

**batch.py**  
runs and times all COG and MCNP input decks

**jezebel.cog** and **jezebel.mcnp**  
example COG and MCNP input decks

**keff.py**  
tabulates keff and standard deviation for all COG and MCNP output files

**param.py**  
imports cog_solid, cog_cone, mcnp_cone, and mcnp_nounion functions and creates a set of COG and MCNP input decks
