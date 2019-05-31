# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

	
class Vehicle:							# base class	
	pass	

class GroundVehicle(Vehicle):					# 1st descendant
	pass

class FlightVehicle(Vehicle):					# 1st descendant
	pass

class Car(GroundVehicle):								# child of GroundVehicle
	pass

class Motorcycle(GroundVehicle):						# child of GroundVehicle
	pass

class Starship(FlightVehicle):							# child of FlightVehicle
	pass

class Airplane(FlightVehicle):							# child of FlightVehicle
	pass