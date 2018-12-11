
# coding: utf-8

# In[1]:



from __future__ import division 
import vbcode
from struct import pack, unpack


# In[9]:


def encode_number(number):   
    bytes_list = []
    while True:
        bytes_list.insert(0, number % 128)
        if number < 128:
            break
        number = number // 128
    bytes_list[-1] += 128
    return pack('%dB' % len(bytes_list), *bytes_list)
vbcode.encode_number(777)


# In[3]:


def encode(numbers):    
    bytes_list = []
    for number in numbers:
        bytes_list.append(encode_number(number))
    return b"".join(bytes_list)


# In[4]:


def decode(bytestream):
    n = 0
    numbers = []
    bytestream = unpack('%dB' % len(bytestream), bytestream)
    for byte in bytestream:
        if byte < 128:
            n = 128 * n + byte
        else:
            n = 128 * n + (byte - 128)
            numbers.append(n)
            n = 0
    return numbers


# In[10]:


vbcode.encode([777,6789])


# In[6]:


vbcode.decode(b'\x06\x89')

