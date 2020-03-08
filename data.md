Logic Gates

Introduction: Voltage & Bits

Computers are capable of dizzying feats, but they’re built from humble origins. At the lowest level, computers run on electric currents limited to two states: power or no power.

There are many ways to represent the two states:

    “I have current!” vs. “I don’t have current!”
    “on” vs. “off”
    + vs. -
    True vs. False
    1 vs. 0


We’ll use 1 and 0 for the remainder of the lesson. This piece of information (power or no power) localized to a single location is called a bit. 


    Bit with power: 1
    Bit without power: 0

Logic gates receive one or more inputs of current and alter the power according to their rules.

Some logic gates will only output power if both of their inputs are powered.


Truth Tables

Logic gates have certain rules that determine what the outputs are with respect to the inputs a and b. When we are analyzing a logic gate, we can visualize all of the possible outputs by making a truth table. A truth table shows the output for all possible inputs.

For example, if we have a gate that returns 1 if and only if both the inputs a and b are 1, we can create the truth table:
a 	b 	output
0 	0 	0
0 	1 	0
1 	0 	0
1 	1 	1

Each row represents an observation of output depending on the values of a and b. So the first row shows that when a is 0 and b is 0, the output will be 0.

When we make a truth table, we want to represent the entire universe of possibilities. This means that we want every combination of inputs to be represented. For 2 variables (a and b), we will need 4 rows to represent all of these combinations.

In Python, and many other programming languages, 1 evaluates to be True, and 0 evaluates to be false.

//NAND GATE 

NAND Gate

Our first gate is the NAND gate. This gate receives two inputs and only returns current if the inputs are both off.

Here’s the truth table:

a 	b 	output
0 	0 	1
0 	1 	1
1 	0 	1
1 	1 	0

def NAND_gate(a, b):
  if a==1:
    if b==1:
      return 0
  return 1

# TEST CASES

print("A: 0, B: 0 | Output: {0}".format(NAND_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(NAND_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(NAND_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(NAND_gate(1, 1)))


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

AND Gate

Our next gate is the AND gate. This gate receives two inputs and only returns current if the inputs are both on.

from nand import NAND_gate
from not_gate import NOT_gate

def AND_gate(a,b):
  if a==1:
    if b==1:
      return NAND_gate(0,0)
  return NAND_gate(1,1)




# TEST CASES

print("A: 0, B: 0 | Output: {0}".format(AND_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(AND_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(AND_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(AND_gate(1, 1)))


OR Gate

The next gate we are going to build is the OR gate. This gate receives two inputs and returns 1 if either one of the inputs is 1.

To build your OR_gate(), you should use any combination of the gates you’ve already made: NAND_gate(), NOT_gate(), and AND_gate().

Here’s the truth table:
a 	b 	output
0 	0 	0
0 	1 	1
1 	0 	1
1 	1 	1



NAND_der_OR

from nand import NAND_gate
from not_gate import NOT_gate
from and_gate import AND_gate

"""def OR_gate(a,b):
  if(a==0):
    if(b==0):
      return 0
  return 1
"""
def OR_gate(a,b):
  return NAND_gate(NAND_gate(a,a), NAND_gate(b,b))


# TEST CASES

print("A: 0, B: 0 | Output: {0}".format(OR_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(OR_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(OR_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(OR_gate(1, 1)))


XOR Gate

Now, we are going to create what’s called an XOR gate, an exclusive or gate. This gate receives two inputs, a and b, and only returns a 1 if one of the inputs is 1, but not if both of the inputs are 1.

To build your XOR_gate(), you should use any combination of the gates you’ve already made: NAND_gate(), NOT_gate(), AND_gate(), and OR_gate().

Here’s the truth table:
a 	b 	output
0 	0 	0
0 	1 	1
1 	0 	1
1 	1 	0

from nand import NAND_gate
from not_gate import NOT_gate
from and_gate import AND_gate
from or_gate import OR_gate


def XOR_gate(a,b):
  return AND_gate(NAND_gate(a,b),OR_gate(a,b))
# TEST CASES

print("A: 0, B: 0 | Output: {0}".format(XOR_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(XOR_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(XOR_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(XOR_gate(1, 1)))

Logic Gate Review

Congratulations! You’ve built out an impressive array of logic gates. The physical representations of these gates are most likely being used in the computer you’re using right now!

https://s3.amazonaws.com/codecademy-content/courses/logic-gates/truth-tables.html

Bit Selection

Up until now, our logic circuits have produced the same output for a given input.

What if we wanted to incorporate branching into our circuits? Branching is when the output is chosen by a third input, a selector bit that we’ll call s.

Our truth tables will now involve a third s input in addition to the inputs a and b. This selector bit will dictate which of the inputs we pass along as output.

# Truth table:
# ___________________
# a     b     s     output
# 0     0     0     0
# 0     1     0     0
# 1     0     0	    1
# 1     1     0     1
# 0     0     1     0
# 0     1     1     1
# val1  val2  val3  val4
# 1     1     1     1


val1 = "1"
val2 = "0"
val3 = "0"
val4 = "1"

Multiplexer

The logic gate that was introduced in the last exercise is called a multiplexer. It takes in the inputs a and b and a selection bit s, and outputs either a or b, depending on what s is.



Here is the truth table again:
a 	b 	s 	output
0 	0 	0 	0
0 	1 	0 	0
1 	0 	0 	1
1 	1 	0 	1
0 	0 	1 	0
0 	1 	1 	1
1 	0 	1 	0
1 	1 	1 	1


     Z = ( A ∧ ¬ S 0 ) ∨ ( B ∧ S 0 ) {\displaystyle Z=(A\wedge \neg S_{0})\vee (B\wedge S_{0})} {\displaystyle Z=(A\wedge \neg S_{0})\vee (B\wedge S_{0})}


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



Demultiplexer

If a multiplexer takes two inputs and channels it into one based on a selector bit, a demultiplexer performs the opposite function: it takes a single input and splits it into two outputs based on a selector bit.

If s is 0 then output1 is a and b is 0.

If s is 1 then output2 is b and a is 0.

Here’s the truth table:
a 	s 	output 1 	output 2
0 	0 	0 	0
0 	1 	0 	0
1 	0 	1 	0
1 	1 	0 	1



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

Learn: Logic Gates
Logic Gate Review

Good job! You’ve started with little bits, and you’ve built out an entire toolkit of logic gates you now can use to perform more complicated operations. You’re well on your way to creating an entire operating system. Watch out, Unix!

We’ve covered:

    Bits and current
    Truth tables
    NAND gates
    NOT gates
    OR gates
    XOR gates
    Branching, using:
        Multiplexers to switch between different inputs
        Demultiplexers to turn one input into two inputs

You’ve done a great job of creating these gates from scratch in Python! All of the basic gates exist already as bitwise operators in Python. Now that you’ve done the hard work to understand how each works, you can save time by using these built-in operators:



#NOT: 
~ x
#E.g. ~1 == 0 and ~0 == 1

#AND:
x & y
#E.g. 1&1 == 1 and 1&0 == 0

#OR:
x | y
#E.g. 1|1 == 1 and 0|0 == 0

#XOR:
x ^ y
#E.g. 1^1 == 0 and 1^0 == 1

YAND_gate 


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


-------------------------------------------------------------------------------------------

references:

http://web.mit.edu/6.111/www/f2005/tutprobs/synthesis.html



--------------------------------------------------------------------------------------------

notes:

look into multiplexers and demux