# -*- coding: utf-8 -*-
"""Задание кандидату. Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13WXQCD7EnXo32-eYkjqNFOAqJ9xdPb87

Task #1.
"""

def isPal (a, b):
  if sorted(a) == sorted(b):
    return 'true'
  else:
    return 'false'

"""Task #2"""

def compress(seq):
    tmp, seq = list(seq[:1]), seq[1:]
    parts = [tmp] if tmp else []

    for ch in seq:
        if ch in tmp:
            tmp.append(ch)
        else:
            tmp = [ch]
            parts.append(tmp)
    compress = ''.join('{}{}'.format(part[0], len(part)) for part in parts)
    if len(compress) < len(seq):
        return compress
    else:
        return seq

"""Task #3"""

import numpy as np
arr=np.random.randint(1,5000,20)
file=open("num.txt","w")
file.write(str(arr))
file.close()

