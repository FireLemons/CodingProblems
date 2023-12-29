#!/usr/bin/python
import re

input_data = open("input.txt", "r")
valid_password_count = 0

line_lexer = re.compile(r"(\d+)-(\d+)\ (\w):\ (\w+)")

for line in input_data:
    line_data = line_lexer.match(line)
    min_character_count = line_data.group(1)
    max_character_count = line_data.group(2)
    special_character = line_data.group(3)
    password = line_data.group(4)

    special_character_counter = re.compile(special_character)
    
    valid_password_count += 1 if int(min_character_count) <= len(special_character_counter.findall(password)) <= int(max_character_count) else 0

print(valid_password_count)
