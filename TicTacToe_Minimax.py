#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
""" CS 335-1 Final Project Tic-Tac-Toe using minimax """
__author__ = "Daniel Choe"

import sys
import random


#Function minimax used for A.I. second player recursively calling
#until outcome of 0, 1 or -1 reached and min value is returned
def minimax(pos, depth, max_Turn):
    outcome = outCome(pos)

    if outcome != 9:
        if outcome == 0:
            value = 0
        elif outcome == 1:
            value = 1
        elif outcome == -1:
            value = -1
        return value

    if max_Turn:
        max_Feedback = float('-inf')

        for a in range(len(pos)):

            if pos[a] != 'O' and pos[a] != 'X':
                hold = pos[a]
                pos[a] = 'X'
                feedback = minimax(pos, depth - 1, False)
                pos[a] = hold
                max_Feedback = max(max_Feedback, feedback)
        return max_Feedback
    else:
        min_Feedback = float('inf')

        for b in range(len(pos)):

            if pos[b] != 'O' and pos[b] != 'X':
                hold2 = pos[b]
                pos[b] = 'O'
                feedback = minimax(pos, depth - 1, True)
                pos[b] = hold2
                min_Feedback = min(min_Feedback, feedback)
        return min_Feedback

    return min_Feedback


#Function minimax2 used for A.I. first player recursively calling
#until outcome of 0, 1 or -1 reached and max value is returned
def minimax2(pos, depth, max_Turn):
    outcome2 = outCome(pos)

    if outcome2 != 9:
        if outcome2 == 0:
            value = 0
        elif outcome2 == 1:
            value = 1
        elif outcome2 == -1:
            value = -1
        return value

    if max_Turn:
        min_Feedback = float('inf')

        for b in range(len(pos)):

            if pos[b] != 'O' and pos[b] != 'X':
                hold2 = pos[b]
                pos[b] = 'O'
                feedback = minimax2(pos, depth - 1, False)
                pos[b] = hold2
                min_Feedback = min(min_Feedback, feedback)
        return min_Feedback
    else:
        max_Feedback = float('-inf')

        for a in range(len(pos)):

            if pos[a] != 'O' and pos[a] != 'X':
                hold = pos[a]
                pos[a] = 'X'
                feedback = minimax2(pos, depth - 1, True)
                pos[a] = hold
                max_Feedback = max(max_Feedback, feedback)
        return max_Feedback

    return max_Feedback



#Function prints the tic-tac-toe grid
def ttt_print(tttp):
    for a in range(len(tttp)):

        if a == 0 or a == 3 or a == 6:

            if a == 3:
                print("_________________")

            print("   " + "  |  " + " " + "  |  " + "   ")
            print("  " + tttp[a] + "  |  " + tttp[a+1] + "  |  " + tttp[a+2] + "  ")
            print("   " + "  |  " + " " + "  |  " + "   ")

            if a == 3:
                print("-----------------")


#Keeps track of available space on the Tic-Tac-Toe board by
#creating a new list with free space counting the length and
#returning that value
def count_Down(tttb):
    list_new = []

    for a in range(len(tttb)):

        if tttb[a] != 'O' and tttb[a] != 'X':
            list_new.append(tttb[a])
    return len(list_new)


#Function will determine a tie,
# win for X or win for O by returning 0, 1 and -1
def outCome(ttt):
    win_condition = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                     [0, 3, 6], [1, 4, 7], [2, 5, 8],
                     [0, 4, 8], [6, 4, 2]]

    count = count_Down(ttt)
    xot = 9

    for a in range(len(win_condition)):

        col_one = win_condition[a][0]
        col_two = win_condition[a][1]
        col_thr = win_condition[a][2]

        if ttt[col_one] == ttt[col_two] and ttt[col_one] == ttt[col_thr]:
            if ttt[col_one] == 'O':
                xot = -1
            elif ttt[col_one] == 'X':
                xot = 1
            return xot
        elif count == 0:
            xot = 0
    return xot


#Function will take in current ai board position and return the optimal
# play by using minimax for player Two A.I..
def ai_Turn(tttg):
    min_fb = float('inf')
    optPlay = 0
    for a in range(len(tttg)):

        if tttg[a] != 'O' and tttg[a] != 'X':
            hold3 = tttg[a]
            tttg[a] = 'O'
            fb = minimax(tttg, count_Down(tttg), True)
            tttg[a] = hold3
            if fb < min_fb:
                min_fb = fb
                optPlay = a
    return optPlay

#Function will take in current ai board position and return the optimal
# play by using minimax2 for player One A.I..
def ai_Turn_fp(tttg):
    max_fb = float('-inf')
    optPlay = 0
    for a in range(len(tttg)):

        if tttg[a] != 'O' and tttg[a] != 'X':
            hold4 = tttg[a]
            tttg[a] = 'X'
            fbm = minimax2(tttg, count_Down(tttg), True)
            tttg[a] = hold4
            if fbm > max_fb:
                max_fb = fbm
                optPlay = a
    return optPlay


