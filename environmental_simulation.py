'''First part of the environmental simulator I am working on '''

#environment 

import random 
import time 

'''run_number is the variable that tells the code how many times it is allowed to reset the life count. This number will change when the program goes to alpha.'''
run_number = 5

life = False

'''total number of lives in the sim'''
life_count = 0 

'''Numbers of specific forms of life'''
plant_count = 0
BlueCow_count = 0
Fang_count = 0



def creature():
	'''This will eventually be replaced by various creature functions '''
	print("normal creature functioning goes here")
	life=True
	return life

def spawn_new(type):
	if type == "BlueCow":
		print("BlueCow is added now")
	elif type == "Fang":
		print("Fang is added here")
	elif type == "plant":
		print("plant is added here")
	return type
	
def life_check():
	for a in range(0,run_number):
		if life == True:
			life_count = life_count + 1
			print(life_count)
		else:
			spawn_new("BlueCow")

			
