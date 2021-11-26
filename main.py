import random

players = ["X", "O"]
turn = 0

class Board:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def make_move(self, move):
        if self.board[move - 1] != " ":
            print("Already taken!\n")
            return False
        global turn
        self.board[move - 1] = players[turn]
        turn = (turn + 1) % 2
        return True
    
    def is_cell_empty(self, cell):
        return self.board[cell] == " "

    def check_win(self):
        for i in range(3):
            if self.board[0 + i*3] == self.board[1 + i*3] == self.board[2 + i*3] and self.board[0 + i*3] != " ":
                print_winner()
                return True
        for j in range(3):
            if self.board[j] == self.board[j + 3] == self.board[j + 6] and self.board[j] != " ":
                print_winner()
                return True
        
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != " ":
            print_winner()
            return True
        elif self.board[2] == self.board[4] == self.board[6] and self.board[2] != " ":
            print_winner()
            return True
        
        if not self.check_filled():
            return False
        print("This game was a tie!")
        return True
    
    def check_filled(self):
        for i in range(9):
            if self.board[i] == " ":
                return False
        return True

    def draw_board(self):
        print()
        for i in range(3):
            print(" " + str(self.board[0 + i*3]) + "  |  " + str(self.board[1 + i*3]) + "  |  " + str(self.board[2 + i*3]))
            if i == 2:
                print()
                return
            print("- " * 8)

class AI:
    def evaluate(self, board):
        for i in range(3):
            if board[0 + i*3] == board[1 + i*3] == board[2 + i*3] and board[0 + i*3] != " ":
                if board[0 + i*3] == players[turn]:
                    return 10
                else:
                    return -10
        for j in range(3):
            if board[j] == board[j + 3] == board[j + 6] and board[j] != " ":
                if board[j] == players[turn]:
                    return 10
                else:
                    return -10
        
        if board[0] == board[4] == board[8] and board[0] != " ":
            if board[0] == players[turn]:
                return 10
            else:
                return -10
        elif board[2] == board[4] == board[6] and board[2] != " ":
            if board[2] == players[turn]:
                return 10
            else:
                return -10
        return 0

    def minimax(self, board, depth, is_max_player):
        score = self.evaluate(board)

        if score == 10:
            return score
        if score == -10:
            return score
        
        if self.is_full(board):
            return 0
        
        if is_max_player:
            best = -1000
            for i in range(9):
                if board[i] == " ":
                    board[i] = players[turn]
                    best = max(best, self.minimax(board, depth + 1, not is_max_player))
                    board[i] = " "
            return best
        
        if not is_max_player:
            best = 1000
            for i in range(9):
                if board[i] == " ":
                    board[i] = players[(turn + 1) % 2]
                    best = min(best, self.minimax(board, depth + 1, not is_max_player))
                    board[i] = " "
            return best

    def find_best_move(self, board):
        bestVal = -1000
        bestMove = -1
        for i in range(9):
            if board[i] == " ":
                board[i] = players[turn]
                eval = self.minimax(board, 0, False)
                board[i] = " "
                if (eval > bestVal):
                    bestVal = eval
                    bestMove = i + 1
        return bestMove
    
    def is_full(self, board):
        for i in range(9):
            if board[i] == " ":
                return False
        return True

def main():
    b = Board()
    ai = AI()
    draw_instructions()
    while not b.check_win():
        if (turn == 0) :
            move = int(input(f"{players[turn]}'s turn\nEnter a move: "))
            if not b.make_move(move):
                continue
        else:
            b.make_move(ai.find_best_move(b.board))
        b.draw_board()

def print_winner():
    print(f"{players[(turn - 1) % 2]} won!")

def draw_instructions():
    print("\n 1  |  2  |  3 ")
    print("- " * 8)
    print(" 4  |  5  |  6 ")
    print("- " * 8)
    print(" 7  |  8  |  9 \n")

main()