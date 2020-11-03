#imports
import sys
from random import randint
import os
from colorama import Fore

#globals
title = (Fore.LIGHTCYAN_EX + "Find the hole")
cur_diff = (Fore.LIGHTGREEN_EX + "Easy")
map_hight = map_width = 7
start_level = 1
win_level = 3
start_X = start_Y = 4
tot_moves = 0

#clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#game start//main menu
def start():
    clear_screen()
    print(title) 
    print(Fore.WHITE + f"\nDiff:  {cur_diff}") 
    print(Fore.WHITE + "1. Play \n2. High Score. \n3. Change Diff \n4. Settings \n5. Help \n6. Quit \n")
    start_command = input(Fore.WHITE + "What do you want to do? \n")
    if start_command.lower() == "1":
        generate_hole(start_level, start_X, start_Y)
    elif start_command.lower() == "2":
        high_score_menu()
    elif start_command.lower() == "3":
        diff_menu()
    elif start_command.lower() == "4":
        settings_menu()
    elif start_command.lower() == "5":
        help_menu()
    elif start_command.lower() == "6":
        sys.exit()
    else:
        start()

#DIFFERENT MENUS

#high score menu
def high_score_menu():
    #input
    with open("high_score.txt", "r") as file:
      f = file.readlines()
      cur_high_score = []
      for line in f:
          cur_high_score.append(line.strip())
    #Output
    clear_screen()
    print(title)
    print(Fore.WHITE + "\n HIGH SCORE")
    print(f" Name: {cur_high_score[0]}\n Moves: {cur_high_score[1]}")
    exit_high_score = input('\nType "q" to exit\n')
    if exit_high_score.lower() == "q":
        start()
    else:
        high_score_menu()

#dif menue            
def diff_menu():
    global start_X
    global start_Y
    global win_level
    global map_hight
    global map_width 
    global cur_diff            
    clear_screen()
    print(f"{title}", Fore.WHITE + "\n\nChange Diff..\n")
    print(Fore.WHITE + "Diffs:\n Easy,   7x7 map & 3 levels. \n Medium, 9x9 map & 5 levels. \n Hard,   11x11 map & 7 levels.\n")
    set_diff = input(Fore.WHITE + "What diff would you like? ")
    if set_diff.lower() == "easy":
        win_level = 3
        map_hight = map_width = 7
        cur_diff = (Fore.LIGHTGREEN_EX + "Easy")
        start_X = start_Y = 4
        start()
    elif set_diff.lower() == "medium":
        win_level = 5
        map_hight = map_width = 9
        cur_diff = (Fore.LIGHTYELLOW_EX + "Medium")
        start_X = start_Y = 5
        start() 
    elif set_diff.lower() == "hard":
        win_level = 7
        map_hight = map_width = 11
        cur_diff = (Fore.LIGHTRED_EX + "Hard")
        start_X = start_Y = 6
        start()
    else:
        diff_menu()

#settings menu
def settings_menu():
    clear_screen()
    print(title)
    print(Fore.WHITE + "\nSettings are comming soon..")
    exit_settings = input('\nType "q" to exit\n')
    if exit_settings.lower() == "q":
        start()
    else:
        settings_menu

#help menu
def help_menu():
    clear_screen()
    print(f"{title}\n\n")
    print(Fore.WHITE + "The goal of the game is to find the all the holes.\nYou can change diffs and music in the game menu.\nCommands and controls are written on screen.")
    exit_help = input('\nType "q" to exit\n')
    if exit_help.lower() == "q":
        start()
    else:
        help_menu()

#hole generator
def generate_hole(level, x, y):
    holeX = randint(1, map_width)
    holeY = randint(1, map_hight)
    if (holeX == start_X) and (holeY == start_Y):
        generate_hole(level, x, y)
    else:
        generate_map(holeX, holeY, x, y, level)

#map generator
def generate_map(holeX, holeY, x, y, level):
    #tiles   vtl = visual top left ect..
    vtl = generate_tiles(x, y ,holeX, holeY, -1, 1)
    vtm = generate_tiles(x, y ,holeX, holeY, 0, 1)
    vtr = generate_tiles(x, y ,holeX, holeY, 1, 1)
    vml = generate_tiles(x, y ,holeX, holeY, -1, 0)
    vmr = generate_tiles(x, y ,holeX, holeY, 1, 0)
    vbl = generate_tiles(x, y ,holeX, holeY, -1, -1)
    vbm = generate_tiles(x, y ,holeX, holeY, 0, -1) 
    vbr = generate_tiles(x, y ,holeX, holeY, 1, -1)
    #generate map
    h_edge = (Fore.WHITE +"#-------#")
    v_edge = (Fore.WHITE + "|")
    player = (Fore.YELLOW + "X")
    vt = f"{v_edge} {vtl} {vtm} {vtr} {v_edge}"
    vm = f"{v_edge} {vml} {player} {vmr} {v_edge}"
    vb = f"{v_edge} {vbl} {vbm} {vbr} {v_edge}"
    v = f" {h_edge}\n {vt}\n {vm}\n {vb}\n {h_edge}"
    game(holeX, holeY, level, v, x, y)

#BACKEND GAME

#generate tile
def generate_tiles(x, y ,holeX, holeY, tileX, tileY):
    cur_tileX = x + tileX
    cur_tileY = y + tileY
    if (cur_tileX == map_width + 1) or (cur_tileX == 0) or (cur_tileY == map_hight + 1) or (cur_tileY == 0):
        return " "
    elif ((cur_tileX == holeX) and (cur_tileY == holeY)):
        return (Fore.LIGHTRED_EX + "0")
    else:
        return (Fore.GREEN + "*")

#FRONTEND GAME

#the game
def game(holeX, holeY, level, v, x, y):
    global tot_moves
    #visuals
    clear_screen()
    print(f"{v}\n", Fore.WHITE + f"Level: {level}\n", Fore.WHITE + f"Position: {x}x, {y}y.\n")
    #game loop
    while True:
        #game movement    
        move = input("Where do you want to move? up/down/left/right? ")
        if move.lower() == "up":
            y += 1
            tot_moves += 1
        elif move.lower() == "down":
            y -= 1
            tot_moves += 1
        elif move.lower() == "left":
            x -= 1
            tot_moves +=1
        elif move.lower() == "right":
            x += 1
            tot_moves += 1
        #check if edge
        if (x > map_width or x <= 0 or y > map_hight or y <= 0):
            game_end_lose()
        #check for hole
        if (holeX == x and holeY == y):
            level += 1
            #check for win
            if level > win_level:
                game_end_win()
            else:
                generate_hole(level, start_X, start_Y)
        #game updating
        generate_map(holeX, holeY, x, y, level)

#AFTER GAME

#end games
def game_end_lose():
    clear_screen()
    print("Oh no. You fell over the edge..\n")
    restart()

def game_end_win():
    clear_screen()
    print("You won!")
    print(f"totalt amount of moves: {tot_moves}")
    restart()

#restart
def restart():
    global tot_moves
    while True:
        restart = input("\nDo you want to restart or quit? (R/Q) \n")
        if restart.upper() == "R":
            tot_moves -= tot_moves
            start()
        elif restart.upper() == "Q":
            clear_screen()
            print("Shuting down game...\n")
            sys.exit()
        else:
            clear_screen()
            print("Invalid comand, please try agian..")

start()