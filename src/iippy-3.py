import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math 
import random

#init 
record_list = []
record_list_round = [] 
count = 0
range_choose = [0,100]

#helper functions

# definition of number_guess class
class number_guess:
    # initializer for range
    def __init__(self, range_choose):
        self.range = range_choose
    # choose a number in a particular range
    def number_choose(self):
    	self.number_chosen = random.randint(self.range[0],self.range[1])
    # review 
    def review(self):
    	number_chosen = self.number_chosen
    	global record_list_round
    	global record_list
    	global count
    	record_list_round.append(number_chosen)
    	if record_list_round[0] != record_list_round[count]:
    		count = count + 1
    		record_list.append(record_list_round)
    		count = 0
    		record_list_round = [] 
    
# compare guessed number and picked number
def number_compare(number_picked,number_guessed):
    global delta
    delta = number_guessed - number_picked
    if delta == 0:
    	print "Amazing"
    elif delta > 0:
    	print "Lower"
    else:
    	print "Higher"
# algorithm to change range 
def range_change(range_choose,number_guessed):
	global delta
	i = 0
	if delta < 0:
		i = 0
	else :
		i = 1
	range_choose[i] = (range_choose[i] + number_guessed)/2.0
	range_choose[int(not i)] = number_guessed


# event handlers
def game_start():
	global range_choose
	num_pick = number_guess(range_choose)
	num_pick.review
	num_guess = number_guess(range_choose)
	num_guess.review
	print num_guess
	number_compare(num_pick,num_guess)
	while record_list_round[0] != record_list_round[count]:
		range_change(range_choose,num_guess)
		num_guess = number_guess(range_choose)
		num_guess.review




# create frame
frame = simplegui.create_frame("guess_number",400,400)
frame.add_button('start', game_start, 100)


#start game
frame.start()
