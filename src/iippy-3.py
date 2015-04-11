import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math 
import random

#init 
record_list = []
record_list_round = [] 
count = -1
range_choose = [0,100]

#helper functions

# choose a number in a particular range
def number_choose(range_choose):
    number_chosen = random.randint(range_choose[0],range_choose[1])
    global record_list_round
    global record_list
    global count
    record_list_round.append(number_chosen)
    print record_list_round
    if count > 0 and record_list_round[0] != record_list_round[count]:
        record_list.append(record_list_round)
        record_list_round = [] 
        count = -1
    count = count + 1
    return number_chosen
    
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
def random_number():
	global num_pick
	global range_choose
	num_pick = number_choose(range_choose)

def game_start():
	global record_list_round
	global record_list
	global count
	global num_pick
	num_guess = number_choose(range_choose)
	print count
	print num_guess
	print num_pick
	number_compare(num_pick,num_guess)
	while count > 0 and record_list_round[0] != record_list_round[count]:
	  range_change(range_choose,num_guess)
	  num_guess = number_choose(range_choose)



# create frame
frame = simplegui.create_frame("guess_number",400,400)
frame.add_button('start', game_start, 100)
frame.add_button('random_choose', random_number, 100)



#start game
frame.start()
