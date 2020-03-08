from nand import NAND_gate
from not_gate import NOT_gate
from and_gate import AND_gate
from or_gate import OR_gate
from xor_gate import XOR_gate
from multiplexer import Multiplexer



def Demultiplexer(a,s):
  if(s==0):
    return(a,0)
  return(0,a)

# TEST CASES
print("A: 0, s:0 | Output: {0}".format(Demultiplexer(0, 0)))
print("A: 0, s:1 | Output: {0}".format(Demultiplexer(0, 1)))
print("A: 1, s:0 | Output: {0}".format(Demultiplexer(1, 0)))
print("A: 1, s:1 | Output: {0}".format(Demultiplexer(1, 1)))
