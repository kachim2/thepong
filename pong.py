import pygame as pg
import socket
s = socket.socket()
port = 3466
p1pos = [20, 40]
p2pos = [680, 40]
ballpos = [640, 360]
def sendn():
    p1posx = p1pos[1]
    msg = '%16s' %p1posx
    s.send(msg.encode())
def cathn():
    s.send(str('%16s' %-2184233).encode())

    p2pos[1] = int(s.recv(16))
    ballpos[0] = int(s.recv(16))
    ballpos[1] = int(s.recv(16))

s.connect(('127.0.0.1', port))
pg.init()
window = pg.display.set_mode((640, 480))
pg.display.set_caption("pong")
kliknieto_x = False
while not kliknieto_x:
    sendn()
    cathn()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            kliknieto_x = True
    window.fill((0,0,0))








    pg.display.flip()
    print(p2pos[1])








s.close()
pg.close()