#!/usr/bin/python
import bisect

input_numbers = open("input.txt", "r")
numbers = []
for x in input_numbers:
    bisect.insort(numbers, int(x)) 

end = len(numbers) - 1
i = 0

while i < end:
    # Remove high numbers that can't possibly add to 2020
    while numbers[i] + numbers[end] > 2020:
        end -= 1

    j = i + 1
    end_prime = end

    while j < end:
        sub_sum = numbers[i] + numbers[j]

        # Remove high numbers that can't possibly add to 2020
        while sub_sum + numbers[end_prime] > 2020 and end_prime >= 0:
            end_prime -= 1

        # Binary Search for the 2020 compliment of numbers[i]
        search_start = j + 1
        search_end = end_prime
        midpoint = ((search_end - search_start) / 2) + search_start

        while search_start <= search_end:
            if sub_sum + numbers[midpoint] == 2020:
                print(numbers[i] * numbers[j] * numbers[midpoint] )
                exit(0)
            elif sub_sum + numbers[midpoint] > 2020:
                search_end = midpoint - 1
            else:
                search_start = midpoint + 1
          
            midpoint = ((search_end - search_start) / 2) + search_start

        j += 1
    i += 1
