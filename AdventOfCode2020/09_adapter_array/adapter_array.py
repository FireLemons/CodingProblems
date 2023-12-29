#!/usr/bin/python3
import bisect

input_numbers = open("input.txt", "r")
sorted_numbers = []

for x in input_numbers:
    bisect.insort(sorted_numbers, int(x))

sorted_numbers.insert(0, 0)
sorted_numbers.append(sorted_numbers[len(sorted_numbers) - 1] + 3)

delta_1_count = 0
delta_3_count = 0

for x in range(len(sorted_numbers) - 1):
    delta = sorted_numbers[x + 1] - sorted_numbers[x]
    if delta == 1:
        delta_1_count += 1
    elif delta == 3:
        delta_3_count += 1

print(delta_1_count * delta_3_count)
