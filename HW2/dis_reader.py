# Yifeng Ding
# 2014-10-06
#
#Create a class to read discharge data
#[date, discharge] = data_inquire(self, year)
#

import datetime
import matplotlib.pyplot as plt

class Discharge(object):

  def __init__(self,filename):
    self.name=filename

  def reader(self):
    f = open(self.name)
    result=list()
    date=list()
    dates=list()
    disch=list()
    for line in f.readlines():
        if not len(line) or line.startswith('#') :   
  	        continue           
        result.append(line) 
    for line in result:
        if line.split()[0] == 'USGS' and len(line.split()) >3 :  
            date.append(line.split()[2])
            disch.append(float(line.split()[3])*0.0283168)
    
    for line in date:
        time=line.split('-')
        if len(time) == 3:
            year=int(time[0])
            month=int(time[1])
            day=int(time[2])
 
            times=datetime.date(year, month, day)
 
            dates.append(times)

    return dates, disch


  def data_inquire(self,year=None):
      dates, disch = self.reader()    
      self.dates = list()
      self.disch = list()
      if year is None:
  	    self.dates, self.disch = dates, disch
      else: 
          for yr in dates:
              if yr.year == year:
                  self.dates.append(yr)
                  self.disch.append(disch[dates.index(yr)])

      fig = plt.figure()
      plt.plot(self.dates, self.disch)
      fig.suptitle('Hydrograph Over %d'%year, fontsize=20)
      plt.xlabel('Time Series', fontsize=16)
      plt.ylabel('Discharge($m^3/s$)', fontsize=16)
      return self.dates, self.disch
