def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = []

    if row > 0:
        moves.append(zero - 3)

    if row < 2:
        moves.append(zero + 3)

    if col > 0:
        moves.append(zero - 1)

    if col < 2:
        moves.append(zero + 1)

    for new_zero in moves:
        new_state = list(state)
        new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
        neighbors.append(tuple(new_state))

    return neighbors


def depth_limited_search(state, goal, depth, path, visited):
    if state == goal:
        return path

    if depth == 0:
        return None

    visited.add(state)

    for new_state in get_neighbors(state):
        if new_state not in visited:
            result = depth_limited_search(
                new_state,
                goal,
                depth - 1,
                path + [new_state],
                visited
            )

            if result is not None:
                return result

    visited.remove(state)
    return None


def iddfs(start, goal, max_depth=50):
    for depth in range(max_depth + 1):
        visited = set()

        result = depth_limited_search(
            start,
            goal,
            depth,
            [start],
            visited
        )

        if result is not None:
            return result

    return None


def print_state(state):
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()


start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

solution = iddfs(start, goal)

if solution:
    print("Solution found!")
    print("Moves:", len(solution) - 1)
    print()

    for state in solution:
        print_state(state)
else:
    print("No solution found!")
