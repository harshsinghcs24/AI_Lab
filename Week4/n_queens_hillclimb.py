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
    restart_count = 1
    while True:

        board = [random.randint(0, n - 1) for _ in range(n)]
        print(f"\n--- [Attempt #{restart_count}] Starting with Initial Board: {board} (h={calculate_cost(board)}) ---")
        
        step = 1
        while True:
            current_cost = calculate_cost(board)
            if current_cost == 0:
                print(f"  └─ Success! Found optimal solution at Step {step-1}.")
                return board
            
            neighbors = generate_neighbors(board)
            if not neighbors:
                break
             
            best_board = min(neighbors, key=calculate_cost)
            best_cost = calculate_cost(best_board)
            
            if best_cost < current_cost:
                print(f"  Step {step}: Moved to {best_board} (h dropped from {current_cost} -> {best_cost})")
                board = best_board
                step += 1
            else:
                
                print(f"  └─ Stuck in Local Minimum at {board} (h={current_cost}). Restarting...")
                restart_count += 1
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
    
    print("\n==============================")
    print("FINAL RESULT FOUND!")
    print("==============================")
    print(f"Array State: {solution}")
    print(f"Number of attacking pairs (h): {calculate_cost(solution)}")
    print("\nVisual Board Layout:")
    display_board(solution)
