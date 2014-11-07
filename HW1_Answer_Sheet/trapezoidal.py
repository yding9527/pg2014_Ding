# Yifeng Ding	
# 2014-10-14
# Homework 1, problem 2, trapazoidal integration

import numpy as np

def integrate(f,dx=1):
  """Trapazoidal integration of function f, with spacing dx"""
  f=np.array(f)
  result=0.5*sum(dx*(f[1:]+f[:-1]))
  return result

#if __name__ == '__main__':

  #test with a flat function, of value 1
#  f = np.ones(11)

