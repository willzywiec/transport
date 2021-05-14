# Transport

These scripts were created for "A Solid of Revolution Time Study using COG11.1 and MCNP6.1", a paper I wrote in 2016 (https://cog.llnl.gov/pdf/804831.pdf).  
  
They were made specifically to highlight how necessary solids/surfaces of revolution are for modeling combinatorial geometry. The joke I made during my presentation is that Egyptians invented the lathe sometime around 1300 BC because they understood the value of turning stone and wood. Unlike the Egyptians, my counterparts at Los Alamos still haven't figured out how to include a similar feature in their code. Needless to say, the joke didn't land, and as of this writing, MCNP still doesn't have this feature, which I think should be standardized across all radiation transport codes. I also included COG and MCNP versions of the Jezebel benchmark, which I used as a toy problem in my paper.

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
