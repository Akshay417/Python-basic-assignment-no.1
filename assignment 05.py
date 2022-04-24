#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. What does an empty dictionary code look like?
# Ans:- empty dictionary code look like this: {}
dict = {}
type(dict)


# 2. What is the value of a dictionary value with the key 'foo' and the value 42?
#     

# In[2]:


{'foo':42}


# 3. What is the most significant distinction between a dictionary and a list?

# significant distinction between a dictionary and a list is :-
# 
#     List - values or atoms  are ordered.
#     dictionary - values or atoms in dictionary are unordered.

# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
# This will give us KeyError

# In[3]:


spam = {'bar':'100'}
spam ['foo']


# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

# In[4]:


# there is no difference
spam = {'cat':100}
'cat' in spam


# In[5]:


'cat' in spam.keys()


# 6.If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
# 
# 'cat' in spam checks whether there is a 'cat' key in the dictionary
# 
# 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.

# In[8]:


spam ={'cat':100}
'cat' in spam


# In[9]:


spam ={'cat':100}
'cat' in spam.values()


# 7. What is a shortcut for the following code?

# if color not in spam:
# 
# spam[color] = black

# In[7]:


#ans:-
spam ={'cat':100}
spam.setdefault('color','black')
spam


# 8. How do you 'pretty print' dictionary values using which module and function?

# In[10]:


import pprint


# In[11]:


dct_arr = [ {'Name': 'Ranjan', 'Age': '20', 'Country': 'USA'},
  {'Name': 'Joseph', 'Age': '40', 'Country': 'China'},
  {'Name': 'Ankit', 'Age': '45', 'Country': 'Rasia'},
  {'Name': 'nakul', 'Age': '32', 'Country': 'Japan'}
]


# In[12]:


# printing with pprint()
pprint.pprint(dct_arr)


# In[13]:


#Printing with print()
print(dct_arr)


# In[ ]:




