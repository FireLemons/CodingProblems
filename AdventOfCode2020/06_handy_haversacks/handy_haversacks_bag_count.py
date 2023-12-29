#!/usr/bin/python3
import re

input_bag_data = open("input.txt", "r")

bags_data = {}
gold_bag_contents_total = 0

color_lexer = re.compile(r"^(\w+\ \w+)")
contents_lexer = re.compile(r"(\d+)\ (\w+\ \w+)\ bags?")

for line in input_bag_data:
    bag_contents = contents_lexer.findall(line)

    if len(bag_contents):
        bag_color = color_lexer.match(line).group(1)

        if not bag_color in bags_data:
            bags_data[bag_color] = {}

        bag = bags_data[bag_color]

        for inner_bag in bag_contents:
            inner_bag_color = inner_bag[1]
            inner_bag_quantity = int(inner_bag[0])

            if not bag_color in bags_data:
                bags_data[bag_color] = {}

            bag_data = bags_data[bag_color]

            if not inner_bag_color in bags_data:
                bags_data[inner_bag_color] = {}

            if not "contents" in bag:
                bag["contents"] = []

            bag["contents"].append([inner_bag_quantity, inner_bag_color])

gold_tree_bfs = [[1, bags_data["shiny gold"]]]

while len(gold_tree_bfs):
    node = gold_tree_bfs.pop()

    multiplier = node[0]
    bag = node[1]

    gold_bag_contents_total += multiplier

    if "contents" in bag:
        for inner_bag in bag["contents"]:
            gold_tree_bfs.append([multiplier * inner_bag[0], bags_data[inner_bag[1]]])

print(gold_bag_contents_total - 1)
