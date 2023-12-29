#!/usr/bin/python3

input = open("input.txt", "r")

highest_seat_id = -1

for line in input:
    row = line[:7].replace("B", "1").replace("F", "0")
    column = line[7:10].replace("R", "1").replace("L", "0")
    highest_seat_id = max(highest_seat_id, int(row + column, 2))

print(highest_seat_id)
