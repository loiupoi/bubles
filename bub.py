from tkinter import *
from random import randint
from time import sleep, time
bubch=10
bub_id=list()
bubR=list()
bubSPD=list()
minR=10
maxR=30
maxSPD=10
gap=100
HG=500
WD=800
window=Tk()
window.title('Охота за МлаДенЦаМи')
c=Canvas(window, width=WD, height=HG, bg='darkblue')
c.pack()
ship1=c.create_polygon(5,5,5,25,30,15,fill='red')
ship2=c.create_oval(0,0,30,30, outline='red')
shipR=15
mX=WD/2
mY=HG/2
c.move(ship1, mX,mY)
c.move(ship2, mX,mY)
shipS=10
def move_ship(event):
    if event.keysym=='Up':
        c.move(ship1, 0,-shipS)
        c.move(ship2, 0,-shipS)
    elif event.keysym=='Down':
        c.move(ship1, 0,shipS)
        c.move(ship2, 0,shipS)
    elif event.keysym=='Left':
        c.move(ship1, -shipS,0)
        c.move(ship2, -shipS,0)
    elif event.keysym=='Right':
        c.move(ship1, shipS,0)
        c.move(ship2, shipS,0)
c.bind_all('<Key>',move_ship)

def create_bub():
    x=WD+gap
    y=randint(0,HG)
    r=randint(minR,maxR)
    idl=c.create_oval(x-r, y-r, x+r, y+r, outline='white')
    bub_id.append(idl)
    bubR.append(r)
    bubSPD.append(randint(1, maxSPD))

def move_b():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bubSPD[i], 0)

def getcoor(id_num):
    pos=c.coords(id_num)
    x=(pos[0]+pos[2])/2
    y=(pos[1]+pos[3])/2
    return x,y

def del_b(i):
    del bubR[i]
    del bubSPD[i]
    c.delete(bub_id[i])
    del bub_id[i]
def cb():
    gap * 2
    maxSPD * 2
    for bub in range(len(bub_id)-1,-1,-1):
        x,y=getcoor(bub_id[bub])
        if x < -gap:
            del_b(bub)
while True:
    if randint(1, bubch)==1:
        create_bub()
    move_b()
    cb()
    window.update()
    sleep(0.01)

