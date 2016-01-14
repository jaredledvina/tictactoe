
def welcome():
    text = """
Welcome to Tic Tac Toe!
Directions:
Enter the position you want to take.
Board positions are numbers 0-8 as shown below.
    """
    print(text)
    print_board(generate_positions())

def generate_positions():
    return [str(num) for num in range(9)]

def print_board(status):
    def print_line():
        print("- " * 5)

    print(' | '.join(status[0:3]))
    print_line()
    print(' | '.join(status[3:6]))
    print_line()
    print(' | '.join(status[6:9]))
    print()

def game_step(turn, status):
    if turn % 2 == 0:
        position = input("Player 1 (X): ")
        player_token = "X"
    else:
        position = input("Player 2 (O): ")
        player_token = "O"
    
    try: 
        status[int(position)] = player_token
        print()
    except (ValueError, IndexError):
        game_step(turn, status)

    if winner(player_token, status):
        print_board(status)
        game_done(player_token)
        if input("Would you like to play again? y/n ") == 'y':
            game_main()
        else: exit()

def squares_finished(status):
    if " " not in status:
        return True
    return False

def winner(player_token, status):
    winning_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]]
    for entry in winning_combinations:
        if all(status[each] == player_token for each in entry):
            return True
    return False

def game_done(player_token):
    print("Congrats", player_token, "you win!")


def game_main():
    status = [" " for _ in range(9)]
    turn = 0

    welcome()
    print_board(status)

    while True:
        game_step(turn, status)
        print_board(status)
        turn += 1
        if squares_finished(status):
            break

if __name__ == '__main__':
    game_main()
