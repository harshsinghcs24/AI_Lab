board = [" " for _ in range(9)]

def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False

def board_full():
    return " " not in board

def computer_move():
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner("O"):
                return i
            board[i] = " "

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner("X"):
                board[i] = "O"
                return i
            board[i] = " "

    if board[4] == " ":
        board[4] = "O"
        return 4

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return i

print("TIC-TAC-TOE")
print("You are X")
print("Computer is O")

display_board()

while True:
    try:
        position = int(input("Enter position (1-9): "))
    except ValueError:
        print("Invalid move. Try again.")
        continue

    if position < 1 or position > 9:
        print("Invalid move. Try again.")
        continue

    index = position - 1

    if board[index] != " ":
        print("Invalid move. Try again.")
        continue

    board[index] = "X"
    display_board()

    if check_winner("X"):
        print("You win!")
        break

    if board_full():
        print("Draw!")
        break

    computer_position = computer_move()

    print("Computer chose position:", computer_position + 1)
    display_board()

    if check_winner("O"):
        print("Computer wins!")
        break

    if board_full():
        print("Draw!")
        break



