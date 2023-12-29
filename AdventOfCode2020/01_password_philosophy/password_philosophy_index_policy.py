#!/usr/bin/python
import re

input_data = open("input.txt", "r")
valid_password_count = 0

line_lexer = re.compile(r"(\d+)-(\d+)\ (\w):\ (\w+)")

for line in input_data:
    line_data = line_lexer.match(line)
    first_character_index = line_data.group(1)
    last_character_index = line_data.group(2)
    special_character = line_data.group(3)
    password = line_data.group(4)

    special_character_counter = re.compile(special_character)

    # Need 2 iterators because they can't be reset after use
    character_matches_1 = special_character_counter.finditer(password)
    character_matches_2 = special_character_counter.finditer(password)

    valid_password_count += 1 if any(match.start() == (int(first_character_index) - 1) for match in character_matches_1) != any(match.start() == (int(last_character_index) - 1) for match in character_matches_2 ) else 0

print(valid_password_count)
