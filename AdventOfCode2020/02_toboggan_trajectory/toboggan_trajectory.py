#!/usr/bin/python

input_terrain = open("input.txt", "r")
x = 0
tree_count = 0

for line in input_terrain:
    line_prime = line.rstrip()

    tree_count += 1 if line_prime[x] == "#" else 0

    x += 3
    line_length = len(line_prime)
    x = x if x < line_length else x % line_length

print(tree_count)
