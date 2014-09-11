def file_reader(filename):
  f = open(filename)
  result=list()
  date=list()
  disch=list()
  for line in f.readlines():
    if not len(line) or line.startswith('#'):   
      continue           
    result.append(line) 
  for line in result:
    date.append(line.split()[2])
    disch.append(line.split()[3])
  return date,disch