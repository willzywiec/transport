# Transport

These scripts were created for "A Solid of Revolution Time Study using COG11.1 and MCNP6.1", a paper I wrote in 2016 (https://cog.llnl.gov/pdf/804831.pdf).
These scripts were made specifically to highlight how necessary solids/surfaces of revolution are for modeling combinatorial geometry.  
  
The joke I made during my presentation was that the Egyptians invented the lathe sometime around 1300 BC because they understood the value of rotational symmetry when turning stone and wood. Unlike the Egyptians, my counterparts at Los Alamos still haven't figured out how to implement a similar feature in MCNP. Needless to say, the joke didn't land and was considered to be somewhat inflammatory. As of this writing, however, MCNP still doesn't have this feature, which I think should be standardized across all radiation transport codes.
  
**TL;DR**: COG has a solid of revolution feature, MCNP does not. I built a toy problem to show the trade-off between problem complexity and simulation speed for two geometrically equivalent pseudo-spheres.  
  
To use these scripts, just run **param.py** (builds COG and MCNP input decks) and then **batch.py** (runs COG and MCNP). If you want to use the current versions of either code, just modify **batch.py**. The codes themselves are export-controlled, so it's up to the user to install and configure them properly.
  
**Backstory**: I have a longstanding, silent beef with physicists and engineers who develop their own geometry libraries from scratch, mostly because they end up forcing everyone else to use geometric primitives and poorly implemented mesh controls. There are experts out there who have a deep understanding and mastery of this topic and have already developed state-of-the-art libraries (https://www.cgal.org/). When it comes to geometry, I prefer a buffet of kernels and visualization options, so on that note, I'll give a shout-out to Geant4 and the team at Royal Holloway for doing all the hard work to solve (or at least amortize) this problem (https://arxiv.org/pdf/2010.01109.pdf).

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
imports **cog_solid**, **cog_cone**, **mcnp_cone**, and **mcnp_nounion** functions and creates a set of COG and MCNP input decks using the **cog_solid** and **mcnp_cone** functions (**cog_cone** and **mcnp_nounion** are commented out)
