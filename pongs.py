import socket
import math
s = socket.socket()
hostname = socket.gethostname()
port = 3466
s.bind(('', port))
s.listen(5)
p1pos = [20, 40]
p2pos = [1240, 40]
points1 = 0
points2 = 0
ballpos = [640, 360]
c1, addr1 = s.accept()
c2, addr2 = s.accept()
alpharot = 75
while True:

    c1r = int(c1.recv(16).decode())
    c2r = int(c2.recv(16).decode())
    if c1r == -2184233:
        c1.send(str('%16s' %p2pos[1]).encode())
        c1.send(str('%16s' %int(ballpos[0])).encode())
        c1.send(str('%16s' %int(ballpos[1])).encode())
        c1.send(str('%16s' %int(points2)).encode())
        c1.send(str('%16s' %int(points1)).encode())
    else:
        p1pos[1] = c1r
    if c2r == -2184233:

        c2.send(str('%16s' %p1pos[1]).encode())
        c2.send(str('%16s' %int(1280-ballpos[0])).encode())
        c2.send(str('%16s' %int(ballpos[1])).encode())
        c2.send(str('%16s' %int(points1)).encode())
        c2.send(str('%16s' %int(points2)).encode())
    else:
        p2pos[1] = c2r
    



    if ballpos[1] <= 0:
        alpharot = 180 - alpharot
    if ballpos[0] >= 1280-20 or ballpos[0] <= 0:
        alpharot = 360 - alpharot
    if ballpos[0] > p2pos[0]-20:
        if ballpos[1] >= p2pos[1]-20 and ballpos[1] <= p2pos[1]+140:
            alpharot = 360 - alpharot
        else:
           points1 += 1
           ballpos = [640, 360]
           alpharot = 75 
    if ballpos[0] < p1pos[0]+20:
        if ballpos[1] >= p1pos[1]-20 and ballpos[1] <= p1pos[1]+140:
            alpharot = 360 - alpharot
        else:
           points2 += 1 
           ballpos = [640, 360]
           alpharot = 75
    if ballpos[1] >= 700:
        alpharot = 180 - alpharot
    ballpos[0] += math.sin(math.radians(alpharot))*10
    ballpos[1] -= math.cos(math.radians(alpharot))*10
    #print(p1pos[1])
    #print(p2pos[1])

    #print(c1r)
    #print(c2r)
    
c1.close()
c2.close()
