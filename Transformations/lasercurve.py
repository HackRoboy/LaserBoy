import time
from comms import main

import math

x = range(0,2*math.Pi,0.1)

horz_deflection = math.cos(x)
vert_deflection = math.sin(x)

max_angle = 30

horz_angle = horz_deflection*max_angle + 150
vert_angle = vert_deflection*max_angle + 150

for i in range(0,len(x))

	main(horz_angle[i], vert_angle[i])
	time.sleep(1)