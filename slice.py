# slice.py
#
# Will Zywiec
#
# turns the first sphere in a COG input deck into a solid of revolution
# with a user-defined number of segments
#
# >> python -c 'from slice import dice; dice(segments)'

import math, sys
from os import getcwd, listdir
from os.path import isfile, join

def dice(file, segments):

	degrees = 90 / (float(segments) / 2)

	degreeSteps = [0.0]
	i = 0

	while degreeSteps[-1] < 90:
		i += 1
		degreeSteps.append(i * degrees)

	radianSteps = []

	for d in degreeSteps:
	        radianSteps.append(math.radians(d))

	f = open(file)

	radius = []
	i = 0

	# get radius and surface index
	for line in f:
		line.lower()
		if 'sphere' in line:
			surfIndex = i
			for num in line.split():
				radius.append(num)
			break
		i += 1

	radius = round(float(radius[-1]), 6)

	xValues = []
	yValues = []

	# get coordinates for half pseudo-sphere
	for r in radianSteps:
		if str(round(-radius * math.cos(r), 6)) != '-0.0':
			xValues.append(str(round(-radius * math.cos(r), 6)))
		else:
			xValues.append('0.0')
		yValues.append(str(round(radius * math.sin(r), 6)))

	# reverse x-values
	for x in reversed(xValues):
		if x != '0.0':
			xValues.append(str(abs(float(x))))

	# reverse y-values
	for y in reversed(yValues):
		if y != str(radius):
			yValues.append(y)

	# write output file
	newFile = file + '-' + str(segments)

	f = open(file)

	newInput = f.readlines()

	newInput[surfIndex] = 'SURFACES  1 rev ' + str(segments + 1) + '\n'

	i = 0

	for x in xValues:
		if (i + 1) % 5 == 0 and i != 0:
			newInput[surfIndex] += '  ' + str(x) + ' ' + str(yValues[i]) + '\n'
		else:
			newInput[surfIndex] += '  ' + str(x) + ' ' + str(yValues[i])
		i += 1

	newInput[surfIndex] += '\n'

	nF = open(newFile, 'w')
	nF.writelines(newInput)

	f.close()
	nF.close()
