#!/usr/bin/python3
with open('input.txt', 'r') as file:
    seat_map = file.read()

line_count = 0
row_index = 0
row_seats = {}
row_seats_upper = {}
seats = []

for char in seat_map:
    if char == '\n':
        line_count += 1
        row_index = 0
        row_seats_upper = row_seats
        row_seats = {}
    elif char == 'L':
        seat = {
            "occupied": [False, False],
            "neighbors": []
        }

        seats.append(seat)
        row_seats[row_index] = seat

        potential_neighbors = [
            row_seats.get(row_index - 1, None),
            row_seats_upper.get(row_index - 1, None),
            row_seats_upper.get(row_index, None),
            row_seats_upper.get(row_index + 1, None)
        ]

        for potential_neighbor in potential_neighbors:
            if potential_neighbor != None:
                seat["neighbors"].append(potential_neighbor)
                potential_neighbor["neighbors"].append(seat)

        row_index += 1
    else:
        row_index += 1

seat_changed = True
filled_seat_count = 0

while seat_changed:
    seat_changed = False

    for seat in seats:
        seat_occupied = seat["occupied"]

        adjacent_seat_count = 0

        for neighbor in seat["neighbors"]:
            if neighbor["occupied"][0]:
                adjacent_seat_count += 1
                if adjacent_seat_count >= 4:
                    break

        if adjacent_seat_count >= 4 and seat_occupied[0]:
            filled_seat_count -= 1
            seat_changed = True
            seat_occupied[1] = False
        elif adjacent_seat_count == 0 and not seat_occupied[0]:
            filled_seat_count += 1
            seat_changed = True
            seat_occupied[1] = True

    for seat in seats:
        seat_occupied = seat["occupied"]
        seat_occupied[0] = seat_occupied[1]

print(filled_seat_count)
