import random
import math

def conflicts(board):
    count = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if abs(board[i] - board[j]) == abs(i - j):
                count += 1
    return count

board = [random.randint(0, 7) for _ in range(8)]
T = 100
alpha = 0.99
step = 1

print("Initial Board:", board)
print("Initial Conflicts:", conflicts(board))

while T > 0.1:
    cost = conflicts(board)

    if cost == 0:
        break

    new_board = board[:]
    col = random.randint(0, 7)
    new_board[col] = random.randint(0, 7)

    new_cost = conflicts(new_board)
    delta = new_cost - cost

    if delta <= 0 or random.random() < math.exp(-delta / T):
        board = new_board
        print("Step", step, "Board:", board,
              "Conflicts:", new_cost)
    else:
        print("Step", step, "Move rejected")

    T *= alpha
    step += 1

print("\nFinal Board:", board)
print("Final Conflicts:", conflicts(board))

if conflicts(board) == 0:
    print("Solution Found!")
else:
    print("Solution Not Found!")
