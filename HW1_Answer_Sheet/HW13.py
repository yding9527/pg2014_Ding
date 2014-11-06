#Yifeng Ding
#Readin discharge data

import datetime

def file_reader(filename):
  """Readin data from the file, discharge.dat, return a list of dates and discharge states.
  
  inputs:filename
  
  outputs:date list and discharge states"""
  
  f = open(filename)
  result=list()
  date=list()
  dates=list()
  disch=list()
  for line in f.readlines():
      if not len(line) or line.startswith('#'):   
	        continue           
      result.append(line) 
  for line in result:
      date.append(line.split()[2])
      disch.append(line.split()[3])
   
  for line in date:
      time=line.split('-')
      year=int(time[0])
      month=int(time[1])
      day=int(time[2])

      times=datetime.date(year, month, day)

      dates.append(times)
  return dates,disch
