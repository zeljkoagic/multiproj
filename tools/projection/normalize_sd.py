# SD normalization by AS

from __future__ import division
import sys
import numpy as np

def clip(x):
    if x < 0:
        return 0.0
    elif x > 1:
        return 1.0
    else:
        return x
def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0
  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg
  return out

def rank(X):
    y=[str((i+1)/len(X)) for i in range(len(X))]
    return dict(zip(sorted(X),y))

def intrank(X):
    y=[str((i+1)) for i in range(len(X))]
    return dict(zip(sorted(X),y))

def quantilize(X):
    D={}
    SD=np.std(X)
    M=np.mean(X)
    Z=[clip(0.5 + float(x) - M / (2*SD)) for x in X]
    D_prime=dict(zip(X,Z))
    y=chunkIt(Z,3)
    for x in X:
        for chunk in y:
            if D_prime[x] in chunk:
                D[x]=str(np.array(chunk).mean())
    return dict(D)

def normalize(X):
    SD=np.std(X)
    M=np.mean(X)
    D=dict(zip(
            X,[str(clip(0.5 + float(x) - M / (2*SD))) for x in X]
           ))
    return dict(D) 

conll = [l.strip().split() for l in open(sys.argv[1]).readlines()]

sent = []

for c in conll:
    if len(c) < 2:
        for w in sent:
            numbers=[float(x.split(":")[1]) for x in w[8:]]
            #D=normalize(numbers)
            D=intrank(numbers)
            #D=quantilize(numbers)
            print("\t".join(w[:8] + [str(i) + ":" + D[numbers[i]] for i in range(len(numbers))])) 
        sent = []
    else:
        sent.append(c)
