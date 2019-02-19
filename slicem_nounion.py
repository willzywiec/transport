# slicem_nounion.py
#
# Will Zywiec
#
# turns the first sphere in a MCNP input deck into a series of conical frustums
# with a user-defined number of segments
#
# >> python -c 'from slicem import dicem; dicem(segments)'

import math, sys
from os import getcwd, listdir
from os.path import isfile, join

def dicem(file, segments):

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
		if 'so' in line:
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

	baseCoords = []
	i = 0

	# get base coordinates
	for x in xValues:
		i += 1
		if i == 1:
			xAbs = abs(float(xValues[i - 1]) - float(xValues[i]))
			yAbs = float(yValues[i])
			tSq = (yAbs / xAbs) ** 2
			baseCoords.append(xValues[i - 1] + '  ' + str(round(tSq, 6)) + '  +1')
			xPl_1 = str(round(float(xValues[i]), 6))
		elif i == segments / 2:
			baseCoords.append(xValues[i] + ' 0 0')
			baseCoords.append(xValues[i] + ' 0 0')
		elif i == segments - 1:
			xAbs = abs(float(xValues[i]) - float(xValues[i + 1]))
			yAbs = float(yValues[i])
			tSq = (yAbs / xAbs) ** 2
			baseCoords.append(xValues[i + 1] + '  ' + str(round(tSq, 6)) + '  -1')
			xPl_2 = str(round(float(xValues[i]), 6))
			baseCoords.append(xPl_1)
			baseCoords.append(xPl_2)
		elif i == segments:
			break
		else:
			baseCoords.append(xValues[i] + ' 0 0')

	hVectors = []
	i = 0

	# get cone height vectors
	for x in xValues:
		if i == segments:
			break
		else:
			xAbs = abs(float(xValues[i]) - float(xValues[i + 1]))
			yAbs = abs(float(yValues[i]) - float(yValues[i + 1]))
			yMax = max(float(yValues[i]), float(yValues[i + 1]))
			if float(yValues[i]) > float(yValues[i + 1]):
				hVectors.append(str(round(xAbs, 6)) + ' 0 0')
			else:
				hVectors.append(str(round(-xAbs, 6)) + ' 0 0')
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
	newFile = file + '-' + str(segments)

	f = open(file)

	newInput = f.readlines()
	newInput[surfIndex] = ''

	# get void cells
	newInput[2] = '4  0 '
	i = 0

	for s in range(0, segments):
		i += 1
		if i == 1:
			newInput[2] = newInput[2]
		elif i % 5 == 0 and i != segments:
			newInput[2] += ' & \n   ' + str(i)
		elif i == segments:
			newInput[2] += ' ' + str(i + 1) + ' ' + str(-(i + 2))
		elif i != 1 or i != segments - 1:	
			newInput[2] += ' ' + str(i)

	newInput[2] += '  imp:n = 0\n'
	newInput[2] += '5  0  ' + str(-(segments + 1)) + ' 1  imp:n = 0\n'
	newInput[2] += '6  0  ' + str(segments + 2) + ' ' + str(segments) + '  imp:n = 0\n'

	i = 0
	j = 0

	# get surface cells
	for s in range(0, segments):
		i += 1
		if i == 1:
			newInput[surfIndex] += str(i) + '  kx  ' + baseCoords[j] + '\n'
		elif i == segments:
			newInput[surfIndex] += str(i) + '  kx  ' + baseCoords[j] + '\n'
			newInput[surfIndex] += str(i + 1) + '  px  ' + baseCoords[j + 1] + '\n'
			newInput[surfIndex] += str(i + 2) + '  px  ' + baseCoords[j + 2] + '\n'
			break
		else:
			newInput[surfIndex] += str(i) + '  trc  ' + baseCoords[j] + '  ' + hVectors[j] + '  ' + rPairs[j] + '\n'
		j += 1

	newInput[1] = '1  1  0.040290  '
	i = 0

	# get plutonium cells
	for s in range(0, segments):
		i += 1
		if i == segments - 1:
			newInput[1] += str(-i) + '  imp:n = 1\n'
			newInput[1] += '2  1  0.040290  ' + str(-(segments + 1)) + ' -1  imp:n = 1\n'
			newInput[1] += '3  1  0.040290  ' + str(segments + 2) + ' ' + str(-segments) + '  imp:n = 1\n'
		else:
			newInput[1] += str(i - 1) + '  1  0.040290  -' + str(i) + ' imp:n = 1\n'

	nF = open(newFile, 'w')
	nF.writelines(newInput)

	f.close()
	nF.close()
