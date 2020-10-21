from abc import *

class NetworkInterface(ABC):
	'NetworkInterface class declaration'
	@abstractmethod					
	def connect(self):						# Abstract Method declaration
		pass

	@abstractmethod
	def transfer(self):
		pass

class RealNetwork(NetworkInterface):
	'RealNetwork class declaration derived from NetworkInterface'
	def connect(self):					# Abstract Method implimentation
		return 'RealNetwork class connected with NetworkInterface'

	def transfer(self):
		return 'All data transfered to NetworkInterface'

object = RealNetwork()
print(object.connect())
print(object.transfer())