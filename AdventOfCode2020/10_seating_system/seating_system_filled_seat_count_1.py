from copy import deepcopy

directions = [(-1, -1), (0, -1), (1, -1), (-1, 0),
              (1, 0), (-1, 1), (0, 1), (1, 1)]


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


def part_one(seats):
    stabilized = True
    next_seats = deepcopy(seats)
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            seat = seats[row][col]
            if seat == "L":
                should_become_occupied = True
                for direction in directions:
                    try:
                        if row + direction[0] >= 0 and col + direction[1] >= 0:
                            if seats[row + direction[0]][col + direction[1]] == '#':
                                should_become_occupied = False
                    except IndexError:
                        continue
                if should_become_occupied:
                    stabilized = False
                    next_seats[row][col] = '#'
            if seat == '#':
                occupied_neighbors = 0
                for direction in directions:
                    try:
                        if row + direction[0] >= 0 and col + direction[1] >= 0:
                            if seats[row + direction[0]][col + direction[1]] == '#':
                                occupied_neighbors += 1
                    except IndexError:
                        continue
                if occupied_neighbors >= 4:
                    stabilized = False
                    next_seats[row][col] = 'L'
    if not stabilized:
        return part_one(next_seats)
    else:
        total = 0
        for row in next_seats:
            for seat in row:
                if seat == "#":
                    total += 1
        return total

with open("input.txt") as f:
    seats = []
    for line in f:
        seats.append([char for char in line.strip()])
    print(part_one(seats))
