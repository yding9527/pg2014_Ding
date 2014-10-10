# Yifeng Ding
# 2014-10-06
#
#Create a class to read discharge data
#[date, discharge] = data_inquire(self, year)
#

import datetime
import numpy as np
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
                  if yr.month == 2 and yr.day ==29:
                      continue

                  self.dates.append(yr)
                  self.disch.append(disch[dates.index(yr)])

      self.dates = np.array(self.dates)
      self.disch = np.array(self.disch)
      return self.dates, self.disch

  def hydro_plot(self):
      fig = plt.figure()
      dates, disch = self.reader()
      plt.plot(dates, disch)
      fig.suptitle('Hydrograph Over %d to %d'%((dates[0].year), (dates[-1].year)),fontsize=20)
      plt.xlabel('Time Series', fontsize=16)
      plt.ylabel('Discharge($m^3/s$)', fontsize=16)

  def annual_mean(self, year=None):
      if year is None: 
        print "No specific year indicated..."
      else:
        dates,disch = self.data_inquire(year)
        mean = np.zeros(365) 
        for iyear in year:
          idate,idisch = self.data_inquire(iyear)
          mean=mean+idisch

        mean = mean/float(len(year))
        self.mean = mean	
      return self.mean

  def compare_plot(self, year=None):
      if year is None: 
        print "No specific year indicated..."
      elif year == 1967 or year == 2014:
        print "Not enough samples within the year..."
      else:
        dates,disch = self.data_inquire(year)
        lst = np.arange(1968,2014).tolist()
        lst.remove(1980)
        lst.remove(1981)
        lst.remove(1982)
        lst.remove(1983)
        lst.remove(1984)
        m_disch = self.annual_mean(lst)
        plt.plot(dates,disch,'r-')	   
        plt.plot(dates,m_disch,'b-')	 

        dis=[]
        std_dv=np.zeros(365)
        for yr in lst:
          tmp_dat,tmp_dis = self.data_inquire(yr)
          dis.append(tmp_dis)
        for i in range(365):
          tmp = np.zeros(len(lst))                  
          for j in range(len(lst)):
            tmp[j]=dis[j][i]
          std_dv[i]=np.std(tmp)		

        plt.fill(dates,m_disch+abs(std_dv),'grey')
        plt.fill(dates,m_disch-abs(std_dv),'grey')
