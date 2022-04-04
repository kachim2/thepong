import pygame as pg
import socket
s = socket.socket()
port = 3466
p1pos = [20, 40]
p2pos = [1240, 40]
ballpos = [640, 360]
points1 = 0
points2 = 0
def sendn():
    p1posx = p1pos[1]
    msg = '%16s' %p1posx
    s.send(msg.encode())
def cathn():
    s.send(str('%16s' %-2184233).encode())

    p2pos[1] = int(s.recv(16))
    ballpos[0] = int(s.recv(16))
    ballpos[1] = int(s.recv(16))
    points1 = int(s.recv(16))
    points2 = int(s.recv(16))

s.connect(('130.162.41.221', port))
pg.init()
window = pg.display.set_mode((1280, 720))
pg.display.set_caption("pong")
kliknieto_x = False
while not kliknieto_x:
    sendn()
    cathn()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            kliknieto_x = True
    window.fill((0,0,0))

    p1pos[1] = pg.mouse.get_pos()[1]
    pg.draw.rect(window, (128, 0, 150), pg.Rect(p1pos[0], p1pos[1], 20, 140))
    pg.draw.rect(window, (128, 0, 150), pg.Rect(p2pos[0], p2pos[1], 20, 140))
    pg.draw.rect(window, (128, 0, 150), pg.Rect(ballpos[0]-20, ballpos[1], 20, 20))

    font = pg.font.SysFont(None, 48)
    #point1img = font.render(str(points1), True, (128, 0, 21))
    #point2img = font.render(str(points2), True, (128, 0, 21))
    #window.blit(point1img, (20, 20))
    #window.blit(point2img, (400, 20))
    pg.display.flip()
    #print(p2pos[1])
    #print(points1)
    






s.close()
pg.close()
