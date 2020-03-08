from nand import NAND_gate
from not_gate import NOT_gate
from and_gate import AND_gate
from or_gate import OR_gate
from xor_gate import XOR_gate

def Multiplexer(a,b,s):
  return OR_gate(AND_gate(a,NOT_gate(s)),AND_gate(b,s))
  
  
def Multiplexer(a,b,s):
  if s:
  return b
else:
  return a

# TEST CASES
print("A: 0, B: 0, s:0 | Output: {0}".format(Multiplexer(0, 0, 0)))
print("A: 0, B: 1, s:0 | Output: {0}".format(Multiplexer(0, 1, 0)))
print("A: 1, B: 0, s:0 | Output: {0}".format(Multiplexer(1, 0, 0)))
print("A: 1, B: 1, s:0 | Output: {0}".format(Multiplexer(1, 1, 0)))
print("A: 0, B: 0, s:1 | Output: {0}".format(Multiplexer(0, 0, 1)))
print("A: 0, B: 1, s:1 | Output: {0}".format(Multiplexer(1, 0, 1)))
print("A: 1, B: 0, s:1 | Output: {0}".format(Multiplexer(0, 1, 1)))
print("A: 1, B: 1, s:1 | Output: {0}".format(Multiplexer(1, 1, 1)))
