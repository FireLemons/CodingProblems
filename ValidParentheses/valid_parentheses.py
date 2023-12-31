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

output = []
outputMaxLen = n * 2
parenthesesString = '1'
searchCursor = {
  'index': 1,
  'parenCountClosed': 0,
  'parenCountOpen': 1
}
traversablePathsStack = []

def isTraversable(openParentheses):
  if len(parenthesesString) >= outputMaxLen - 1:
    return False

  if openParentheses:
    return searchCursor['parenCountOpen'] + 1 <= n
  else:
    return searchCursor['parenCountClosed'] + 1 <= searchCursor['parenCountOpen']

def traverseParenthesesClosed():
  global parenthesesString, searchCursor

  searchCursor = traversablePathsStack.pop()
  parenthesesString = parenthesesString[:searchCursor['index']]

  parenthesesString = parenthesesString + '0'
  searchCursor['index'] +=  1
  searchCursor['parenCountClosed'] += 1

  return

def traverseParenthesesOpen():
  global parenthesesString

  parenthesesString = parenthesesString + '1'
  searchCursor['index'] +=  1
  searchCursor['parenCountOpen'] += 1

def doWhileLoopBody():
  if isTraversable(False):
    traversablePathsStack.append(searchCursor.copy())

  if isTraversable(True):
    traverseParenthesesOpen()
  else:
    traverseParenthesesClosed()
  
  if len(parenthesesString) >= outputMaxLen:
    output.append(parenthesesString)
  elif len(parenthesesString) == outputMaxLen - 1:
    output.append(parenthesesString + '0')

  return len(traversablePathsStack) > 0 or isTraversable(True)

if n == 1:
  output.append('()')
else:
  while (doWhileLoopBody()):
    pass

print(output)