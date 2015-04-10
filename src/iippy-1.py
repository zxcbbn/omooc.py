# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import math
import simplegui
import time


# helper function to start and restart the game
def new_game():
    input_guess(int(i))
    return
# define event handlers for control panel
def range100():
    global random_choose
    global i #counts game chanes
    global range
    i = 6
    range = 100
    random_choose = random.randrange(0, 100)
    print "Let me think for a while"
    #    time.sleep(3)
    print "I have picked a number in this range"
    new_game()
    return
def range1000():
    global random_choose
    global i #counts game chanes
    global range
    range = 1000
    i = 9
    random_choose = random.randrange(0, 1000)
    print "Let me think for a while"
    #    time.sleep(3)
    print "I have picked a number in this range"
    new_game()
    return

def input_guess(i):
    if i > 0:
        guessed_number = int(raw_input("Please input your guess:\n"),10)
        print "You've guessed %d " % guessed_number
        print "You have %d chances to guess" % i
        if guessed_number > range or guessed_number < 0:
            print "Please don't waste your chance"
        compare(guessed_number,i)
    else:
        print "You have no chances to guess,the correct number is %d" % random_choose
        print "Play it again in this range?"
        print "Press Y.\n" ">"
        start_it_again = raw_input()
        if start_it_again == "Y":
            new_game()
        else:
            print "Press start to start a new Game"
    return
def compare(guessed_number,i):
    difference = guessed_number - random_choose
    if difference == 0:
        print "Correct while remains %d chances" % i
    elif difference < 0:
        print "Higher"
        i = i - 1
        input_guess(i)
    else:
        print "Lower"
        i = i - 1
        input_guess(i)
    return
def start():
    def draw_handler(canvas):
        canvas.draw_text("Welcome to Guess the Num", (20, 20), 12, 'Blue')
        canvas.draw_text("Choose a range from the left side to start ", (20, 30), 12, 'Blue')
    
    frame.set_draw_handler(draw_handler)
    return
# create frame
frame = simplegui.create_frame("Guess The Num", 250, 250)
frame.set_canvas_background("white")
frame.add_button("range 0~100",range100,100)
frame.add_button("range 0~1000",range1000,100)
frame.add_button("start",start,100)
#frame.set_draw_handler(draw_handler)
frame.start()




# game start


