"""
File: Steeplechase.py
Name: hsuan yu
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
       if front_is_clear():
           move()
       else:
        jump()
        turn_left()





def jump():
    """
    pre-condition:Karel is on the

    """
    up()
    cross()
    down()
def up():
    turn_left()
    while not right_is_clear():
        #karel is facing north,wall is on the right
        move()

def turn_right():
    for i in range(3):
        turn_left()

def cross():
    turn_right()
    move()
    turn_right()

def down():
    while front_is_clear():
        move()
    turn_left()






# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
