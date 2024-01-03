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

alternatingBits = [0]

def binaryToParentheses(number):
  return format(number, 'b')#.replace('0', ')').replace('1', '(')

def getAlternatingBits (numberOfBits):
  computedValuesCount = len(alternatingBits)

  if computedValuesCount <= numberOfBits:
    while computedValuesCount <= numberOfBits:
      alternatingBits.append(alternatingBits[computedValuesCount - 1] * 2 + computedValuesCount % 2)
      computedValuesCount += 1

  return alternatingBits[numberOfBits]

def slowAssPythonHammingWeight(number):
  weight = 0

  while number:
    weight += 1
    number &= number - 1

  return weight

lastOutput = 0

while lastOutput < 2 ** (n - 1):
  lastOutput *= 2
  lastOutput += 1

lastOutput *= 2 ** n
mostRecentlyComputedNumber = getAlternatingBits(n * 2)
numberToAdd = 2
output = [binaryToParentheses(mostRecentlyComputedNumber)]

while mostRecentlyComputedNumber < lastOutput:
  mostRecentlyComputedNumber += numberToAdd
  numberToAdd *= 2

  mostRecentlyComputedNumberHammingWeight = slowAssPythonHammingWeight(mostRecentlyComputedNumber)

  if (mostRecentlyComputedNumberHammingWeight < n):
    #print(f'{binaryToParentheses(mostRecentlyComputedNumber)} was found to not have enough bits')
    #print(f'adding {getAlternatingBits((n - mostRecentlyComputedNumberHammingWeight) * 2)}')
    mostRecentlyComputedNumber += getAlternatingBits((n -  mostRecentlyComputedNumberHammingWeight) * 2)
    numberToAdd = 2

  #print(binaryToParentheses(mostRecentlyComputedNumber))
  output.append(binaryToParentheses(mostRecentlyComputedNumber))

print(len(output))