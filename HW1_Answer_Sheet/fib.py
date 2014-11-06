#Yifeng Ding
#Fibonacci number module

def fib(n):
  """Function to return a series of N Fibonacci numbers
  
  Inputs: n
  number of Fibonacci numbers will be returned, range [1,Inf)
  
  Outputs: 
  a list of N Fibonacci numbers, starting with 1"""
  
  result=[]
  if n==1:
    result=[1,]
  elif n==2:
    result=[1,1]
  else:
    result=fib(n-1)
    result.append(fib(n-1)[n-2]+fib(n-1)[n-3])              
  return result
