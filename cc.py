# cc.py
#
# Will Zywiec
#
# removes all MCNP 'comou', 'out', 'runtp', and 'srct' files from a directory

from os import system

system('rm {comou*,out*,runtp*,srct*}')
