#!/usr/bin/env python
# coding: utf-8
Q 01. what exactly is [] ?

Ans: [] this is a square bracket symbol which is mostly use for indicating list. 
list=[]Q 02. In list of vlaues stored in a variable called spam, how would you assing the value 'hello' as the third value?
spam = [2,4,6,8,10]

Ans:  
# In[3]:


spam = [2,4,6,8,10]
spam[3] = ('hello')


# In[5]:


spam

Q. 03. 
Lets pretend the spam includes the list ['a','b','c','d'] for the next three queries.

01. What is the value of spam [int(int('3' * 2/ 11)]
# In[13]:


spam = ['a','b','c','d']
spam [int(int('3' * 2)/ 11)]

what is the value of spam [-1] ?

Ans: 'd'what is the value of spam[-2] ?

Ans: 'c'lets pretend bacon has list[3.14, 'cat',11,'cat',True] for the next theree question.what is the value of bacon.index('cat') ?

Ans: value is 1.How does bacon.append(99) change the look of the list value in bacon ?
Ans: (99) will be add in the end of the list at fifth index.
# In[23]:


bacon = [3.14, 'cat',11,'cat',True]
bacon.append(99)


# In[22]:


bacon

How does bacon.remove('cat') chages the look of the list in the bacon ?

Ans: 'cat' from the first index will be remove. other one is same.
# In[19]:


bacon = [3.14, 'cat',11,'cat',True]
bacon.remove('cat')


# In[20]:


bacon

What are the list concatination and list replication operators ?

Ans:list concatination is the cration of the single list from the multiple smaller list.
The multiplication operator acts as a replication operator when we have one string and one integer as operands.What is the differece between the list methods append() and insert() ?

Ans: In append() method, the data add at the last of the given list. and in insert() method, the data is add as per user required location. What are the two methods of removing items from the list ?

ans:There are two method for removing items from the list that is pop() and clear().How list values and string values are identical ?

Ans: string values are always denoted in inverted commas.
     and list values are always denoted in square bracket.What are the difference between list and tupples ?

Ans: list are denoted in square bracket and list are mutable.
     tuples are denoted in parenthisis ans tuples are immutable.     How do you type a tuple value that only contains the integer 42 ?
Ans : it will writtern as int(42).How do you get list values from tuple form? How do you get a tuple values list form ?

Ans: suppose, list = [2,3,4,5,6] then we can convert list into tuple by using tuple(list).
# In[17]:


list = [2,3,4,5,6]


# In[18]:


list


# In[19]:


tuple(list)

Variable that "contain" list values are not necessarily lists themselves. instead, what do they  contain ?

Ans: they contain tuples also.How do you distinguish between copy.copy() and copy.deepcopy() ?

Ans:A shallow copy that means copy.copy() constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.

A deep copy that means copy.deepcopy () constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
thank you..!