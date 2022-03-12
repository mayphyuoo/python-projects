
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    turn_left()
    
def safe_move():
    if front_is_clear():
        move()

while not at_goal():
    if is_facing_north():
        if right_is_clear():
            turn_right()
            while front_is_clear() and not at_goal():
                move()
        elif (right_is_clear() == False) and (front_is_clear() == True):
            safe_move()
        else:
            turn_around()
            if front_is_clear():
                
                # stuck in wall north, east and west corner
                if right_is_clear() == False:
                    safe_move()
                    turn_right()
                    safe_move()
                    turn_right()
                    safe_move()
                else:
                    while front_is_clear():
                        move()
                    if right_is_clear():
                        turn_left()
                        while front_is_clear():
                            move()
                        if not at_goal():
                            turn_around()
                            safe_move()
                            turn_right()
                            while front_is_clear():
                                move()
                            turn_left()
                            safe_move()
                            turn_right()
                            while front_is_clear():
                                move()
            
            else:
                turn_right()
                if front_is_clear():
                    move()
                    turn_right()
                    safe_move()  
                
                
    else:
        turn_left()