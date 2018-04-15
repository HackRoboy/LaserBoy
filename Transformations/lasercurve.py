import time
from comms import main

import math
import numpy

x = numpy.arange(0,2*math.pi,0.3)

print(x)


horz_deflection = numpy.sin(x)
vert_deflection = numpy.cos(x)

max_angle = 25

horz_angle = horz_deflection*max_angle + 150
vert_angle = vert_deflection*max_angle + 150

print(horz_angle)
print(vert_angle)

while True:
	for i in range(0,len(x)):
	
	#print(".")

		main(horz_angle[i], vert_angle[i])
		time.sleep(0.3)