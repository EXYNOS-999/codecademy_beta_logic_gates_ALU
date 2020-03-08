from nand import NAND_gate

def NOT_gate(a):
  if(a==0):
    return 1
  return 0

# TEST CASE
print("A: 0 | Output: {0}".format(NOT_gate(0)))
print("A: 1 | Output: {0}".format(NOT_gate(1)))

# TEST CASE
print("A: 0 | Output: {0}".format(NAND_gate(0,0)))
print("A: 1 | Output: {0}".format(NAND_gate(1,1)))