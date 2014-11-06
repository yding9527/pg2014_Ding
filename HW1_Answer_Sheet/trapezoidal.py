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
  return result
