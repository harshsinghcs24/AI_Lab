def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        zero = state.index(0)
        row = zero // 3
        col = zero % 3

        moves = []

        if row > 0:
            moves.append(-3)

        if row < 2:
            moves.append(3)

        if col > 0:
            moves.append(-1)

        if col < 2:
            moves.append(1)

        for move in moves:
            new_zero = zero + move
            new_state = list(state)

            new_state[zero], new_state[new_zero] = (
                new_state[new_zero],
                new_state[zero]
            )

            new_state = tuple(new_state)

            if new_state not in visited:
                stack.append((new_state, path + [new_state]))

    return None


def print_state(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solution = dfs(start, goal)

if solution:
    print("Solution found!")
    print("Moves:", len(solution) - 1)
    print()

    for state in solution:
        print_state(state)
else:
    print("No solution found!")
