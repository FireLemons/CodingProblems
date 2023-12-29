#!/usr/bin/python3
import re

line_lexer = re.compile(r"(nop|acc|jmp)\ ([+-]\d+)")

def process_line(line):
    line_data = line_lexer.search(line).groups()
    return [line_data[0], int(line_data[1])]

input_instructions = open("input.txt", "r").read().split("\n")
input_instructions.pop()
input_instructions = list(map(process_line, input_instructions))

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

def execute():
    global instruction
    global instruction_pointer

    instruction.append(1)

    instruction_pointer = commands[instruction[0]](instruction_pointer, instruction[1])
    instruction = input_instructions[instruction_pointer]

def branch(command, arg):
    global accumulator
    global instruction
    global instruction_pointer
    executed_lines = []
    initial_acc_value = accumulator
    initial_instruction = instruction
    initial_instruction_pointer = instruction_pointer

    if command == "nop":
        instruction_pointer = jmp(instruction_pointer, arg)
    else: # command is jmp
        instruction_pointer = nop(instruction_pointer, arg)

    if instruction_pointer == len(input_instructions):
        return None

    instruction = input_instructions[instruction_pointer]

    while len(instruction) < 3:
        executed_lines.append(instruction_pointer)

        try:
            execute()
        except IndexError:
            return None

    return [initial_acc_value, initial_instruction, initial_instruction_pointer, executed_lines]

def revert(diff):
    global accumulator
    global instruction
    global instruction_pointer

    accumulator = diff[0]
    instruction = diff[1]
    instruction_pointer = diff[2]

    for pointer in diff[3]:
        input_instructions[pointer].pop()

while len(instruction) < 3:
    if not instruction[0] == "acc":
        branch_attempt = branch(instruction[0], instruction[1])
        if branch_attempt:
            revert(branch_attempt)
        else:
            print(accumulator)
            exit(0)

    execute()

print("Error")
