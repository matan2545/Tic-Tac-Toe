# Matan Antebi
# 12.04.19
# ver 5.2

import socket, time
import pygame as py

"""
==============================
CONSTANTS
==============================
"""
TURN = False
WIDTH = 420
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
WHITE = (255, 255, 255)
LEFT = 1
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
music = 'music.mp3'
py.mixer.init()
py.mixer.music.load(music)
fin = False
"""
==============================
Client
==============================
"""
my_socket = socket.socket()
port = 9999
host = '127.0.0.1'
my_socket.connect((host, port))
print("Connected !")
"""
==============================
Define Images
==============================
"""
screen = py.display.set_mode(SIZE)
bg = py.image.load('BOARD.png')
ImgX = py.image.load('x.png')
ImgO = py.image.load('o.png')
ImgXRED = py.image.load('xR.png')
ImgORED = py.image.load('oR.png')
HOME = py.image.load('HOME.png')
RULES = py.image.load('RULES.png')
PICKNAME = py.image.load('PICKNAME.png')
LOSE = py.image.load('LOSE.png')
WIN = py.image.load('WIN.png')
DRAW = py.image.load('DRAW.png')
DUDU_WIN = py.image.load('DUDU_WIN.png')
PEWDIEPIE_WIN = py.image.load('PEWDIEPIE_WIN.png')
GEVER_WIN = py.image.load('GEVER_WIN.png')
KING_WIN = py.image.load('KING_WIN.png')
DUDU_LOSE = py.image.load('DUDU_LOSE.png')
PEWDIEPIE_LOSE = py.image.load('PEWDIEPIE_LOSE.png')
GEVER_LOSE = py.image.load('GEVER_LOSE.png')
KING_LOSE = py.image.load('KING_LOSE.png')
REMATCH_EXIT = py.image.load('REMATCH_EXIT.png')
WONWON = py.image.load('WOUWON.png')
LOSELOSE = py.image.load('LOSELOSE.png')
DRAWDRAW = py.image.load('DRAWDRAW.png')
#===============================
py.init()
"""
Checks position by x and y and return board area
"""
def CheckPos(x, y):
    if (x > 0 and x < 140) and (y > 0 and y < 140):
        return 1
    elif (x > 140 and x < 280) and (y > 0 and y < 140):
        return 2
    elif (x > 280 and x < 420) and (y > 0 and y < 140):
        return 3
    elif (x > 0 and x < 140) and (y > 140 and y < 280):
        return 4
    elif (x > 140 and x < 280) and (y > 140 and y < 280):
        return 5
    elif (x > 280 and x < 420) and (y > 140 and y < 280):
        return 6
    elif (x > 0 and x < 140) and (y > 280 and y < 420):
        return 7
    elif (x > 140 and x < 280) and (y > 280 and y < 420):
        return 8
    elif (x > 280 and x < 420) and (y > 280 and y < 420):
        return 9
"""
Get a number of an area and return the top left position of this area
"""
def WhatLoc(num):
    if num == 1:
        return 0, 0
    elif num == 2:
        return 140, 0
    elif num == 3:
        return 280, 0
    elif num == 4:
        return 0, 140
    elif num == 5:
        return 140, 140
    elif num == 6:
        return 280, 140
    elif num == 7:
        return 0, 280
    elif num == 8:
        return 140, 280
    elif num == 9:
        return 280, 280
"""
Checks if the 3 points have the same value in the game array and return a winner
"""
def Check(a, b, c, name, GAME):
    if (GAME[a] == 'X') and (GAME[b] == 'X') and (GAME[c] == 'X'):
        nx, ny = WhatLoc(a+1)
        screen.blit(ImgXRED, (nx, ny))
        py.display.flip()
        time.sleep(0.08)
        # ======
        nx, ny = WhatLoc(b+1)
        screen.blit(ImgXRED, (nx, ny))
        py.display.flip()
        time.sleep(0.08)
        # ======
        nx, ny = WhatLoc(c+1)
        screen.blit(ImgXRED, (nx, ny))
        py.display.flip()
        # ======
        time.sleep(1)
        Win("X", name)
        return "X"
    elif (GAME[a] == 'O') and (GAME[b] == 'O') and (GAME[c] == 'O'):
        nx, ny = WhatLoc(a+1)
        screen.blit(ImgORED, (nx, ny))
        py.display.flip()
        time.sleep(0.08)
        # ======
        nx, ny = WhatLoc(b+1)
        screen.blit(ImgORED, (nx, ny))
        py.display.flip()
        time.sleep(0.08)
        # ======
        nx, ny = WhatLoc(c+1)
        screen.blit(ImgORED, (nx, ny))
        py.display.flip()
        # ======
        time.sleep(1)
        Win("O", name)
        return "O"
    else:
        return "-"
