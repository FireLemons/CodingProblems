#!/usr/bin/python3
import bisect
import math

input_numbers = open("input.txt", "r")
numbers = []
numbers_prime = []
preserved_indicies = []
orig_index = 0

for x in input_numbers:
    x = int(x)

    if len(numbers) >= 25:
        if len(numbers) == 26:
            oldest_index = preserved_indicies.index(orig_index - 26)
            numbers_prime.append(numbers.pop(oldest_index))
            preserved_indicies.pop(oldest_index)
        end = len(numbers) - 1

        for number in numbers:
            compliment = x - number

            try:
                while numbers[end] > compliment:
                    end -= 1
            except IndexError:
                while len(numbers):
                    orig_index += 1
                    oldest_index = preserved_indicies.index(orig_index - 26)
                    numbers_prime.append(numbers.pop(oldest_index))
                    preserved_indicies.pop(oldest_index)

                sublist_sum = numbers_prime[0]
                start = 0
                end = 0

                while not sublist_sum == x:
                    if sublist_sum < x:
                        end += 1
                        sublist_sum += numbers_prime[end]
                    elif sublist_sum > x:
                        sublist_sum -= numbers_prime[start]
                        start += 1

                sublist_min = math.inf
                sublist_max = 0
                
                for i in range(start, end + 1):
                    sublist_min = min(sublist_min, numbers_prime[i])
                    sublist_max = max(sublist_max, numbers_prime[i])
                    
                print(sublist_max + sublist_min)

                exit()
           
            if numbers[end] == compliment:
                break

    sort_position = bisect.bisect(numbers, x)
    numbers.insert(sort_position, x)
    preserved_indicies.insert(sort_position, orig_index)

    orig_index += 1
