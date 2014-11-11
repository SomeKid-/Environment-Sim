'''First part of the environmental simulator I am working on '''

#environment 

import random 
import time 
import varb

'''Everything below this point and above the next point has been moved to varb'''
'''run_number is the variable that tells the code how many times it is allowed to reset the life count. This number will change when the program goes to alpha.'''
#run_number = 5

#life = False

'''total number of lives in the sim'''
#life_count = 0 

'''Numbers of specific forms of life'''
#plant_count = 0
#BlueCow_count = 0
#Fang_count = 0
'''Everything above this point has been moved to varb'''

'''def creature():
	print("normal creature functioning goes here")
	life=True
	life_count=life_count+1
	return life'''

def spawn_new(life_form):
	if life_form == "BlueCow":
		print("BlueCow is added now")
	elif life_form == "Fang":
		print("Fang is added here")
	elif life_form == "plant":
		print("plant is added here")
	return life_form
	
def life_check():
	if varb.life == True:
		print(varb.life_count)
		print(varb.life)
	else:
		print(varb.life_count)
		print(varb.life)		
			
