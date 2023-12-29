#!/usr/bin/python
tree_product = 1
input_terrain = open("input.txt", "r")

def tree_count(delta_x, delta_y):
    input_terrain.seek(0)
    x = 0
    y = 0
    tree_count = 0

    for line in input_terrain:
        if y % delta_y == 0:
            line_prime = line.rstrip()

            tree_count += 1 if line_prime[x] == "#" else 0

            x += delta_x
            line_length = len(line_prime)
            x = x if x < line_length else x % line_length
        y += 1

    return tree_count

tree_product *= tree_count(1, 1)
tree_product *= tree_count(3, 1)
tree_product *= tree_count(5, 1)
tree_product *= tree_count(7, 1)
tree_product *= tree_count(1, 2)

print(tree_product)
