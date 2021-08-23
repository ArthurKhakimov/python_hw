#!/usr/bin/env python3
import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    data=input("Type Something(q or Q to exit:)")
    if data=='q' or data=='Q':
        client_socket.close()
        break
    else:
        client_socket.sendto(data.encode('utf-8'),("192.168.2.100", 5000))
        newdata=client_socket.recvfrom(512)
        print(newdata[0].decode('utf-8'))
