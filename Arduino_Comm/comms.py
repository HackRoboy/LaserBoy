import socket
import struct

# set IP to local
#UDP_IP = '127.0.0.1'

#ESP's IP
UDP_IP = '192.168.1.220'
UDP_PORT = 4210

# create socket
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

def main(angle_theta_1, angle_theta_2) :
	
	angle_theta_1 = int(angle_theta_1)
	angle_theta_2 = int(angle_theta_2)
	
	mylist = [angle_theta_1, angle_theta_2]
	
	# remember negative values
	
	#b_angle_theta_1 = angle_theta_1.to_bytes(1,'big')
	#b_angle_theta_2 = angle_theta_2.to_bytes(1,'big')
	
	MESSAGE = struct.pack('>HH',angle_theta_1, angle_theta_2)
	
	print(MESSAGE)
	
	# convert & concatenate
	#MESSAGE = (angle_theta_1 & 0xFF) << 8 | (angle_theta_2 & 0xFF)
	
	#MESSAGE = (b_angle_theta_1 & 0xFF) << 8 | (b_angle_theta_2 & 0xFF)
	
	#send
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	
if __name__ == "__main__":
    # execute only if run as a script
    main(270,256)
	
	