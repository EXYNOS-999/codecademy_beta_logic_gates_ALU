from nand import NAND_gate
from not_gate import NOT_gate
from and_gate import AND_gate
from or_gate import OR_gate
from xor_gate import XOR_gate
from multiplexer import Multiplexer
from demultiplexer import Demultiplexer

c_in=0

def half_adder(a,b):
  s=a^b
  c=a&b
  return(s,c_in)


def full_adder(a,b,c_in):
  half_adder(a,b)
  s=a^b
  d=c_in^s
  c_out=((c_in &s) |(a&b))
  return(s,c_out)


def ALU(a,b,c_out,opcode):
  if(opcode==0):
    return half_adder(a, b)
  return full_adder(a, b, c_out)
    

#TEST CASES 

print("A: 0, B: 0 | Output: {0}".format(half_adder(1, 1)))
print("A: 0, B: 1 | Output: {0}".format(full_adder(0, 1,1)))
print("A: 1, B: 0 | Output: {0}".format(full_adder(1, 0,0)))
print("A: 1, B: 1 | Output: {0}".format(full_adder(1, 1,1)))


print(ALU(0,1,0,1))
