#!/usr/bin/python3
import re

input_bag_data = open("input.txt", "r")

bags_data = {}
valid_bag_color_count = 0

color_lexer = re.compile(r"^(\w+\ \w+)")
contents_lexer = re.compile(r"\d+\ (\w+\ \w+)\ bags?")

for line in input_bag_data:
    bag_contents = contents_lexer.findall(line)

    if len(bag_contents):
        bag_color = color_lexer.match(line).group(1)

        for inner_bag_color in bag_contents:
            if not bag_color in bags_data:
                bags_data[bag_color] = {}

            bag_data = bags_data[bag_color]

            if not inner_bag_color in bags_data:
                bags_data[inner_bag_color] = {}

            inner_bag = bags_data[inner_bag_color]

            if not "required" in inner_bag:
                inner_bag["required"] = [bag_color]
            else:
                inner_bag["required"].append(bag_color)

gold_tree_bfs = [bags_data["shiny gold"]]

while len(gold_tree_bfs):
    node = gold_tree_bfs.pop()

    if "required" in node:
        for color in node["required"]:
            if not "is_member" in bags_data[color]:
                bags_data[color]["is_member"] = True
                valid_bag_color_count += 1
                gold_tree_bfs.append(bags_data[color])

print(valid_bag_color_count)
