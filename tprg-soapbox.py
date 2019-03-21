import csv
import math
from math import radians
data = []
# file = str(input("FILENAME >>") or "soapboxes.csv")
file = "soapboxes.csv"

g = 9.81
ramplen = 0
rampangle = 0
tracklen  = 0

#<FUNKY STUFF>
def loadcsv(file):
	with open(file, 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			data.append(row)
def vf(vi,a,t):
	return  vi + a*t
def distanc_eq1():
	return (0.5(vf + vi))*t
def distanc_eq2():
	return (
		(vi * t) + (0.5(a * (t **2)))
		)
def vf_sq():
	return (
		(vi ** 2) + (2 * a * x)
		) 
def fg(m):
	return (m * 9.81)
def accel(f):
	return(
		f/m

		)
def framp(fg,theta):
	return(
		fg*math.sin(radians(theta))
		)
def fframp(fg,theta,uk):
	return(
		fg*math.cos(radians(theta))*uk
		)
def normforce(m):
	return (m * 9.81)
def friction(us,framp):
	return (us*framp)

# </FUNKY STUFF>

# START OF ACTUAL CODE HERE
loadcsv(file)
# PUT HEADERS IN VAIABLES
ramplen = float(data[0][0])
rampangle= float(data[0][1])
tracklen = float(data[0][2])


print(
	"RAMP LENGTH>>", ramplen, "		"
	"RAMP ANGLE>>", rampangle,"		"
	"TRACK LENGTH>>", tracklen,'\n')
	
for i in range(1,len(data)):
	m = float(data[i][0])
	us = float(data[i][1])
	uk = float(data[i][2])
	print("MASS>>",m,"		STAT COEFF>>",us,chr(956),"		KIN COEFF>>",uk,chr(956))


	fRampStatic = (framp(fg(m),rampangle)-fframp(fg(m),rampangle,us))
	accel(fRampStatic)
	if accel(fRampStatic) <= 0 :
		print('not going anywhere')
	else:
		print("going somewhere")
		fRampKinetic = (framp(fg(m),rampangle)-fframp(fg(m),rampangle,uk))
		aEndRamp = accel(fRampKinetic)
		print(aEndRamp)
		vEndRamp= math.sqrt(2 * aEndRamp * ramplen)
		print(vEndRamp)






		


