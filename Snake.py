import curses
import random


screen = curses.initscr()  # before doing anything, curses must be initialized. Done by initscr().
# initscr() will determine he terminal type,
# sends setup code to the terminal to create various internal data structures
curses.curs_set(0)  # set cursor to 0  invisible
height, width = screen.getmaxyx()  # Return a tuple (y, x) of the height and width of the window.
w = curses.newwin(height, width, 1,
                  1)  # Return a new window, whose left-upper corner is at (1,1), and whose height/width is (height,width).
w.keypad(1)  # If yes is 1, escape sequences generated by some inputs will be interpreted by curses.
#  If yes is 0, escape sequences will be left as is in the input stream. If it is 0, press any input, the game ends
w.timeout(188)  # how fast the snake is going

snk_x = width / 4
snk_y = height / 2
snake = [
    [snk_y, snk_x],
    [snk_y - 1, snk_x],
    [snk_y - 2, snk_x],
    [snk_y - 3, snk_x]
]  # snake's size

food = [height / 2, width / 2]
w.addch(int(food[0]), int(food[1]),
        curses.ACS_PI)  # window.addch(y, x, ch[, attr]) Paint character ch at (y, x) with attributes attr

input = curses.KEY_RIGHT  # the snake goes to the right when games starts

while 1:
    next_input = w.getch()  # Get a character; -1 means there is no input

    if (next_input == -1):
        input = input
    else:
        input = next_input
    if snake[0][0]<=0 or snake[0][0]>=height-1 or snake[0][1] <=0 or snake[0][1]>= width-1:
    #if  snake[0][0] in [0, height] or snake[0][0] in [0, width] or snake[0] in snake[1:] or snake[0][0] in [height, width] :
        curses.endwin()  # De-initialize the library, and return terminal to normal status
        quit()

    new_head = [snake[0][0], snake[0][1]]  # used for turning

    if input == curses.KEY_LEFT:
        new_head[1] -= 1
    if input == curses.KEY_RIGHT:
        new_head[1] += 1
    if input == curses.KEY_DOWN:
        new_head[0] += 1
    if input == curses.KEY_UP:
        new_head[0] -= 1


    snake.insert(0, new_head)

    if snake[0] == food:  # if food is eaten
        food = None
        while food is None:
            newfood = [random.randint(1, height - 1),random.randint(1, width - 1)]

            if newfood not in snake:
                food = newfood
            else:
                food = None

        w.addch(food[0], food[1], curses.ACS_PI)
    else:   #if the snake didnt get the food, pop the last bit of the snake body, add a blank at the tail
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')
        
        
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_DIAMOND)  #what character makes up the snake's body

        
