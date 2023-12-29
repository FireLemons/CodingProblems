#!/usr/bin/python3
import bisect
import math

input_numbers = open("input.txt", "r")
numbers = []
preserved_indicies = []
orig_index = 0

for x in input_numbers:
    x = int(x)

    if len(numbers) >= 25:
        if len(numbers) == 26:
            oldest_index = preserved_indicies.index(orig_index - 26)
            numbers.pop(oldest_index)
            preserved_indicies.pop(oldest_index)
        end = len(numbers) - 1

        for number in numbers:
            compliment = x - number

            try:
                while numbers[end] > compliment:
                    end -= 1
            except IndexError:
                print(x)
                exit(0)
           
            if numbers[end] == compliment:
                break

    sort_position = bisect.bisect(numbers, x)
    numbers.insert(sort_position, x)
    preserved_indicies.insert(sort_position, orig_index)

    orig_index += 1
