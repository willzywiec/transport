# keff.py
#
# Will Zywiec
#
# reads all COG and/or MCNP output files in a directory and
# creates a .csv summary file in the following format: file name, keff, standard deviation

from os import getcwd, listdir
from os.path import isfile, join

myPath = getcwd()
files = [f for f in listdir(myPath) if (isfile(join(myPath,f)) and '.o' in f)]
files = [f for f in files if 'slurm' not in f] # ignore Slurm output
files.sort()

f_out = open('all_keffs.csv', 'w')

# search file, line by line, for 'Average Multiplication' or 'final result'
for file in files:
	f = open(file)
	if 'Average Multiplication' not in open(file).read() or 'final result' not in open(file).read():
		str = file
		str += ', error\n'
		f_out.write(str)
	else:
		for line in f:
			# COG
			if 'Average Multiplication' in line:
				str = file
				for num in line.split('=')[1].split():
					str += ', ' +  num
			if 'Standard Deviation' in line:
				for num in line.split('=')[1].split():
					str += ', ' +  num
				f_out.write(str + '\n') # save each line as 'filename, num1, num2, ...'
			# MCNP
			if 'final result' in line:
				str = file
				str += ', ' + line.split(' ')[16]
				str += ', ' + line.split(' ')[25] + '\n'
				f_out.write(str)
