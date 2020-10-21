from abc import *

class Vehical(ABC):
	'Abstract class Vehicle declaration'
	@abstractmethod
	def noOfWheels(self):			# Abstract method declaration
		pass

	def engine(self):
		return 'Engine of this vehicle is good!!'

class Car(Vehical):
	def noOfWheels(self):			# Abstract method implimentation
		return 'Number of vehicle wheels: 4'

car_object = Car()
print(car_object.noOfWheels())
print(car_object.engine())