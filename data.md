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

references://to-do 

http://web.mit.edu/6.111/www/f2005/tutprobs/synthesis.html

http://www.ee.surrey.ac.uk/Projects/CAL/digital-logic/gatesfunc/index.html

https://www.khanacademy.org/computing/ap-computer-science-principles/computers-101/logic-gates-and-circuits/a/logic-gates

https://www.coursera.org/learn/digital-systems

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c4/c4s2/c4s2v2/useful-logic-gates-5-56-/

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c4/c4s2/c4s2v8/gates-and-boolean-logic/


--------------------------------------------------------------------------------------------

notes:

look into multiplexers and demux



----------------------------------------------------------


Creating an Adder Circuit

At the most basic level, the computer you are typing on right now is a complex combination of the gates you have already learned how to construct. But how do we go from having a NAND gate, for example, to having an entire processor that runs Mac OS?

One step we can take towards this goal is to create an ALU, or an Arithmetic Logic Unit. An ALU can perform a bunch of bitwise operations like adding, subtracting, and shifting.

For this project, we are going to focus on creating one part of the ALU, the adder.

A full adder is normally comprised of two half adders. A half adder takes in two inputs, a and b, and returns a sum bit, s, and a carry bit, c. The truth table looks like this:

a 	b 	s 	c
0 	0 	0 	0
0 	1 	1 	0
1 	0 	1 	0
1 	1 	0 	1

When we add 0 to 0, we should get a sum of 0 with a carry of 0. When we add 0 to 1, we should get a sum of 1, with a carry of 0. And so on.

The full adder takes in a, b, and a carry-in bit c. It returns a sum bit s and a carry-out bit c_out. The truth table looks like this:
a 	b 	c 	s 	c_out
0 	0 	0 	0 	0
0 	0 	1 	0 	1
0 	1 	0 	0 	1
0 	1 	1 	1 	0
1 	0 	0 	0 	1


HALF ADDER 

s::=a ^ b   //  ::= this is defining the relationship not assigning it.
c=a & b  


//ripple carry


THEORY:

Propositional operators play a basic role in the design of digital circuitry, and we're going to illustrate that in the section by designing a little binary addition circuit.

So let's begin with a review of binary notation and addition in binary.

So the way binary works is like decimal. Except instead of using powers of 10, you're using powers of 2. So here is the binary representation of the number 39. The way to understand that is this is the ones place. That's the twos place. That's the fours place.

So 1 plus 2 plus 4 is 7. Then this is the eighth place with nothing, this is the 16th place with something, and this is the 32 place with 1. So we get 32 to 7, and get 39.

Likewise, the binary representation of 28 is 011100. I'll let you check how that works with contributing 1, 2, 4, 8, 16, and 32.

And finally, let's add these two numbers in binary. Now, binary addition works just like decimal addition except that the only numbers are ones and zeros so that when you get 1 plus 1, you have to carry 1. Let's do that.

So 1 plus 0 is 1. That fills in the first column. Now we have another 1 plus 0 is 1. That's fine.

Now we have a 1 plus 1. And that's going do a 0 here and contribute a carry of 1 to the next column. Now, the next column has two ones. So it becomes a 0 and contributes to another carrying. Now we have two ones. We get a 0 and contribute another carry. And now we have two ones, and we finally get a 1 0.

So this is the binary representation of the sum, and you can check that this is 1 plus 2 is 3 plus 64. So the answer should be 67. And you can check that it is. So that's how binary addition works.

So now let's try to design a bit of circuitry using digital logic signals of 0 and 1, which will do addition. And so we're going to try to design a little six bit binary addition circuit. So I'm going to have as inputs, the six digits of the first binary number-- a 5 down through a 0 and then the second binary number. Let's call it b 0 through b 5.

So these are two binary numbers that are six digits long, and I'm going to add them up by thinking of a 1 as a 0 or 1 signal. a 0 is a 0 1 signal. b 0 is a 0 1 signal.

And these can be transmitted down wires into some boxes that contain digital operators that will cause the right signals to come out. And what we want to come out of here is the possibly seven digit representation of their binary sum.

So d 0 is the sum of a 0 and b 0-- the lower digit possibly with carry and so on.

And then c 5 if the sum of two six digit numbers runs to seven digits, which it might as we saw in the previous example, then c 5 would become 1, otherwise 0.

So this is the specification. I want a and b to come in, and I want their binary sum to come out as d's with a high order c if need be.

Now, the way I'm going to do that is it's clear that the behavior of the inputs for a and b, which produced the lower digit, might produce a carry, and that carry has to be transmitted to the next column if it exists. So I'm going to need a wire that sends a 0 1 signal from this box over to that one that carries 0 or 1 and likewise for all of the others.