"""
Change window caption to the results and show the winner image
"""
def Win(Winner, name):
    if Winner == "X":
        py.display.set_caption('OPPONENT WON!')
        if name == "DUDU FARUK":
            screen.blit(LOSE, (0, 0))
            py.display.flip()
            screen.blit(DUDU_LOSE, (0, 0))
            py.display.flip()
        elif name == "GEVER123":
            screen.blit(LOSE, (0, 0))
            py.display.flip()
            screen.blit(GEVER_LOSE, (0, 0))
            py.display.flip()
        elif name == "HA KING":
            screen.blit(LOSE, (0, 0))
            py.display.flip()
            screen.blit(KING_LOSE, (0, 0))
            py.display.flip()
        else:
            screen.blit(LOSE, (0, 0))
            py.display.flip()
            screen.blit(PEWDIEPIE_LOSE, (0, 0))
            py.display.flip()
    elif Winner == "O":
        py.display.set_caption('YOU WON!')
        if name == "DUDU FARUK":
            screen.blit(WIN, (0, 0))
            py.display.flip()
            screen.blit(DUDU_WIN, (0, 0))
            py.display.flip()
        elif name == "GEVER123":
            screen.blit(WIN, (0, 0))
            py.display.flip()
            screen.blit(GEVER_WIN, (0, 0))
            py.display.flip()
        elif name == "HA KING":
            screen.blit(WIN, (0, 0))
            py.display.flip()
            screen.blit(KING_WIN, (0, 0))
            py.display.flip()
        else:
            screen.blit(WIN, (0, 0))
            py.display.flip()
            screen.blit(PEWDIEPIE_WIN, (0, 0))
            py.display.flip()
    else:
        py.display.set_caption('DRAW!')
        screen.blit(DRAW, (0, 0))
        py.display.flip()
"""
Checks all the possible ways to win every call
"""
def Algorithm(name, GAME):
    if Check(0, 1, 2, name, GAME)[0] != "-":
        return True
    elif Check(0, 3, 6, name, GAME)[0] != "-":
        return True
    elif Check(0, 4, 8, name, GAME)[0] != "-":
        return True
    elif Check(0, 1, 2, name, GAME)[0] != "-":
        return True
    elif Check(1, 4, 7, name, GAME)[0] != "-":
        return True
    elif Check(3, 4, 5, name, GAME)[0] != "-":
        return True
    elif Check(2, 4, 6, name, GAME)[0] != "-":
        return True
    elif Check(2, 5, 8, name, GAME)[0] != "-":
        return True
    elif Check(6, 7, 8, name, GAME)[0] != "-":
        return True
    elif "-" not in GAME:
        Win("Tie", name)
        return True
    return False

"""
While no win/draw
"""
def Game1(fin, TURN, name):
    GAME = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    screen.blit(bg, (0, 0))
    py.display.flip()
    while not fin:
        for event in py.event.get():
            if event.type == py.QUIT:
                fin = True
            if TURN is True:
                py.display.set_caption('(' + name + ')' + ' YOUR TURN! (O)')
                py.mouse.set_visible(1)
                if event.type == py.MOUSEBUTTONDOWN:
                    if event.button == LEFT:
                        mouse_point = py.mouse.get_pos()
                        x, y = mouse_point
                        try:
                            data = CheckPos(x, y)
                            py.mouse.set_visible(0)
                            print(data)
                            if GAME[data-1] == '-':
                                TURN = False
                                my_socket.send(str(data))
                                GAME[data-1] = 'O'
                                newx, newy = WhatLoc(data)
                                screen.blit(ImgO, (newx, newy))
                                py.display.flip()
                                if Algorithm(name, GAME) is True:
                                    fin = True
                                    break
                        except:
                            continue

            else:
                py.display.set_caption('(' + name + ')' + ' OPPONENT TURN! (X)')
                print("client waiting")
                newdata = int(my_socket.recv(1024))
                TURN = True
                GAME[newdata - 1] = 'X'
                newx, newy = WhatLoc(newdata)
                screen.blit(ImgX, (newx, newy))
                py.display.flip()
                print("data from server: ", newdata)
                if Algorithm(name, GAME) is True:
                    fin = True
                    break
                print(GAME)
    time.sleep(1)

"""
Open rules page and wait for mouse input 
"""
def OpenRules():
    screen.blit(RULES, (0, 0))
    py.display.flip()
    press = False
    while not press:
        for event in py.event.get():
            if event.type == py.MOUSEBUTTONDOWN:
                if event.button == LEFT:
                    mouse_point = py.mouse.get_pos()
                    x, y = mouse_point
                    if (x > 128 and x < 292) and (y > 291 and y < 355):
                        press = True
                        break
