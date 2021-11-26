import random

board = [" " for _ in range(9)]

players = ["X", "O"]
turn = 0

def main():
    draw_instructions()
    while not check_win():
        if (turn == 0) :
            move = int(input(f"{players[turn]}'s turn\nEnter a move: "))
            if not make_move(move):
                continue
        else:
            # Temporary random opponent
            print(f"{players[turn]}'s turn\nEnter a move: ")
            r = random.randint(0, 8)
            while (board[r] == " "):
                r = random.randint(0, 8)
            make_move(r)
        draw_board()

def make_move(move):
    if board[move - 1] != " ":
        print("Already taken!\n")
        return False
    global turn
    board[move - 1] = players[turn]
    turn = (turn + 1) % 2
    return True

def check_win():
    if board[0] == board[1] == board[2] and board[0] != " ":
        print_winner()
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        print_winner()
        return True
    elif board[6] == board[7] == board[8] and board[7] != " ":
        print_winner()
        return True

    if board[0] == board[3] == board[6] and board[0] != " ":
        print_winner()
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        print_winner()
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        print_winner()
        return True
    
    if board[0] == board[4] == board[8] and board[0] != " ":
        print_winner()
        return True
    elif board[2] == board[4] == board[6] and board[2] != " ":
        print_winner()
        return True
    
    for i in range(9):
        if board[i] == " ":
            return False
    print("There was a tie!")
    return True

def print_winner():
    print(f"{players[(turn - 1) % 2]} won!")

def draw_board():
    print()
    for i in range(3):
        print(" " + str(board[0 + i*3]) + "  |  " + str(board[1 + i*3]) + "  |  " + str(board[2 + i*3]))
        if i == 2:
            print()
            return
        print("- " * 8)

def draw_instructions():
    print("\n 1  |  2  |  3 ")
    print("- " * 8)
    print(" 4  |  5  |  6 ")
    print("- " * 8)
    print(" 7  |  8  |  9 \n")

main()