So this is the kind of basic structure of my binary addition circuit. This is called a ripple carry organization. It's mimicking exactly the way that we added up to two numbers column by column, possibly propagating carry of 0 or 1-- or really a carry of just 1 to the next column. And I've got all the wires in place that I need. What we need to do is design the digital circuitry that's in those boxes.

Well, this box is different from the others because it's only got two inputs. All the others have three inputs. So the three input boxes, we'll call full adders and the two input boxes a half an adder.

And the specification of a half an adder, again, is that the output is the binary representation of a 0 plus b 0. So it's a two digit binary representation-- never be bigger than 2 because there's only two numbers.

The output of a full adder is it gets three inputs in this case-- b 1, a 1. And the carry, c 0. And it produces the binary representation of the sum of those three numbers, which is a two digit binary representation that might be anything from 0 to 3. OK.

Well, let's start with the easy case. What's a half adder? Well, a half adder, again, has inputs b and a, and it's supposed to produce as output the binary representation of b plus a. So d is the lower digit in the zeros place, and c is the high order digit, namely the twos place.

Well, what does that look like? Well, here's the circuit. This is the digital designer symbol for an exclusive [INAUDIBLE] gate that returns.

So d is going to be the exclusive or of a and b according to this pictorial diagram. Notice I'm using this colon colon equal symbol which is convenient as a reminder that I'm defining the thing on the left. You could replace it by equal, but it's informative to realize that it's not an equality that you've proved or that some derivation of the two interesting things are proven to be equal, but rather that I'm just defining what the d is.

This output d is defined to be a XOR b.

And likewise, this is an AND gate. So the output c a AND b.

And let's check that. The low order digit is definitely the [INAUDIBLE] sum, XOR of a and b.

And when is there a carry? Well, the only way there's a carry is when the value is 2, in which case the output c would be 1 and d would be 0. And that's exactly when both a and b are 1, that is c is a and b.

So that's a half adder. That was easy.

Well, a full adder looks like this. It's a little bit more complicated, and I'm going to write out the equations without trying to justify them completely. But I need a name in order to describe this with propositional operators. I need a name for that important signal. Call it s, which is what we were not calling it in the previous one.

But now this is a half adder with inputs a and b and outputs s, which is a XOR b and another output here, which we know is just going to be a and b. OK.

How do I express this set of connections as formulas? Well, first of all, s is the output of this first half adder, which is a XOR b. OK.

The output d I get by taking s, and it's the first output of the second half adder, which means it's c in XOR or s. That's easy.

And what about c out? Well, c out is getting-- this is an OR gate by the way. So c out is going to be an OR of what comes out of this half adder, which is c in and c s and OR with the output of this half adder, which is just a and b.

So there are a bunch of equations that completely characterize the structure of this little bit of digital logic and how it is wired up and fits together.

Now, let's go back to describing our ripple carry circuit of what was going on here. Now that we have the equations that characterize the behavior of these full adders and half adders, I can explain to you what the formulas are for all of these outputs-- the c's and the d's. And that goes as follows.

So the first one, looking at this half adder with a 0, b 0 coming in and c 0, d 0 coming out, I know that d 0 is a 0 XOR b 0 and c 0 is a 0 AND b0.

That's just that the formulas that we have for the half adder when the inputs are a 0 and b 0 and I call the outputs b 0 and c 0.

Now, the more general case of the full adder-- what's coming in here is an a and a b with the same subscript-- a i and b i. And what's coming out is the ith digit of the binary sum, d i and the carry c i.

And I could describe those just by using the formulas for the full adder. So what it means is that I'm going to introduce a new convening variable, s i, which I'm going to define to be a i or XOR b i.

D i is then going to be c i minus 1-- the carry from the previous place-- XOR with s i. And the new carry, c i, is going to be the output of the first half adder, which is c i minus 1 AND s i or the output of the first half adder, which is a i and b i.

So the point is that I've just taken the wiring and translated it into equations like this, and you can see how these equations might be better to use than the particular way that you drew the picture with all the wires connected because the logical behavior of the circuit doesn't depend on how it's laid out. It just depends on these logical connectives between the values of these different variables. 

FULL ADDER 

 s::=a ^ b
 d=c_in^s 
 c_out=((c_in & s ) | (a & b))

 d0::=(a0 XOR b0)
 c0::=(a0 AND b0)

 si::= Ai XOR Bi
 Di::=Ci-1 XOR Si
 Ci::=(Ci-1 AND s1) OR (Ai AND Bi)


 Wow! You have a basic Arithmetic Logic Unit that can produce different outputs with the same inputs.

Most ALUs also allow for incrementing, decrementing, and subtraction. Can you figure out how to implement incrementation (adding 1 to a) in your ALU? You will probably need a bigger opcode!


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


