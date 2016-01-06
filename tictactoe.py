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
        player_token = "X"
    else:
        position = input("Player 2 (O): ")
        player_token = "O"
    status[int(position)] = player_token
    if winner(player_token):
        game_done(player_token)

def squares_finished():
    if " " in status:
        return False
    else:
        return True

def winner(player_token):
    winning_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]]
    for entry in winning_combinations:
        if all(status[each] == player_token for each in entry):
            return True
    return False

def game_done(player_token):
    print("Congrats", player_token, "you win!")

create_game()
welcome()
print_board()

while True:
    game_step(turn)
    print_board()
    turn += 1
    if squares_finished():
        break
