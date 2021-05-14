# param.py
#
# Will Zywiec
#
# imports cog_solid, cog_cone, mcnp_cone, and mcnp_nounion
# and creates a set of COG and MCNP input decks

from os import system

from cog_slice import cog_solid
from cog_slice import cog_cone
from mcnp_slice import mcnp_cone
from mcnp_slice import mcnp_nounion

list = list(range(10, 1000, 10))
list.append(1000)
list.remove(350)
list.remove(700)

for l in list:
	cog_solid('jezebel.cog', l)
	# cog_cone('jezebel.cog', l) # uncommenting this line will overwrite jezebel.cog files
	mcnp_cone('jezebel.mcnp', l)
	# mcnp_nounion('jezebel.mcnp', l) # uncommenting this line will overwrite jezebel.mcnp files
