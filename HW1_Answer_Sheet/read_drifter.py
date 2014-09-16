import time

def read_drifter(fname):
	f=open(fname)

	names=[]
	dic={}

	for line in f.readlines():
		data=line.split()
		if not len(data)==0 and data[0] == 'Waypoint':
			names.append(data[1])

	for name in names:
		f=open(fname)
		coord=[]
		while 1:
			line=f.readline()
			lines=line.split()
			if len(lines) == 7  and lines[1]==name and lines[0] == 'Track' :
				f.readline()
				f.readline()
				f.readline()
				while 1:
					line=f.readline()
					lines=line.split()
					if not len(lines) == 0:
						lat=float(lines[1][1:3])+(float(lines[2])%100.0)/60.0
						lon=float(lines[3][1:3])+(float(lines[4])%100.0)/60.0
						
						coord.append((float(int(lat*10000))/10000,float(int(lon*10000))/10000)) 

					else: 
						break
					dic[name]=coord
				break
			if not line:
				break
           
	return dic
