#Fibonacci number module

def fib(n):
  result=[]
  if n==1:
    result=[1,]
  elif n==2:
    result=[1,1]
  else:
    result=fib(n-1)
    result.append(fib(n-1)[n-2]+fib(n-1)[n-3])              
  return result