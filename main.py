# import only system from os
import os


board = {}
for i in range(1, 10):
    board[i] = "-"


# def clear():
#     print(name)
#     # for windows
#     if name == 'nt':
#         system('cls')
#
#     # for mac and linux(here, os.name is 'posix')
#     else:
#         system('clear')


def print_board():
    os.system("clear")
    for j in [1, 4, 7]:
        print(f"|{board[j]}|{board[j + 1]}|{board[j + 2]}|")


def player_input(player, location):
    result = False
    try:
        loc = int(location)
    except ValueError:
        print("Incorrect")
        return result

    is_incorrect = not (loc in range(1, 10))

    if is_incorrect:
        print("Incorrect")
        return result

    is_occupied = not (board[loc] == "-")
    if is_occupied:
        print("Occupied")
        return result

    if player == 1:
        symbol = "o"
    else:
        symbol = "x"
    board[loc] = symbol
    return True


def board_check():
    result = False
    initial = "-"
    # horizontal
    h1 = [board[1], board[2], board[3]]
    h2 = [board[4], board[5], board[6]]
    h3 = [board[7], board[8], board[9]]
    # vertical
    v1 = [board[1], board[4], board[7]]
    v2 = [board[2], board[5], board[8]]
    v3 = [board[3], board[6], board[9]]
    # slant
    s1 = [board[1], board[5], board[9]]
    s2 = [board[3], board[5], board[7]]

    pattern_list = [h1, h2, h3, v1, v2, v3, s1, s2]
    for pattern in pattern_list:
        is_default_not_exist = not(initial in pattern)
        is_all_same = all(value == pattern[0] for value in pattern)
        #print(f"{pattern} {is_default_not_exist} {is_all_same}")
        if is_default_not_exist and is_all_same:
            result = True
            print("Game Over")
    return result


is_playing = True
current_player = 1
move_ctr = 0


while is_playing:

    while True:
        player_choice = input(f"[Player{current_player}] Enter Location (1-9)")
        if player_input(current_player, player_choice):
            break

    print_board()

    if board_check() or move_ctr > 9:
        is_playing = False
        print(f"Player {current_player} Wins!")

    if current_player == 1:
        current_player = 2
    else:
        current_player = 1
    move_ctr += 1
