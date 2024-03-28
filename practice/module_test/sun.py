#!/usr/bin/env python
# coding: utf-8

# In[1]:

x = 1
_x = 2
__x = 3  # 내부적으로 쓰겠다는 의미이다. # 접그을 할 수 있긴 하다.

def y():
    pass

def _y():
    pass

def __y():
    pass

#__all__ = ['_x','__x'] # 여기에들어가면, import 할 때 다 같이 불러와진다. 언더바 있는지 상관없이


# In[ ]: