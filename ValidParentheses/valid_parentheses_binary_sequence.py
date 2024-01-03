#!/usr/bin/python3

import sys

if len(sys.argv) == 1:
  print('Insufficient Arguments')
  exit()

try:
  n = int(sys.argv[1])
except:
  print(f'Could not convert argument "{sys.argv[1]}" into an integer')
  exit()

if n < 1:
  print("n must be at least 1")
  exit()

alternatingBitsEndingInZero = [2]
output = []

def binaryToParentheses(number):
  return format(number, 'b').replace('0', ')').replace('1', '(')

def getAlternatingBitsEndingInZero (n):
  computedValuesCount = len(alternatingBitsEndingInZero)

  if computedValuesCount < n:
    while computedValuesCount < n:
      alternatingBitsEndingInZero.append(alternatingBitsEndingInZero[computedValuesCount - 1] * 4 + 2)
      computedValuesCount += 1

  return alternatingBitsEndingInZero[n - 1]

def slowAssPythonHammingWeight(number):
  weight = 0

  while number:
    weight += 1
    number &= number - 1

  return weight

print(getAlternatingBitsEndingInZero(12))