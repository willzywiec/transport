# Transport

These scripts were created for "A Solid of Revolution Time Study using COG11.1 and MCNP6.1", a paper I wrote in 2016 (https://cog.llnl.gov/pdf/804831.pdf).
These scripts were made specifically to highlight why solids of revolution are necessary for modeling combinatorial geometry.  
  
To use these scripts, run **param.py** (builds COG and MCNP input decks) and then **batch.py** (runs COG and MCNP). If you want to use the current versions of either code, modify **batch.py**. The codes themselves are export-controlled, so it's up to the user to install and configure them properly
  
**Backstory**:
  
Whenever someone presents a new Monte Carlo radiation transport code, I usually ask if the developers wrote their own geometry libraries from scratch. If the answer is 'yes', I usually dismiss the entire code because I'm not interested in using poorly implemented geometric primitives and meshes.
  
There are experts out there who have a deep understanding and mastery of this topic and have already developed state-of-the-art libraries (https://www.cgal.org/), which everyone should be using.
  
When it comes to geometry, I prefer a buffet of kernels and visualization options, so on that note, I'll give a shout-out to Geant4 and the team at Royal Holloway for doing all the hard work to solve (or at least amortize) this problem (https://arxiv.org/pdf/2010.01109.pdf).

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
