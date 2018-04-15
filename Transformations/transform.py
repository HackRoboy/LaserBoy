#from IPython.display import display
import sympy as sy

import time
from comms import main

delta_vertikal = 240
delta_horizontal = 250

#Position = (x,y,z)
x = 200
y = 300
z = 1000

#T_laser_base


#sy.init_printing()

# declaring symbolic variables:
theta_1, theta_2 = sy.symbols("theta_1 theta_2", real=True)

# Building matrices and vectors:
T_base_1 = sy.Matrix([[sy.cos(-theta_1), -sy.sin(-theta_1), 0, 0],
                        [sy.sin(-theta_1), sy.cos(-theta_1), 0, 0],
                        [0, 0, 1, 88],
                        [0, 0, 0, 1]])
#print(T_base_1)
T_1_laser = sy.Matrix([[sy.cos(-theta_2), -sy.sin(-theta_2), 0, 0],
                          [0, 0, -1, 0],
                          [sy.sin(-theta_2), sy.cos(-theta_2), 0, 0],
                          [0, 0, 0, 1]])
#print(T_1_laser)
T_laser_base = T_base_1*T_1_laser
T_base_laser = T_laser_base.inv()
print(T_base_laser)

p_object = sy.Matrix([x,y,z,0])
print(p_object)
p_laser = p_object - sy.Matrix([delta_vertikal, delta_horizontal, z, 0])
print(p_laser)

print("this should be zero:")
Zero = sy.simplify(T_base_laser*p_object-p_laser)                     


res = sy.solve(Zero[1:3])

print(res)
print(".....")
#print(res[1])

angle_1 = []
angle_2 = []
j = 0

for i in res : 
	
	angle_1.append(i[theta_1] + 150)
	angle_2.append(i[theta_2] + 150)
	j = j +1
	

a = res[0]

#print(list(a.keys()))

#print(a[theta_1])

main(30, 30)

print(angle_1)
print(angle_2)
time.sleep(2)
main(angle_1[0], angle_2[0])
#main(angle_1[1], angle_2[1])
#main(angle_1[2], angle_2[2])
#main(angle_1[3], angle_2[3])