from nand import NAND_gate
from not_gate import NOT_gate
from and_gate import AND_gate
from or_gate import OR_gate
from xor_gate import XOR_gate
from multiplexer import Multiplexer
from demultiplexer import Demultiplexer


def YAND_gate(a,b):
  if a&b==0:
    a=1
    b=1
  else:
    pass
  return(OR_gate(a,b))

print("A: 0, B: 0 | Output: {0}".format(YAND_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(YAND_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(YAND_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(YAND_gate(1, 1)))
