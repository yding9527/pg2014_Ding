def read_drifter(fname):
	f=open(fname)
	ff=open(fname)

	names=[]

	for line in f.readlines():
		data=line.split()
		if not len(data)==0 and data[0] == 'Waypoint':
			names.append(data[1])

	for name in names:
		f=open(fname)
		line=f.readline()
		lines=line.split()
		if name == lines[1] and 'Track' == lines[0]:
			f.readline()
			f.readline()
			f.readline()
			line=f.readline()
			print line
			lines=line.split()
			print lines[0]
			




#for name in names:
#	for line in ff.readlines():
#		data=line.split()
#		if not len(data)==0 and data[0] == 'Track' and data[1] == name:
#			line2=ff.readline()
#			print line2
#				data=line2.split()
#				print data[0]
#			line2=ff.readline()
#			print line2
#				data=line2.split()
#				print data[0]
#			line2=ff.readline()
#			print line2
#				data=line2.split()
#				print data[0]
#					print line2
#					print type(line2)
#					print 2

#					data2=line2.split()
#					points=[]
#					if not len(data)==0 and data[0] == 'Trackpoint':
#						print line2
#						lat=float(data[1][1:3])+(float(data[2])%100.0)/60.0
#						lon=float(data[3][1:3])+(float(data[4])%100.0)/60.0
                        
#						points=points.append((lon,lat))
#						print points                          
						
                      
            
