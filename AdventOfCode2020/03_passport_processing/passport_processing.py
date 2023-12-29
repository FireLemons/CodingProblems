#!/usr/bin/python3
import re

input_passport_data = open("input.txt", "r")

passport_data = ""
valid_passport_count = 0

passport_data_lexer = re.compile(r"(\w{3}):[#\w\d]+", re.MULTILINE)

field_validity_bits = {
    "byr" : 15,
    "iyr" : 240,
    "eyr" : 3840,
    "hgt" : 61440,
    "hcl" : 983040,
    "ecl" : 15728640,
    "pid" : 251658240,
}

def determine_validity(passport_data):
    passport_validity = -268435456

    for match in passport_data_lexer.finditer(passport_data):
        try:
            passport_validity |= field_validity_bits[match.group(1)]
        except:
            pass

    return not ~passport_validity

for line in input_passport_data:
    if line == "\n":
        valid_passport_count += 1 if determine_validity(passport_data) else 0
        passport_data = ""
    else:
        passport_data += line

valid_passport_count += 1 if determine_validity(passport_data) else 0

print(valid_passport_count)
