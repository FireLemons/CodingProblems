#!/usr/bin/python3

input_passport_data = open("input.txt", "r")

alphabet_binary_values = {
    "a": 1,
    "b": 2,
    "c": 4,
    "d": 8,
    "e": 16,
    "f": 32,
    "g": 64,
    "h": 128,
    "i": 256,
    "j": 512,
    "k": 1024,
    "l": 2048,
    "m": 4096,
    "n": 8192,
    "o": 16384,
    "p": 32768,
    "q": 65536,
    "r": 131072,
    "s": 262144,
    "t": 524288,
    "u": 1048576,
    "v": 2097152,
    "w": 4194304,
    "x": 8388608,
    "y": 16777216,
    "z": 33554432,
    "\n": 0,
}

group_shared_questions = -1
count_sum = 0

for line in input_passport_data:
    if line == "\n":
        for char in "{0:b}".format(group_shared_questions):
            count_sum += 1 if char == "1" else 0
        group_shared_questions = -1
    else:
        individual_questions = 0
        for char in line:
            individual_questions |= alphabet_binary_values[char]

        group_shared_questions &= individual_questions

for char in "{0:b}".format(group_shared_questions):
    count_sum += 1 if char == "1" else 0

print(count_sum)
