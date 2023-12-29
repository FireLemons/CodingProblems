#!/usr/bin/python3
import bisect

input_numbers = open("input.txt", "r")
sorted_numbers = []

for x in input_numbers:
    bisect.insort(sorted_numbers, int(x))

sorted_numbers.insert(0, 0)
sorted_numbers.append(sorted_numbers[len(sorted_numbers) - 1] + 3)

computed = {}

i = 1
while sorted_numbers[i + 1] - sorted_numbers[i - 1] > 3:
    i += 1

def permutation_count(first_elem: int, starting_index: int):
    if (starting_index == len(sorted_numbers) - 1):
        return 1
    elif (f'{first_elem}, {starting_index}' in computed):
        return computed[f'{first_elem}, {starting_index}']
    else:
        result = 0

        if (sorted_numbers[starting_index + 1] - first_elem <= 3):
            result = permutation_count(first_elem, starting_index + 1) + permutation_count(sorted_numbers[starting_index], starting_index + 1)
        else:
            result = permutation_count(sorted_numbers[starting_index], starting_index + 1)

        computed[f'{first_elem}, {starting_index}'] = result
        return result

print(permutation_count(sorted_numbers[i - 1], i))
