def same(x, y, z):
    if x == y and x == z and x != ' ':
        return True
    return False

def check_winner(board):
    for i in range(3):
        if same(board[i][0], board[i][1], board[i][2]):
            return 2 if board[i][0] == 'X' else -2
    for i in range(3):
        if same(board[0][i], board[1][i], board[2][i]):
            return 2 if board[0][i] == 'X' else -2
    if same(board[0][0], board[1][1], board[2][2]):
        return 2 if board[0][0] == 'X' else -2
    if same(board[2][0], board[1][1], board[0][2]):
        return 2 if board[2][0] == 'X' else -2
    tie = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                tie = False
    if tie:
        return 0
    return 1

def draw_board(board):
    for i in range(3):
        for j in range(3):
            print(f"| {board[i][j]} |", end="")
        print("\n -------------- ")

def minimax(board, depth, is_maximizing, first_time=True):
    result = check_winner(board)
    if depth == 0 or result != 1:
        return result

    if is_maximizing:
        final_score = -10
        final_i, final_j = -1, -1
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth - 1, False, False)
                    board[i][j] = ' '
                    if score > final_score:
                        final_score = score
                        final_i, final_j = i, j
                    if first_time:
                        print(f"score,{i},{j}: {score}")
        if first_time:
            board[final_i][final_j] = 'O'
        return final_score
    else:
        final_score = 10
        final_i, final_j = -1, -1
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth - 1, True, False)
                    board[i][j] = ' '
                    if score < final_score:
                        final_score = score
                        final_i, final_j = i, j
                    if first_time:
                        print(f"score,{i},{j}: {score}")
        if first_time:
            board[final_i][final_j] = 'O'
        return final_score

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    has_winner = False
    player = 'X'
    while not has_winner:
        draw_board(board)
        if player == 'X':
            print("Player X's turn:")
            valid_move = False
            while not valid_move:
                try:
                    x, y = map(int, input("Enter your move (row and column): ").split())
                    if 0 <= x < 3 and 0 <= y < 3:
                        if board[x][y] == ' ':
                            board[x][y] = 'X'
                            has_winner = check_winner(board) != 1
                            valid_move = True 
                            player = 'O' 
                        else:
                            print("The field is not empty. Try again.")
                    else:
                        print("Invalid input. Coordinates must be between 0 and 2. Try again.")
                except ValueError:
                    print("Invalid input. Please enter two integers separated by a space. Try again.")
        else:
            print("Player O's turn:")
            minimax(board, 100, False)
            has_winner = check_winner(board) != 1
            player = 'X'

    result = check_winner(board)
    draw_board(board)
    if result == 0:
        print("Tie")
    else:
        print("X player wins" if result == 2 else "O player wins")

if __name__ == "__main__":
    main()