"""
Gets X score and O score and changes the score on the board
"""
def Score(scoreX, scoreO, screen):
    py.draw.rect(screen, (0, 0, 0), [0, 420, 420, 60])
    py.font.init()
    myfont = py.font.SysFont('Comic Sans MS', 20)
    textsurface = myfont.render("Your Score: " + str(scoreO), False, GREEN)
    screen.blit(textsurface, (10, 420))
    textsurface = myfont.render("Opponent Score: " + str(scoreX), False, RED)
    screen.blit(textsurface, (10, 440))
    py.display.flip()
"""
Gets X score and O score and display the score
on the end screen
"""
def EndScore(scoreX, scoreO, Color):
    py.font.init()
    myfont = py.font.SysFont('Comic Sans MS', 50)
    textsurface = myfont.render(str(scoreO) + " - " + str(scoreX), False, Color)
    screen.blit(textsurface, (160, 220))
    py.display.flip()
"""
Open Rematch and Exit buttons and wait for mouse input
"""
def ReMatchExit():
    screen.blit(REMATCH_EXIT, (0, 0))
    py.display.flip()
    py.mouse.set_visible(1)
    press = False
    while not press:
        for event in py.event.get():
            if event.type == py.MOUSEBUTTONDOWN:
                if event.button == LEFT:
                    mouse_point = py.mouse.get_pos()
                    x, y = mouse_point
                    if (22 < x < 195) and (363 < y < 393):
                        return "REMATCH"
                    if (300 < x < 380) and (363 < y < 393):
                        return "EXIT"
"""
Open home page and wait for mouse input
"""
def HomePage():
    screen.blit(HOME, (0, 0))
    py.display.flip()
    press = False
    while not press:
        for event in py.event.get():
            if event.type == py.MOUSEBUTTONDOWN:
                if event.button == LEFT:
                    mouse_point = py.mouse.get_pos()
                    x, y = mouse_point
                    print(x, y)
                    if (x > 100 and x < 320) and (y > 200 and y < 290):
                        press = True
                        break
                    elif (x > 116 and x < 306) and (y > 290 and y < 363):
                        press = True
                        OpenRules()
                        break
"""
Open name page and wait for mouse input
"""
def NamePage():
    screen.blit(PICKNAME, (0, 0))
    py.display.flip()
    press = False
    while not press:
        for event in py.event.get():
            if event.type == py.MOUSEBUTTONDOWN:
                if event.button == LEFT:
                    mouse_point = py.mouse.get_pos()
                    x, y = mouse_point
                    if (x > 57 and x < 182) and (y > 207 and y < 264):
                        return "DUDU FARUK"
                        break
                    elif (x > 238 and x < 362) and (y > 207 and y < 264):
                        return "GEVER123"
                        break
                    elif (x > 57 and x < 182) and (y > 286 and y < 345):
                        return "HA KING"
                        press = True
                        break
                    elif (x > 238 and x < 362) and (y > 286 and y < 345):
                        return "PEWDIEPIE"
                        press = True
                        break
                    print(x, y)

def main():
    """
    Tic Tac Toe
    Made by Matan Antebi 2019
    Main definition (client)
    """
    TURN = False
    py.mixer.music.play()
    ScoreX = 0
    ScoreO = 0
    screen = py.display.set_mode(SIZE)
    HomePage()
    name = NamePage()
    Score(ScoreX, ScoreO, screen)
    EXIT = "CONTINUE"
    while EXIT != "EXIT":
        py.mouse.set_visible(1)
        Game1(fin, TURN, name)
        if py.display.get_caption()[0] == 'OPPONENT WON!':
            ScoreX += 1
            Score(ScoreX, ScoreO, screen)
            TURN = False
        elif py.display.get_caption()[0] == 'YOU WON!':
            ScoreO += 1
            Score(ScoreX, ScoreO, screen)
            TURN = True
        else:
            ScoreO += 1
            ScoreX += 1
        TEMP = ReMatchExit()
        HISTEMP = my_socket.recv(1024)
        my_socket.send(TEMP)
        if HISTEMP == "EXIT" or TEMP == "EXIT":
            EXIT = "EXIT"

    if int(ScoreX) < int(ScoreO):
        screen.blit(WONWON, (0, 0))
        py.display.flip()
        EndScore(ScoreX, ScoreO, GREEN)
    elif int(ScoreX) > int(ScoreO):
        screen.blit(LOSELOSE, (0, 0))
        py.display.flip()
        EndScore(ScoreX, ScoreO, RED)
    else:
        screen.blit(DRAWDRAW, (0, 0))
        py.display.flip()
        EndScore(ScoreX, ScoreO, BLACK)
    time.sleep(3)
    py.mixer.music.stop()
    py.quit()
    my_socket.close()

if __name__ == '__main__':
    main()


