import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math 
import random

#init 
record_list = []
record_list_round = [] 

#helper functions

# definition of number_guess class
class number_guess:
    
    # initializer for range
    def __init__(self, range):
        self.range = range
    # choose a number in a particular range
    def number_choose(self, number_chosen):
    	self.number_chosen = random.randrange(self.range[0],self.range[1])
	# method that updates the range computer to guess   
    def update_range(self,update):
    	self.range[0] += update[0]
        self.range[1] += update[1]
    
# algorithm to change range 
def number_compare(number_pick,number_guess,range):
	i = 0
	if number_guess > number_pick:
		i = 1
	else:
		i = 0
	range[i] = (range[i] + number_guess)/2.0
	range[int(not i)] = number_guess



# event handlers


# create frame

# create a record_list



#start game