#Function is main, choice two is human vs A.I., choice three and four
#are A.I. vs A.I.
def option_Play(t_i):
    xpOne = True
    conclusion = False
    ttt_grid = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    if t_i == "start":
        choice = input("\nEnter 1 to play Against A.I."
                       "\nEnter 2 for A.I. Against A.I."
                       "\nEnter 3 for first A.I. choose first randomly"
                       "\nAgainst A.I. : ")
        print()

    if t_i == "help":
        print("How to play Tic-Tac-Toe.")
        print()
        print("The goal of the game is for players to position their marks"
              "\nso that they make a continuous line of three cells vertically,"
              "\nhorizontally, or diagonally.")
        print()
        print("Tic-Tac-Toe board has numbers 0 - 8. Human player is X and A.I. is O."
              "\nwhen prompted type in the box number you wish to occupy and press"
              "\nEnter")
        print()
        print("You can also have the computer play against each other once you start"
              "\nthe program. When you run the computer vs. computer simulation it will"
              "\nprint out the board and all the moves made by both A.I. players.")
        print()
        print("If you are using python version 2 input this in your terminal:")
        print()
        print("python2 final_project.py start")
        print()
        print("If you are using python version 3 input this in your terminal:")
        print()
        print("python3 final_project.py start")
        print()

    elif choice == "1":
        print("(X) = Player Against (O) = A.I.")
        print()
        ttt_print(ttt_grid)
        print()

        pick = int(input("Pick number and press Enter: "))
        print()
        while xpOne:
            if pick > 8 or pick < 0:
                pick = input("Not a valid entry, please try again: ")
                print()
            else:
                print("You chose box number: " + str(pick))
                print()
                ttt_grid[pick] = 'X'
                ttt_print(ttt_grid)
                print()
                xpOne = False

        ai = True
        while not conclusion:
            txo = outCome(ttt_grid)

            if txo == 1:
                conclusion = True
                print("You won, congrats !")
                print()
            elif txo == -1:
                conclusion = True
                print("I am Hal the A.I. and I won !")
                print()
            elif txo == 0:
                conclusion = True
                print("  It's a tie !")
                print()
            else:
                if ai:
                    ait = ai_Turn(ttt_grid)
                    ttt_grid[ait] = 'O'
                    print("A.I. (O)\nchose box number:" + str(ait))
                    print()
                    ttt_print(ttt_grid)
                    print()
                    ai = False
                else:
                    p_turn = int(input("  Your turn: "))
                    print()
                    ttt_grid[p_turn] = 'X'
                    ttt_print(ttt_grid)
                    print()
                    ai = True


    elif choice == "2":
        print("Cyberdyne A.I. against Cyberdyne A.I.")
        print("(X) = T1000 against (O) = T800")
        print("Both A.I. Independent")
        print()
        ttt_print(ttt_grid)
        print()
        t1000 = True

        while not conclusion:
            xto = outCome(ttt_grid)

            if xto == 1:
                conclusion = True
                print("T1000 wins !")
                print()
            elif xto == -1:
                conclusion = True
                print("T800 wins !")
                print()
            elif xto == 0:
                conclusion = True
                print("We are evenly matched !")
                print()
            else:
                if t1000:
                    tron2 = ai_Turn_fp(ttt_grid)
                    ttt_grid[tron2] = 'X'
                    print("T1000 move (X) \nchose grid number: " + str(tron2))
                    ttt_print(ttt_grid)
                    print()
                    t1000 = False
                else:
                    tron = ai_Turn(ttt_grid)
                    ttt_grid[tron] = 'O'
                    print("T800 move (O) \nchose grid number: " + str(tron))
                    ttt_print(ttt_grid)
                    print()
                    t1000 = True


    elif choice == "3":
        print("A.I. against A.I.")
        print("(X) = first choice picked randomly")
        print("Both A.I. independent")
        print()
        ttt_print(ttt_grid)
        print()
        t1000 = False
        a = random.randint(0,8)
        ttt_grid[a] = 'X'
        print("Randomly picked (X)")
        ttt_print(ttt_grid)
        print()
        while not conclusion:
            xto = outCome(ttt_grid)

            if xto == 1:
                conclusion = True
                print("First A.I. wins !")
                print()
            elif xto == -1:
                conclusion = True
                print("Second A.I. wins !")
                print()
            elif xto == 0:
                conclusion = True
                print("  It's a tie !")
                print()
            else:
                if t1000:
                    tron2 = ai_Turn_fp(ttt_grid)
                    ttt_grid[tron2] = 'X'
                    print("First A.I. (X) \nchose grid number: " + str(tron2))
                    ttt_print(ttt_grid)
                    print()
                    t1000 = False
                else:
                    tron = ai_Turn(ttt_grid)
                    ttt_grid[tron] = 'O'
                    print("Second A.I. (O) \nchose grid number: " + str(tron))
                    ttt_print(ttt_grid)
                    print()
                    t1000 = True

    else:
        print("Sorry, wrong input. We can't play. I need to be restarted")


if __name__ == "__main__":
    terminal_input = sys.argv[1]
    option_Play(terminal_input)

