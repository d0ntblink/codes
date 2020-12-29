def fuckgoback():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal() :
    if front_is_clear() :
        move()
        turn_right()
    else :
        turn_left()