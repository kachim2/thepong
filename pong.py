from socket import socket
import pygame
import socket
s = socket.socket()
hostname = socket.gethostname()
port = 3466

def sendn():
    print ("sending")
def cathn():
    print("catching")

p1pos = {20, 40}
p2pos = {680, 40}
ballpos = {640, 360}

s.listen(5)