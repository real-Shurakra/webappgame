"""This is the game settings file 


"""
##########################################################################################
## Accounting settings
#  You don't want to change any of this settings after your world is gerated
#
#  You should obviusly change the pepper and salt settings

## papper
strAccountPassPepper = 'K1ller'

## salt
strAccountPassSalt = 'Rab1t'

##########################################################################################
## pre-generate settings
#  This settings do not have any impact after the world is gereated

## number of solar systems
intSolarSystems = 20

## max and mix number of orbits a solar system can have
#  use intMaxSolarSystemorbits = intMinSolarSystemorbits if you don't want
#  solar systems to have randomised number of orbits
intMinSolarSystemorbits = 10
intMaxSolarSystemorbits = 30

## probability a solar orbit has a planet
intPlanetCreationPobability = 50

## probability a planet has a moon
intMoonCreationPobability = 25

## multiplikator for an additional moon to create
#  IMPORTANT: moons will be creted as long as a moon was created in first place
intMoonCreationPobabilitymult = 25

## max numbers of moons a planet can have while world generation
intMaxMoon = 3

##########################################################################################
## post-generate settings

## How mutch of the construction cost the player get refounded when 
#  a building is demolished (*%)
intDemolitionRefund = 75

## the scale a player gets resources and how long it will take to produce something
intUniverseSpeed = 1

##########################################################################################