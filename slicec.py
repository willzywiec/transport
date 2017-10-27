# slicec.py
#
# Will Zywiec
#
# turns the first sphere in a COG input deck into a series of conical frustums
# with a user-defined number of segments
#
# python -c 'from slicec import dice; dice(segments)'

import math, sys
from os import getcwd, listdir
from os.path import isfile, join

def dicec(file, segments):

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

	# get radius and surface/geometry/boundary indexes
	for line in f:
		line.lower()
		if 'sphere' in line:
			surfIndex = i
			for num in line.split():
				radius.append(num)
		if 'GEOMETRY' in line:
			geomIndex = i
		if 'boundary' in line:
			boundIndex = i
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

	hScalars = []
	i = 0

	# get cone height scalars
	for x in xValues:
		if i == segments:
			break
		else:
			xAbs = abs(float(xValues[i]) - float(xValues[i + 1]))
			hScalars.append(str(round(xAbs, 6)))
		i += 1

	rPairs = []
	i = 0

	# get radius pairs
	for y in reversed(yValues):
		if i == segments:
			break
		else:
			yMax = max(float(yValues[i]), float(yValues[i + 1]))
			yMin = min(float(yValues[i]), float(yValues[i + 1]))
			rPairs.append(str(round(yMax, 6)) + ' ' + str(round(yMin, 6)))
			i += 1

	# write output file
	newFile = file + 'c-' + str(segments)

	f = open(file)

	newInput = f.readlines()

	newInput[surfIndex] = 'SURFACES\n'

	i = 0

	for h in hScalars:
		if i < segments / 2:
			newInput[surfIndex] += str(i + 1) + ' cone ' + hScalars[i] + ' ' + rPairs[i] + '  0 ' + hScalars[i] + '  TR ' + xValues[i] + ' 0 0'
		if i >= segments / 2:
			newInput[surfIndex] += str(i + 1) + ' cone ' + hScalars[i] + ' ' + rPairs[i] + '  -' + hScalars[i] + ' 0  TR ' + xValues[i + 1] + ' 0 0'
		if i < len(hScalars) - 1:
			newInput[surfIndex] += '\n'
		i += 1

	newInput[surfIndex] += '\n'

	newInput[geomIndex] = 'GEOMETRY  sector 1 alloy\n'
	newInput[boundIndex] = 'boundary vacuum\n'

	i = 1

	for h in hScalars:
		if i % 10 == 0:
			newInput[geomIndex] += '-' + str(i) + ' \n'
			newInput[boundIndex] += '+' + str(i) + ' \n'
		if i == len(hScalars):
			break
		else:
			newInput[geomIndex] += '-' + str(i) + ' '
			newInput[boundIndex] += '+' + str(i) + ' '
		i += 1

	nF = open(newFile, 'w')
	nF.writelines(newInput)

	f.close()
	nF.close()
