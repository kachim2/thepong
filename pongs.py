import socket
s = socket.socket()
hostname = socket.gethostname()
port = 40674
s.bind(('', port))
s.listen(5)

c1, addr1 = s.accept()
print(c1)
c1.sendall(bytes(int(10)))

c2, addr2 = s.accept()
print(c2)
c2.sendall(bytes(int(10)))

c1.close()
c2.close()
