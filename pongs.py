import socket
s = socket.socket()
hostname = socket.gethostname()
port = 3466
s.bind(('', port))
s.listen(5)
p1pos = [20, 40]
p2pos = [680, 40]
ballpos = [640, 360]
c1, addr1 = s.accept()
c2, addr2 = s.accept()

while True:
    #print("hell")
    c1r = int(c1.recv(16).decode())
    c2r = int(c2.recv(16).decode())
    if c1r == -2184233:
        c1.send(str('%16s' %p2pos[1]).encode())
        c1.send(str('%16s' %ballpos[0]).encode())
        c1.send(str('%16s' %ballpos[1]).encode())
    else:
        p1pos[1] = c1r
    if c2r == -2184233:

        c2.send(str('%16s' %p2pos[1]).encode())
        c2.send(str('%16s' %ballpos[0]).encode())
        c2.send(str('%16s' %ballpos[1]).encode())
    else:
        p2pos[1] = c2r
    print(c1r)
    print(c2r)

c1.close()
c2.close()
