states = {
    1: ["A", "Dirty", "Dirty"],
    2: ["B", "Dirty", "Dirty"],
    3: ["A", "Clean", "Dirty"],
    4: ["B", "Dirty", "Clean"],
    5: ["A", "Dirty", "Clean"],
    6: ["B", "Clean", "Dirty"],
    7: ["A", "Clean", "Clean"],
    8: ["B", "Clean", "Clean"]
}

state = int(input("Enter initial state (1-8): "))

position, room_a, room_b = states[state]

print("\nInitial State:", state)
print("Vacuum Position:", position)
print("Room A:", room_a)
print("Room B:", room_b)

while room_a == "Dirty" or room_b == "Dirty":

    if position == "A":
        if room_a == "Dirty":
            print("\nAction: SUCK")
            room_a = "Clean"
        else:
            print("\nAction: MOVE RIGHT")
            position = "B"

    else:
        if room_b == "Dirty":
            print("\nAction: SUCK")
            room_b = "Clean"
        else:
            print("\nAction: MOVE LEFT")
            position = "A"

    print("Vacuum Position:", position)
    print("Room A:", room_a)
    print("Room B:", room_b)

print("\nBoth rooms are clean.")
print("Goal state reached.")