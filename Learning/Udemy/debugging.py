# debugging
# lintiing >> use to detect error in code, manally used in editor.

# num + 6 # Error num not define

# 'num' + 4 # Error int add with str

# pdb >> Python debugger
# pdb is a bult-in module in python

import pdb

def addNum(num1, num2):
  # print(num1, num2)
  pdb.set_trace()
  return num1 + num2

finalNum = addNum(4, 'num')
print(finalNum)
