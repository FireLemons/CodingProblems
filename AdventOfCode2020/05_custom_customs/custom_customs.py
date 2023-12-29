#!/usr/bin/python3

input_passport_data = open("input.txt", "r")

custom_form_data = ""
party_question_count = {}
total_question_count = 0

def count_party_questions(custom_form_data):
    question_count = 0

    for char in custom_form_data:
        party_question_count[char] = 0

    question_count += len(party_question_count.keys())

    if "\n" in party_question_count:
        question_count -= 1

    return question_count


for line in input_passport_data:
    if line == "\n":
        total_question_count += count_party_questions(custom_form_data)

        custom_form_data = ""
        party_question_count = {}
    else:
        custom_form_data += line

total_question_count += count_party_questions(custom_form_data)

print(total_question_count)
