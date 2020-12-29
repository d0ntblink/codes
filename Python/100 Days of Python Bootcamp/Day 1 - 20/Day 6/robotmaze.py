wall_on_left = True

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def check_wall_on_left():
    turn_left()
    if front_is_clear():
        wall_on_left = False
    else :
        wall_on_left = True
    turn_right()

while not at_goal() :
    check_wall_on_left()
    if front_is_clear() :
        move()
        if front_is_clear() and wall_on_left and right_is_clear() :
            move()
        else :
            turn_right()
    else :
        turn_left()