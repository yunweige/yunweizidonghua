import socket
HOST = '0.0.0.0'
PORT = 9000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    while True:
        print 'Got a conection from', addr
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data.upper())
        print 'Received...:', data


conn.close()
