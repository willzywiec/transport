# batch.py
#
# Will Zywiec
#
# runs all files (in serial mode) in a directory as either COG11 or MCNP6 input decks
#
# 'screen python batch.py'

from os import getcwd, listdir, system
from os.path import isfile, join

# get directory and generate a list of all filenames
myPath = getcwd()
cogFiles = [f for f in listdir(myPath) if (isfile(join(myPath,f)) and 'j-' in f or 'jc-' in f)]
mcnpFiles = [f for f in listdir(myPath) if (isfile(join(myPath,f)) and 'jm-' in f)]
cogFiles.sort()
mcnpFiles.sort()

for file in cogFiles:
	str = '(time COG11 ' + file + ') > ' + file + '.out 2> ' + file + '-time'
	system(str)

for file in mcnpFiles:
	str = '(time mcnp6 in=' + file + ') > ' + file + '.out 2> ' + file + '-time'
	system(str)
	system('rm {comou*,out*,runtp*,srct*}')