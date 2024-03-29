start_pos = (0, 0)
MIDDLE = 50
STOP = 10

def checkdist():
    pass

def move_until(dist):
    while (checkdist() > dist):
        move_motors()

def turn_right(deg):
    while (current_degrees < deg):
        move_left_forward()
        move_right_backward()

def turn_left(deg):
    while (current_degrees < deg):
        move_left_backward()
        move_right_forward()

def move(toWhere):
    if toWhere == "Plastic":
        new_pos = (0, 1)
    elif toWhere == "Organic":
        new_pos = (0, -1)
    elif toWhere == "Paper":
        new_pos = (1, 0)
    else:
        new_pos = (-1, 0)
    
    if ((start_pos == (0, -1) and new_pos == (1, 0)) or (start_pos == (1, 0) and new_pos == (0, 1)) or (start_pos == (0, 1) and new_pos == (-1, 0)) or (start_pos == (-1, 0) and new_pos == (0, -1))):
        move_until(MIDDLE)
        turn_right(90)
    elif ((start_pos == (0, -1) and new_pos == (-1, 0)) or (start_pos == (-1, 0) and new_pos == (0, 1)) or (start_pos == (0, 1) and new_pos == (1, 0)) or (start_pos == (1, 0) and new_pos == (0, -1))):
        move_until(MIDDLE)
        turn_left(90)
    elif (start_pos == (0, 0)):
        if (new_pos == (-1, 0)):
            turn_left(90)
        elif (new_pos == (1, 0)):
            turn_right(90)
        elif (new_pos == (0, -1)):
            turn_right(180)
    move_until(STOP)
