#!/usr/bin/env python3

# Полученные от клиента данные перевдим в строку. При нахождении в строке подстроки ADD, записываем пару в словарь.
# При запросе клиента, имя ищем в первую очередь из словаря, если там нет уже запрашиваем через gethostbyname.
# В пару мест добавил обработку исключений, чтоб при ошибочном вводе сервер не падал и выдавал соответсвующие ошибки.


import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(('',5000))
print ("DNS Server listening on port 5000:")
manual_records = {}
error_message = "Incorrect command format. Example: ADD HOST:IP"
accept_message = "Data recorded"
while True:
    data,address = server_socket.recvfrom(512)
    data_str = data.decode('utf-8')
    print (address, ":said", data_str)
    if data_str.find("ADD ") == 0:
        try:
            host_name, host_ip = data_str[4:].split(":")
        except:
            server_socket.sendto(error_message.encode('utf-8'),address)
        else:
            manual_records[host_name] = host_ip
            server_socket.sendto(accept_message.encode('utf-8'),address)
            print(manual_records)
    else:
        if data_str in manual_records.keys():
            answer = manual_records[data_str]
        else:    
            try:
                answer = socket.gethostbyname(data_str)
            except socket.gaierror as e:
                answer = str(e)
        server_socket.sendto(answer.encode('utf-8'),address)
