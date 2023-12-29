#!/usr/bin/python
import re

line_lexer = re.compile(r"(nop|acc|jmp)\ ([+-]\d+)")

def process_line(line):
    line_data = line_lexer.search(line).groups()
    return [line_data[0], int(line_data[1])]

input_instructions = open("input.txt", "r").read().split("\n")
input_instructions.pop()
input_instructions = map(process_line, input_instructions)

accumulator = 0
instruction = input_instructions[0]
instruction_pointer = 0

def nop(ip, diff):
    return ip + 1

def acc(ip, diff):
    global accumulator
    accumulator += diff
    return ip + 1

def jmp(ip, diff):
    return ip + diff

commands = {
    "nop": nop,
    "acc": acc,
    "jmp": jmp
}

while len(instruction) < 3:
    instruction.append(1)

    instruction_pointer = commands[instruction[0]](instruction_pointer, instruction[1])
    instruction = input_instructions[instruction_pointer]

print(accumulator)
