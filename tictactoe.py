status = []
turn = 0

def create_game():
    status[:] = []
    for _ in range(9):
        status.append(" ")

def welcome():
    print("Welcome to Tic Tac Toe!")
    print("Directions:")
    print("Enter the position you want to take.")
    print()
    print("Board positions are numbers 0-8 as shown below.")
    generate_positions()
    print_board()
    create_game()

def generate_positions():
    status[:] = []
    for item in range(9):
        status.append(str(item))

def print_board():
    print()
    print(' | '.join(status[0:3]))
    print("- - - - -")
    print(' | '.join(status[3:6]))
    print("- - - - -")
    print(' | '.join(status[6:9]))
    print()

def game_step(turn):
    if turn % 2 == 0:
        position = input("Player 1 (X): ")
        value = "X"
    else:
        position = input("Player 2 (O): ")
        value = "O"
    status[int(position)] = value

def squares_finished():
    if " " in status:
        return False
    else:
        return True

def x_win():
    return False

def o_win():
    return False

def game_done():
    # if:
        # Any of these are true:
        # squares_finished()
        # Check for adjacency among Xs
        # Check for adjacency among Os
        # Return False
    return True

create_game()
welcome()
print_board()

while True:
    game_step(turn)
    print_board()
    turn += 1
    if squares_finished():
        break
