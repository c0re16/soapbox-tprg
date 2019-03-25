import csv
import math
from math import radians
data = [] #DECLARATIONS
file = str(input("FILENAME >>") or "soapboxes.csv")

# Soap box calculator. 
# Corey Ball (100626709) 
# TPRG1131 Section 20941 
# MAR 24, 2019 

# Develop a program that reads a data file where the first line
# gives information about the track, and the remaining lines give
# the details of the soapboxes, then determines the top speed
# and finish time of each soapbox.

# Ramp down force = mg sin (theta)
# Ramp perpendicular force = mg sin (theta)
# Static friction = normal force * coefficient of static friction
# Kinetic friction = normal force * coefficient of kinetic friction
# Net force = ramp perpendicular force - kinetic friction
# Ramp acceleration = net force / mass
# Time to end of ramp = root of x^2/a
# Exit velocity = ramp acceleration * time to end of ramp = track Vi
# Kinetic friction on track = mg * coefficient of kinetic friction
# Net force = Kinetic friction on track * -1
# Acceleration on track = net force / mass
# Distance travelled = (negative track vi ^2)/(2 * acceleration on track)
# Final velocity at end of track = root of (track vi squared + 2* track acceleration * track length)
# Time taken to finish = final velocity - track vi divided by track acceleration




g = 9.8
ramplen = 0
rampangle = 0
tracklen  = 0

#<FUNKY STUFF>
def loadcsv(file): #POPULATE DATA ARRAY
	with open(file, 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			data.append(row)

def fg(m):
	return (m * g)
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

# DISPLAY GIVENS GLOBAL
print(
	"RAMP LENGTH>>", ramplen, "		"
	"RAMP ANGLE>>", rampangle,"		"
	"TRACK LENGTH>>", tracklen,'\n')
	
for i in range(1,len(data)):
	# LOAD DATA FROM ROW INTO VARIABLES
	m = float(data[i][0])
	us = float(data[i][1])
	uk = float(data[i][2])
	# DISPLAY GIVENS
	print("CAR #" , i ,"	MASS>>",m,"	STAT COEFF>>",us,chr(956),"	KIN COEFF>>",uk,chr(956))


	fRampStatic = (framp(fg(m),rampangle)-fframp(fg(m),rampangle,us)) #CHECK IF IT'LL ROLL.
	accel(fRampStatic)
	if accel(fRampStatic) <= 0 :
		print('DOESNT START TO ROLL\n')
	else:

		print("STARTS TO ROLL")

		fgsin0 = fg(m)*math.sin(radians(rampangle)) #VERTICAL FORCE
		fgcos0= fg(m)* math.cos(radians(rampangle)) #HORIZONTAL FORCE
		FUKramp = fframp(fg(m),rampangle,uk) #FORCE OF KINETIC FRICTION
		FNETramp =  fgsin0 - FUKramp #NET FORCES ON RAMP
		ACCELramp = FNETramp/m #ACCELERATION ON RAMP
		time=math.sqrt((ramplen*2)/ACCELramp) #TIME TO REACH END OF RAMP
		TRACKvi = ACCELramp*time #VELOCITY AT END OF RAMP
		print("Velocity exiting ramp>>", round(TRACKvi,3), "m/s")
		FUKtrack = fg(m)*uk #FRICTION FORCE ON TRACK
		FNETtrack = -FUKtrack #NET FORCE ON TRACK
		ACCELtrack = FNETtrack/m #ACCELERATION ON TRACK
		STOPdistance = (-TRACKvi**2)/(2*ACCELtrack) #DISTANCE UNTIL CAR STOPS
		
		if STOPdistance <15: #CHECK IF IT FINISHES
			print("DOESNT FINISH RACE")
			print("Stop distance>>", round(STOPdistance,3),"m\n")

		else:
			v15m = math.sqrt(TRACKvi**2 + (2 * (ACCELtrack) * tracklen)) #VELOCITY AT FINISH LINE

			TIMErampTOfinish =  (v15m- TRACKvi )/ACCELtrack #TIME TAKEN TO COMPLETE TRACK FROM RAMP
			print("FINISH TIME>>",round(TIMErampTOfinish + time,4),"s") #TOTAL TIME FROM START
			print('\n')






		


