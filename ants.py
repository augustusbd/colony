## python 
# Colony - Ant Classes

class Queen:
	def __init__(self):
		self.id = 0
		self.title = 'Queen'
		self.age = 1				# age determines efficiency and title in colony
		self.age_limit = 30
		self.energy = 100
		self.status = 'Normal'		# Status : Normal, Wounded, Dead
									# wounded would decrease efficiency by 50%
	def lay_egg(self):
		# fertilize or unfertilized eggs
		# depends on amount of workers and drones that are alive
		# Workers to Drones == 80 to 20 (1 Drone for every 4 Workers)
		self.energy -= 1
		pass
		
class Worker:
	def __init__(self, ID):
		self.id = ID
		self.status = 'Normal'
		self.age = 3
		self.age_limit = 15
		self.dirs = {'east':0,'north':90,'west':180,'south':270} # directions in degrees
		#### self.job = 'Forage' 			# Jobs: Forage, Protect, Attack
		# Larvae become Workers or Drones at age 3
		# 3 days after egg has been lain
		# 2 days after egg hatches
									
	# Basic Functions -- Interactions with physical world
	# 			Senses
	def sense(self, surroundings):
		''' returns a dictionary of the surrounding area 
		e.g. - dict = {noise1:hear, pheremone1:smell, object1:touch  '''
		pass
		
	def hear(self, noises):
		pass
	def smell(self, phermones):
		pass
	def touch(self, object):	
		pass

	# 			Actions
	def leave_trail(self):
		pass
	def move(self, direction):
		pass
	def forage(self):
		pass
	def attack(self, enemy):
		pass
	def protect(self):
		pass


class Drone:
	'''' same basic functions as Worker class '''
	def __init__(self, ID):
		self.id = ID

