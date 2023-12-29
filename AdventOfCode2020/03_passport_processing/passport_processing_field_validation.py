#!/usr/bin/python3
import re

input_passport_data = open("input.txt", "r")

passport_data = ""
valid_passport_count = 0

passport_data_lexer = re.compile(r"(byr):(19[2-9][\d]|200[0-2])|(iyr):20(1[0-9]|20)|(eyr):20(2[0-9]|30)|(hgt):(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)|(hcl):#[\da-f]{6}|(ecl):(amb|blu|brn|gry|grn|hzl|oth)|(pid):[0-9]{9}(\ |\n|\Z)", re.MULTILINE)

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
            passport_validity |= field_validity_bits[match.group()[:3]]
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
