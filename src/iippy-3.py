import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math 
import random

#init 
record_list = []

#helper functions

# definition of number_guess class
class number_guess:
    
    # initializer for range
    def __init__(self, range):
        self.range = range

    # choose a number in a particular range
    def number_choose(self, number_chosen):
    	self.number_chosen = random.randrange(self.range[0],self.range[1])
	def number_compare(self,delta):
		self.delta = self.number_chosen - (self.range[1] - self.range[0])/2.0
	# method that updates the range computer to guess   
    def update_range(self):
    	if self.delta > 0:
    		self.range[0] = (self.range[1] - self.range[0])/2.0
    		self.range[1] = self.number_chosen
		else:
			self.range[1] = (self.range[1] - self.range[0])/2.0
    		self.range[0] = self.number_chosen



#event handlers

#create frame

# create a record_list
record_list = []
for i in range(100):
	n = number_guess([0, 100])

#start game

