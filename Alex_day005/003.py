import socket

HOST= '127.0.0.1'
PORT= 9000

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((HOST,PORT))

while True:
    user_input = raw_input("msg to send::").strip()
    if len(user_input) == 0 :continue
    c.sendall(user_input)
    return_data = c.recv(1024)
    print 'Receved: ', return_data

c.close()