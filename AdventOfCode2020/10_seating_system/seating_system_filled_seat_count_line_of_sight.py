#!/usr/bin/python3
with open('input.txt', 'r') as file:
    seat_map = file.read()

all_seats = {}
closest_northern_seats = {}
closest_west_seat = None
line_count = 0
line_length = seat_map.find('\n')
row_index = 0

for char in seat_map:
    if char == '\n':
        closest_west_seat = None
        line_count += 1
        row_index = 0
    elif char == 'L':
        seat = {
            "occupied": [False, False],
            "neighbors": []
        }

        all_seats[f'{row_index},{line_count}'] = seat

        potential_neighbors = [
            closest_west_seat,
            closest_northern_seats.get(row_index, None),
        ]

        closest_northern_seats[row_index] = seat
        closest_west_seat = seat

        for i in range(min(line_count, row_index)):
            potential_top_left_neighbor = all_seats.get(f'{row_index - (1 + i)},{line_count - (1 + i)}', None)
            if potential_top_left_neighbor != None:
                potential_neighbors.append(potential_top_left_neighbor)
                break

        for i in range(min(line_count, line_length - (row_index + 1))):
            potential_top_right_neighbor = all_seats.get(f'{row_index + i + 1},{line_count - (i + 1)}', None)
            if potential_top_right_neighbor != None:
                potential_neighbors.append(potential_top_right_neighbor)
                break

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

    for seat in all_seats.values():
        seat_occupied = seat["occupied"]

        adjacent_seat_count = 0

        for neighbor in seat["neighbors"]:
            if neighbor["occupied"][0]:
                adjacent_seat_count += 1
                if adjacent_seat_count >= 5:
                    break

        if adjacent_seat_count >= 5 and seat_occupied[0]:
            filled_seat_count -= 1
            seat_changed = True
            seat_occupied[1] = False
        elif adjacent_seat_count == 0 and not seat_occupied[0]:
            filled_seat_count += 1
            seat_changed = True
            seat_occupied[1] = True

    for seat in all_seats.values():
        seat_occupied = seat["occupied"]
        seat_occupied[0] = seat_occupied[1]

print(filled_seat_count)
