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

def main(angle_phi, angle_delta) :
	
	angle_phi = int(angle_phi)
	angle_delta = int(angle_delta)
	
	mylist = [angle_phi, angle_delta]
	
	# remember negative values
	
	#b_angle_phi = angle_phi.to_bytes(1,'big')
	#b_angle_delta = angle_delta.to_bytes(1,'big')
	
	MESSAGE = struct.pack(b'BB',angle_phi, angle_delta)
	
	# convert & concatenate
	#MESSAGE = (angle_phi & 0xFF) << 8 | (angle_delta & 0xFF)
	
	#MESSAGE = (b_angle_phi & 0xFF) << 8 | (b_angle_delta & 0xFF)
	
	#send
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	
if __name__ == "__main__":
    # execute only if run as a script
    main(45,45)
	
	