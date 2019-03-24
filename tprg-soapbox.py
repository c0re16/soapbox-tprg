import csv
import math
from math import radians
data = []
#file = str(input("FILENAME >>") or "soapboxes.csv")
file = "soapboxes.csv"

g = 9.8
ramplen = 0
rampangle = 0
tracklen  = 0

#<FUNKY STUFF>
def loadcsv(file):
	with open(file, 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			data.append(row)

def fg(m):
	return (m * 9.8)
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
	print("CAR #" , i ,"	MASS>>",m,"	STAT COEFF>>",us,chr(956),"	KIN COEFF>>",uk,chr(956))


	fRampStatic = (framp(fg(m),rampangle)-fframp(fg(m),rampangle,us))
	accel(fRampStatic)
	if accel(fRampStatic) <= 0 :
		print('DOESNT START TO ROLL\n')
	else:

		print("STARTS TO ROLL")

		fgsin0 = fg(m)*math.sin(radians(rampangle))
		fgcos0= fg(m)* math.cos(radians(rampangle))
		# print("FG(COS0)>>",round(fgcos0),3)

		# print("FG(SIN0)>>",round((fgsin0),3))
		
		FUKramp = fframp(fg(m),rampangle,uk)
		# print("FUKramp>>",round(FUKramp,3))
		
		FNETramp =  fgsin0 - FUKramp
		# print("FNETramp>>",round(FNETramp,3))
		
		ACCELramp = FNETramp/m
		# print("ACCEL>>",round(ACCELramp,5))

		time=math.sqrt((ramplen*2)/ACCELramp)
		# print("TIME>",round(time,3))

		TRACKvi = ACCELramp*time
		print("Velocity exiting ramp>>", round(TRACKvi,3), "m/s")

		FUKtrack = fg(m)*uk
		# print("FUKtrack>>",round(FUKtrack,4))

		FNETtrack = -FUKtrack
		# print("FNETtrack>>",round(FNETtrack,4))

		ACCELtrack = FNETtrack/m
		# print("ACCELtrack>>",round(ACCELtrack,4))

		STOPdistance = (-TRACKvi**2)/(2*ACCELtrack)
		
		if STOPdistance <15:
			print("DOESNT FINISH RACE")
			print("Stop distance>>", round(STOPdistance,3),"m\n")

		else:
			v15mtemp = TRACKvi**2 + (2 * (ACCELtrack) * tracklen)
			v15m = (v15mtemp**0.5)
			# print("v15m>>", round(v15m,4))
			TIMErampTOfinish =  (v15m- TRACKvi )/ACCELtrack
			# print("TIME RAMP TO FINISH>>", round(TIMErampTOfinish,4))

			print("TOTAL TIME>>",round(TIMErampTOfinish + time,4),"s")

			print('\n')






		


