import csv
import math
from math import radians
data = []
# file = str(input("FILENAME >>") or "soapboxes.csv")
file = "soapboxes.csv"
vi = 0
a = 0
vf = 0
t = 0
us = 0
uk = 0
n = 0
fg = 0
ff = 0
m = 0
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
def accel(uk, theta):
	return(
		(9.81* math.sin(radians(theta))) - (uk*9.81*math.cos(radians(theta)))
		)
def framp(fg,theta):
	return(
		fg*math.cos(radians(theta))
		)
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
	"ramplen>>", ramplen, "		"
	"rampangle>>", rampangle,"		"
	"tracklen>>", tracklen,'\n')
	
for i in range(1,len(data)):
	m = float(data[i][0])
	us = float(data[i][1])
	uk = float(data[i][2])
	print("MASS>>",m,"		STAT COEFF>>",us,"		KIN COEFF>>",uk)
	if accel(us,rampangle) <= 0:
		print("nah u aint movin\n")
	else:
		print("ya u boogyin")
		print(
			round(
				accel(uk,rampangle)
				,3)
			,'m/s^2 acceleration')


		print(
			round(
				math.sqrt(
					2*accel(uk,rampangle)*ramplen
					)
				,3)
			,"m/s at end of ramp\n")
		


