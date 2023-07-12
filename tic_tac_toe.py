"""
2 players should be able to play the game o the same computer
the board should be printed out every time a player makes a move
you should be able to accept input of the player position
"""
import os
import random


# board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def display_board(board):
    print()
    print("+___+___+___+")
    print("|", board[7] + ' | ' + board[8] + " | " + board[9], "|")
    print("+___+___+___+")
    print("|", board[4] + ' | ' + board[5] + " | " + board[6], "|")
    print("+___+___+___+")
    print("|", board[1] + ' | ' + board[2] + " | " + board[3], "|")
    print("+___+___+___+")


def chose_marker():
    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Player 1 chose a marker (X or O): ").upper()
    if marker == "X":
        return "X", "O"
    else:
        return "O", "X"


def place_marker(board, marker, position):
    board[position] = marker


# Clear the console output based on the operating system
def del_output():
    if os.name == 'posix':
        _ = os.system('clear')


def choose_first():
    first = random.randint(0, 1)
    if first == 0:
        return 'Player_1'
    else:
        return 'Player_2'


def win_check(board, mark):
    # if all rows, columns and diagonals share the same marker
    for row in range(1, 10, 3):
        if board[row] == board[row + 1] == board[row + 2] == mark:
            return True
    for col in range(1, 4):
        if board[col] == board[col + 3] == board[col + 6] == mark:
            return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True

    return False


def space_check(board, position):
    return board[position] == ' '


# board is full, then return true
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        try:
            position = int(input('Choose position (1-9): '))
            if position not in range(1, 10):
                print("Invalid input. Enter a number between 1 and 9")
            elif not space_check(board, position):
                print("Position occupied. Please chose another position")
        except ValueError:
            print("This is not a number. Enter a number")

    return position

def play_again():
    choice = input("Play again? (Yes or No): ")
    return choice.lower() == "yes"


# While loop to keep running the game
print("Welcome to TIC TAC TOE")
while True:
    board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    player1_marker, player2_marker = chose_marker()
    turn = choose_first()
    print(turn + ' will move first')
    play_game = input('Ready to play? y or n: ')
    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player_1':
            # show board
            display_board(board)
            # Chose a position on the board
            position = player_choice(board)
            # Place the marker in the position
            place_marker(board, player1_marker, position)
            # Check if they won
            # Check is there is a tie

            # no tie and no win ? then next player turn
            if win_check(board, player1_marker):
                display_board(board)
                print("player one won")
                break
            elif full_board_check(board):
                display_board(board)
                print("Tie Game")
                break
            else:
                turn = "Player_2"
        else:
            # show board
            display_board(board)
            # Chose a position on the board
            position = player_choice(board)
            # Place the marker in the position
            place_marker(board, player2_marker, position)
            # Check if they won
            # Check is there is a tie
            # no tie and no win ? then next player turn
            if win_check(board, player2_marker):
                display_board(board)
                print("player two won")
                break
            elif full_board_check(board):
                display_board(board)
                print("Tie Game")
                break
            else:
                turn = "Player_1"

    if not play_again():
        break
