# param.py
#
# Will Zywiec
#
# imports dice, dicec, and dicem
# and creates a set of COG and MCNP input decks
#
# requires slice.py, slicec.py, and slicem.py

from os import system
from slice import dice
from slicec import dicec
from slicem import dicem

list = list(range(10, 1000, 10))
list.append(1000)
list.remove(350)
list.remove(700)

for l in list:
	dice('j', l)
	dice('j10', l)
	dicec('j', l)
	dicec('j10', l)
	dicem('jm', l)
