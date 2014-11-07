<<<<<<< HEAD
# Yifeng Ding	
# 2014-10-14
# Homework 1, problem 2, trapazoidal integration

import numpy as np

def integrate(f,dx=1):
  """Trapazoidal integration of function f, with spacing dx"""
  f=np.array(f)
  result=0.5*sum(dx*(f[1:]+f[:-1]))
=======
#Yifeng Ding
#Trapezoidal integration

def integrate(f,dx=1):
  """Function can be used to compute the integral of a list of numbers.
  
  inputs:
  f:number list for integration
  dx:integration step, default set to be 1
  
  outputs:
  integral result of the input list, calculated with trapezoidal rule."""
  
  N=len(f)
  result=0.0
  for i in range(0,N-1):
    result=result+0.5*dx*(f[i]+f[i+1])
>>>>>>> 831d7bfa204effa9495ae85bafcfcaa148854f4a
  return result

#if __name__ == '__main__':

  #test with a flat function, of value 1
#  f = np.ones(11)

