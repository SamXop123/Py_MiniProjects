def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row = int(input(f"Player {player}, enter row (1-3): ")) - 1
        col = int(input(f"Player {player}, enter column (1-3): ")) - 1

        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("This position is already taken. Try again.")
            continue

        print_board(board)

        if check_winner(board):
            print(f"Player {player} wins!")
            break
        elif " " not in [cell for row in board for cell in row]:
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()

