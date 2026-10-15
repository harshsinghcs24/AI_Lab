import random

def calculate_cost(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):

            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def generate_neighbors(board):
    neighbors = []
    n = len(board)
    for col in range(n):
        for row in range(n):
            if board[col] != row:
                new_board = board.copy()
                new_board[col] = row
                neighbors.append(new_board)
    return neighbors

def hill_climbing(n):
    while True:

        board = [random.randint(0, n - 1) for _ in range(n)]
        
        while True:
            current_cost = calculate_cost(board)
            if current_cost == 0:
                return board
            
            neighbors = generate_neighbors(board)
            if not neighbors:
                break
             
            best_board = min(neighbors, key=calculate_cost)
            best_cost = calculate_cost(best_board)
            
            if best_cost < current_cost:
                board = best_board
            else:
             
                break 

def display_board(board):
    n = len(board)
    for row in range(n):
        for col in range(n):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter value for n : "))
    solution = hill_climbing(n)
    
    print("\nSolution Found!")
    print("Final Board:")
    display_board(solution)
    print("Number of attacking pairs:", calculate_cost(solution))
