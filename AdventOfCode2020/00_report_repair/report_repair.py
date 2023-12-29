#!/usr/bin/python3
import bisect
import math

input_numbers = open("input.txt", "r")
numbers = []
for x in input_numbers:
    bisect.insort(numbers, int(x)) 

end = len(numbers) - 1
i = 0

midpoint = lambda search_end, search_start: math.floor(((search_end - search_start) / 2) + search_start)

while i < end:
    # Remove high numbers that can't possibly add to 2020
    while numbers[i] + numbers[end] > 2020:
        end -= 1

    # Binary Search for the 2020 compliment of numbers[i]
    search_start = i + 1
    search_end = end
    mid = midpoint(search_end, search_start)

    while search_start <= search_end:
        if numbers[i] + numbers[mid] == 2020:
            print( numbers[i] * numbers[mid] )
            exit(0)
        elif numbers[i] + numbers[mid] > 2020:
            search_end = mid - 1
        else:
            search_start = mid + 1
      
        mid = midpoint(search_end, search_start)

    i += 1
