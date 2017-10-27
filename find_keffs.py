# find_keffs.py
#
# Will Zywiec
#
# reads all COG output files in a directory and
# creates a .csv summary file in the following format: filename, keff, standard deviation

from os import getcwd, listdir
from os.path import isfile, join

# get directory and generate a list of all filenames with '.out'
myPath = getcwd()
allFiles = [f for f in listdir(myPath) if (isfile(join(myPath,f)) and '.out' in f)]
allFiles.sort()

# open file to write everything
f_out = open('all_keffs.csv', 'w')

# search file, line by line, for 'Average Multiplication' and 'Standard Deviation' and split up all values after it with a comma
for file in allFiles:
    f = open(file)
    for line in f:
        if 'Average Multiplication' in line:
            str = file
            for num in line.split('=')[1].split():
                str += ', ' +  num
        if 'Standard Deviation' in line:
            for num in line.split('=')[1].split():
                str += ', ' +  num
            f_out.write(str + '\n') # save each line as 'filename, num1, num2, ...'
