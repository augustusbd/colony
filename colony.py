## python 
import numpy as np
import matplotlib  
import ants as ant


class World:
	# global grid = np.zeros(100,100)
	def __init__(self, size):
		self.grid = np.zeros(size)
		# create self.border to be 1 unit wide along border of grid
	def populate(self):
		# place food around map randomly
		pass

class Colony(ant.Queen):
	def __init__(self):
		ants = {self.id:self.title}			#first ant is colony
		ants.update()				# every 1000? ants, archive with pickle maybe?
		
	def kill_ant(self,ID):
		del ants[ID] 	# maybe	
	def kill_ants(self,dict,ID):
		ant_ids = []
		for x,y in dict.items():
			if (y == 'Dead'):
				ant_ids.append(x)

# DICTIONARY HELP INSIDE MAIN()				
def main():	
	'''
Dictionary Help
# id = 5
# dict = {}
# dict.update( {str(id)'worker'} )
#		dict = {'5''worker'}
# dict.update( {id'drone'})
#		dict = {'5''worker', 5'drone'}

# for x,y in dict.items()
#	print(x,y) 			prints out key and value pairs line by line without 
	
# dict.update( [(1022,'drone'),(9290,'drone'),(420,'worker')] )	---- multiple entries at once	

#  a = { 5'worker', 82'worker'}
# dict.update(a)
#		dict = { '5''worker', 5'worker', 82'worker'}

# 
## deleting entries from dictionary - in this case keys that are strings
# d = []
# for x,y in dict.items()
#		if ( type(x) == str)
#			d.append(x)
# for x in d
# del dict[x]
	'''
	pass
	
if __name__ == '__main__':
	main()

