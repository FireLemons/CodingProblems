#!/usr/bin/python3

import struct
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

if struct.calcsize("i") == 4: # 32 bit ints
  bitCaptures = [0x55555555, 0x33333333, 0x0f0f0f0f, 0x00ff00ff, 0x0000ffff]
else: # assuming 64 bit ints
  bitCaptures = [0x5555555555555555, 0x3333333333333333, 0x0f0f0f0f0f0f0f0f, 0x00ff00ff00ff00ff, 0x0000ffff0000ffff, 0x00000000ffffffff]

def binaryToParentheses(number):
  return format(number, 'b').replace('0', ')').replace('1', '(')

def getAlternatingBits (numberOfBits):
  computedValuesCount = len(alternatingBits)

  if computedValuesCount <= numberOfBits:
    while computedValuesCount <= numberOfBits:
      alternatingBits.append(alternatingBits[computedValuesCount - 1] * 2 + computedValuesCount % 2)
      computedValuesCount += 1

  return alternatingBits[numberOfBits]

def getHammingWeight(number):
  weight = number

  for i in range(0, len(bitCaptures)): 
    bitCapture = bitCaptures[i]
    weight = (weight & bitCapture) + ((weight >> (2 ** i)) & bitCapture)

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

  mostRecentlyComputedNumberHammingWeight = getHammingWeight(mostRecentlyComputedNumber)

  if (mostRecentlyComputedNumberHammingWeight < n):
    mostRecentlyComputedNumber += getAlternatingBits((n -  mostRecentlyComputedNumberHammingWeight) * 2)
    numberToAdd = 2

  output.append(binaryToParentheses(mostRecentlyComputedNumber))

print(len(output))