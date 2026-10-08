import heapq

initial = (
    (2, 8, 3),
    (1, 6, 4),
    (7, 0, 5)
)

goal = (
    (1, 2, 3),
    (8, 0, 4),
    (7, 6, 5)
)

def misplaced_tiles(state, goal):
    count = 0

    for i in range(3):
        for j in range(3):
            # Ignore blank tile (0)
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1

    return count

def manhattan_distance(state, goal):
    distance = 0

    for i in range(3):
        for j in range(3):
            tile = state[i][j]

            # Ignore blank tile
            if tile == 0:
                continue

            # Find goal position of the tile
            for x in range(3):
                for y in range(3):
                    if goal[x][y] == tile:
                        distance += abs(i - x) + abs(j - y)

    return distance

def get_neighbors(state):

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                row, col = i, j

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_state = [list(r) for r in state]

            new_state[row][col], new_state[new_row][new_col] = \
                new_state[new_row][new_col], new_state[row][col]

            new_state = tuple(tuple(r) for r in new_state)

            neighbors.append(new_state)

    return neighbors

def print_state(state):

    for row in state:
        print(" ".join("_" if x == 0 else str(x) for x in row))

    print()

def a_star(initial, goal, heuristic):

    open_list = []

    h = heuristic(initial, goal)
    g = 0
    f = g + h

    heapq.heappush(open_list, (f, g, initial, [initial]))

    visited = {}

    while open_list:

        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, g

        if current in visited and visited[current] <= g:
            continue

        visited[current] = g

        for neighbor in get_neighbors(current):

            new_g = g + 1
            h = heuristic(neighbor, goal)
            new_f = new_g + h

            new_path = path + [neighbor]

            heapq.heappush(
                open_list,
                (new_f, new_g, neighbor, new_path)
            )

    return None, -1


print("======================================")
print("CASE 1: TILES OUT OF PLACE")
print("======================================")

path, moves = a_star(
    initial,
    goal,
    misplaced_tiles
)

if path:
    print("Solution found!")
    print("Number of moves:", moves)
    print()

    for i, state in enumerate(path):
        print("State", i)
        print_state(state)

        g = i
        h = misplaced_tiles(state, goal)
        f = g + h

        print("g(n) =", g)
        print("h(n) =", h)
        print("f(n) =", f)
        print("--------------------------------")

print("\n======================================")
print("CASE 2: MANHATTAN DISTANCE")
print("======================================")

path, moves = a_star(
    initial,
    goal,
    manhattan_distance
)

if path:
    print("Solution found!")
    print("Number of moves:", moves)
    print()

    for i, state in enumerate(path):
        print("State", i)
        print_state(state)

        g = i
        h = manhattan_distance(state, goal)
        f = g + h

        print("g(n) =", g)
        print("h(n) =", h)
        print("f(n) =", f)
        print("--------------------------------")
