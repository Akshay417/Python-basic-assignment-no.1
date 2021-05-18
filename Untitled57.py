#!/usr/bin/env python
# coding: utf-8

# # Python Basic Assignment No.1
# 
Q1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.

Ans:   * = multiplication (mathematical Operator)
       "hello" = String element
       -87.8  = Float element
       -   = Subtraction (mathematical Operator)
       /   = Division (mathematical Operator)
       +   = Addition (mathematical Operation)
       6   = Integer element.
Q2. What is the difference between string and variable?

Ans:String is a tpye of data or information. And Variable is a store the data.
    eg. A ="Ineuron" 
        in above example A is a variable and "Ineuron" is a data as information which is store in A.      Q3. Describe three different data types.

Ans:  types of data:
    A) Built-in data type.
    B) User define data type.
    
       A) Built-in data type:
          1) None data type.
          2) Numeric data type.
          3) Sequences data type.
          4) Sets data type.
          5) Mapping data type.
      
             1) None data type:
                 this type of data represent that is object doesn't contains any value.
             2) Numeric data type:
                i) integer
               ii) float
              iii) boolean
               iv) complex
             3) Sequences data type:
                i) sets
               ii) Tuples
              iii) String
               iV) Range
             4) Set Data type:
                 set is a unordered collection of data or information data type.
             5) Mapping data type:
                i) Dictionary.
    Q4. What is an expression made up of? What do all expressions do?

Ans:Expression is madeup of combination of values and operators to perform mathematical operation to give a results. Q5. This assignment statements, like spam = 10. What is the difference between an
expression and a statement?

Ans:Expression is a combination of values and operators.expression evaluates to a value. Statement is represents any type of action or command to execute.  Q6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1

Ans:
# In[1]:


bacon=22
bacon+1

variabe bacon contain integer data type value that is 23. 
Q7. What should the values of the following two terms be?
   "spam"+"spamspam"
   "spam"* 3
   
Ans: The value is "spamspamspam".
      Q8. Why is eggs a valid variable name while 100 is invalid?

Ans:  100 is not valid variable because int() type data can'nt beigin with variable.9. What three functions can be used to get the integer, floating-point number, or string
version of a value?

Ans: int() function for get the integer.
     float() function for get the floating-point number.
     str() function for get the string version of a value.
    Q10. Why does this expression cause an error? How can you fix it?
     "I have eaten"  + 99 +  "burritos"
   
Ans: Because above expression contain string as well as interger type data.concatination of string and integer data type can't possible. for concatination of above expression we have to convert integer 99 into string by using str() function.
# In[18]:


"I have eaten" + str(99) + "burritos"

THANK YOU...!