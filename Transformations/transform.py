#from IPython.display import display
import sympy as sy

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

display(Zero)
#Zero[3] = 0

sy.solve(Zero[1:3])

#print("Vector of Unkowns xx.T = ")
#xx = sy.Matrix(list(T_base_laser.atoms(sy.Symbol)))
#display(xx.T_base_laser)
#print("For equation HH.xx = mm, HH = ")
#HH = KTM[:2, :].jacobian(xx)  # calculate the derivative for each unknown
#display(HH)