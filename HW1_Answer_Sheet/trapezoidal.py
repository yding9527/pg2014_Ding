def integrate(f,dx=1):
  N=len(f)
  result=0.0
  for i in range(0,N-1):
    result=result+0.5*dx*(f[i]+f[i+1])
  return result
