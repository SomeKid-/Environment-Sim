'''First part of the environmental simulator I am working on '''

#environment 

import random 
import time 

life = False

life_count = 0 

def creature():
	'''This will eventually be replaced by various creature functions '''
	print("normal creature functioning goes here")
	life=True
	return life

def spawn_new(type):
	if type == "herbivore":
		print("herbivore is added now")
	elif type == "carnivore":
		print("carnivore is added here")
	elif type == "plant":
		print("plant is added here")
	return type
	
def life_check():
	while True:
		if life == True:
			life_count = life_count + 1
			print(life_count)
		else:
			spawn_new("herbivore")
