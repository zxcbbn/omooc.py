# palette

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
import random

# init


time = 0
mode = 0
interval_list = [200,500,1000]
width = 800
height = 600
shape_list = ["ball","triangle","square"]
color_list = ['rgba(255, 0, 0, 0.3)',"Blue","Green"]
record_list = []
temp_record_list = []


# helper functions
def color(x):
    global color
    if color_list[int(x)] in color_list:
        color = int(x)
    else:
        color = random.choice([0,1,2])
def tick():
    global time
    time = time + 1
def speed(x):
    global speed
    speed = interval_list[int(x)]
# Define event handler for mouse click, draw
def click(pos):
    record_list.append([pos,shape,color])
def shape_choose(x):
    global shape
    shape = int(x)
    return
def draw(canvas):
    global mode
    if mode == 0:
        for img_pos in record_list:
            if shape_list[img_pos[1]] == "ball":
                canvas.draw_circle(img_pos[0], 15, 1,
                color_list[img_pos[2]],
                color_list[img_pos[2]])
            elif shape_list[img_pos[1]] == "triangle":
                canvas.draw_polygon([(img_pos[0][0], img_pos[0][1]+10), 
                (img_pos[0][0]-6, img_pos[0][1]), 
                (img_pos[0][0]+6, img_pos[0][1])], 2, 
                color_list[img_pos[2]],
                color_list[img_pos[2]])
            elif shape_list[img_pos[1]] == "square":
                canvas.draw_polygon([(img_pos[0][0]-5, img_pos[0][1]-5),
                (img_pos[0][0]+5, img_pos[0][1]-5),
                (img_pos[0][0]+5,img_pos[0][1]+5),
                (img_pos[0][0]-5,img_pos[0][1]+5)], 
                2, color_list[img_pos[2]],
                color_list[img_pos[2]])
                
    else:
        if len(record_list) > 1 and time < len(record_list):
            temp_record_list.append(record_list[time])
        for img_pos in temp_record_list:
            if shape_list[img_pos[1]] == "ball":
                canvas.draw_circle(img_pos[0], 15, 1,
                color_list[img_pos[2]],
                color_list[img_pos[2]])
            elif shape_list[img_pos[1]] == "triangle":
                canvas.draw_polygon([(img_pos[0][0], img_pos[0][1]+10), 
                (img_pos[0][0]-6, img_pos[0][1]), 
                (img_pos[0][0]+6, img_pos[0][1])], 2, 
                color_list[img_pos[2]],
                color_list[img_pos[2]])
            elif shape_list[img_pos[1]] == "square":
                canvas.draw_polygon([(img_pos[0][0]-5, img_pos[0][1]-5),
                (img_pos[0][0]+5, img_pos[0][1]-5),
                (img_pos[0][0]+5,img_pos[0][1]+5),
                (img_pos[0][0]-5,img_pos[0][1]+5)], 
                2, color_list[img_pos[2]],
                color_list[img_pos[2]])
def review():
    timer = 0
    global speed
    global count
    global mode
    speed = 500
    mode = 1
    timer = simplegui.create_timer(speed, tick)
    timer.start() 
    print time
    if time >= len(record_list):
        timer.stop() 
        print time
def restart():
    global time 
    global record_list
    global temp_record_list
    time = 0
    mode = 0
    record_list = []
    temp_record_list = []



# create frame
frame = simplegui.create_frame("painting board", width, height)
frame.set_canvas_background("White")
color = frame.add_input('color', color, 50)
shape = frame.add_input('shape', shape_choose, 50)
speed = frame.add_input('speed', speed, 50)
review = frame.add_button('review', review)
restart = frame.add_button('restart', restart)




# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)



# start frame or timer
frame.start()




