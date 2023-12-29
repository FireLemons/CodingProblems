#!/usr/bin/python3

input = open("input.txt", "r")

highest_seat_id = -1
lowest_seat_id = float('inf')
my_seat_id = 0

for line in input:
    row = line[:7].replace("B", "1").replace("F", "0")
    column = line[7:10].replace("R", "1").replace("L", "0")

    seat_id = int(row + column, 2)
    my_seat_id ^= seat_id

    highest_seat_id = max(highest_seat_id, seat_id)
    lowest_seat_id = min(lowest_seat_id, seat_id)

i = 2047
while i > highest_seat_id:
    my_seat_id ^= i 
    i -= 1

i = 0
while i < lowest_seat_id:
    my_seat_id ^= i
    i += 1

if my_seat_id < 0:
    my_seat_id = ~my_seat_id

print(my_seat_id)
