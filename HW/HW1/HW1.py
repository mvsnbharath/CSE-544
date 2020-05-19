#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import math

allPossibilities =[(5,10**2),(5,10**3),(5,10**4),(5,10**5),(20,10**2),(20,10**3),(20,10**4),(20,10**5)]
#allPossibilities =[(5,10**2)]

def atleastOneDiscardedIPhone(n,N):
    atleastOneCorrectSequence = 0
    for i in range(N):
        myList = list(range(1,n+1))
        random.shuffle(myList)
        if atLeastOneCorrectPresent(myList,n):
            atleastOneCorrectSequence+=1
    
    print ("For(n,N):=({},{}),the approximated probability is {}".format(n,N,atleastOneCorrectSequence/N))  
    return atleastOneCorrectSequence


def atLeastOneCorrectPresent(myList,n):
    for i in range(1,n+1):
        if myList[i-1]==i:
            return True
    return False


# In[2]:


for permutation in allPossibilities:
    n,N = permutation[0],permutation[1]
    atleastOneDiscardedIPhone(n,N)


# In[ ]:




