##########################################
# Programmer: Tabitha Wong               #
# Date: April 15, 2019                   #
# Title: Chicken & Little                #
#                                        #
# P.S. I'm almost ashamed at how much    #
# fun I had drawing little chickens      #
##########################################

from tkinter import *
from random import *
from math import *
from time import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="grey80")
screen.pack()

#GLOOMY WEATHER
screen.create_rectangle(0,0,800,635, fill = "grey80", outline = "grey80")

#GROUND
screen.create_rectangle(0,625,800,800,fill = "chartreuse4", outline = "chartreuse4")

#MOUNTAIN
screen.create_polygon(-175,625,100,275,375,625, fill = "grey40")
screen.create_polygon(21,375,100,275,179,375,fill = "white")
tplus = 53
tx = 21
for tip in range(3):
    screen.create_polygon(tx, 375,tx+(tplus/2),383,tx+tplus,375,fill="white",outline = "white")
    tx = tx + tplus
dx = 75
dplus = 29
for dt in range(2):
    screen.create_line(dx,450,dx+dplus,426,width = 2,fill = "grey30")
    dx = dx + 2*dplus
screen.create_line(104,426,133,450,width = 2, fill = "grey30")
screen.create_line(162,426,191,450,width = 2, fill = "grey30")
dx2 = -5
for dt in range(2):
    screen.create_line(dx2,575,dx2+dplus,551,width = 2, fill = "grey30")
    dx2 = dx2 + 2*dplus
screen.create_line(24,551,53,575,width = 2, fill = "grey30")
screen.create_line(82,551,111,575,width = 2, fill = "grey30")

#SIGN
screen.create_rectangle(210,560,216,625, fill = "palegoldenrod")
screen.create_rectangle(163,560,263,590, fill = "palegoldenrod")
screen.create_text(213,575, text = "<-CHICKFEST;)", font = "Arial 10")

#HORIZON
screen.create_line(0,624,800,624,width = 2)

#GRASS
for g1 in range(25):
    gx1 = randint(0,800)
    gy1 = randint(630,800)
    gx2 = gx1 + 5
    gy2 = gy1 - 5
    gx3 = gx2
    gy3 = gy2
    gx4 = gx3 + 5
    gy4 = gy3 + 5
    gx5 = gx4
    gy5 = gy4
    gx6 = gx5 + 5
    gy6 = gy5 - 5
    gx7 = gx6
    gy7 = gy6
    gx8 = gx7 + 5
    gy8 = gy7 + 5
    screen.create_line(gx1,gy1,gx2,gy2, fill = "black")
    screen.create_line(gx3,gy3,gx4,gy4, fill = "black")
    screen.create_line(gx5,gy5,gx6,gy6, fill = "black")
    screen.create_line(gx7,gy7,gx8,gy8, fill = "black")

#CLOUD 1
zx = []
zy = []
zx.append(-100)
zy.append(-100)
for z in range(45):
    zx.append(randint(75,300))
    zy.append(randint(50,150))
    zxx = zx[z] + 70
    zyy = zy[z] + 50
    cloud1 = screen.create_oval(zx[z],zy[z],zxx,zyy, fill = "grey60", outline = "grey60")
    
#CLOUD 2
yx = []
yy = []
yx.append(-100)
yy.append(-100)
for y in range(45):
    yx.append(randint(450,650))
    yy .append(randint(250,390))
    yxx = yx[y] + 70
    yyy = yy[y] +50
    cloud2 = screen.create_oval(yx[y],yy[y],yxx,yyy, fill = "grey60", outline = "grey60")

word1 = screen.create_text(400,515, text = "The weather looks so glum.", font = "Arial 25")
screen.update()
screen.delete(word1)
sleep(2)

screen.create_text(400,515, text = "Hopefully we'll have blue skies again soon.", font = "Arial 25")
screen.update()
sleep(2)
    
#CHANGE TO WARM WEATHER
#SKY GRADIENT
skyy = [0,625*.25,625*.5,625*.75,625]
screen.create_rectangle(0,skyy[0],800,skyy[1], fill = "lightblue1", outline = "lightblue1")
screen.create_rectangle(0,skyy[1],800,skyy[2], fill = "paleturquoise1", outline = "paleturquoise1")
screen.create_rectangle(0,skyy[2],800,skyy[3], fill = "lightblue1", outline = "lightblue1")
screen.create_rectangle(0,skyy[3],800,skyy[4], fill = "paleturquoise1", outline = "paleturquoise1")

#GROUND
screen.create_rectangle(0,625,800,800,fill = "chartreuse4", outline = "chartreuse4")

#MOUNTAIN
screen.create_polygon(-175,625,100,275,375,625, fill = "grey40")
screen.create_polygon(21,375,100,275,179,375,fill = "white")
tplus = 53
tx = 21
for tip in range(3):
    screen.create_polygon(tx, 375,tx+(tplus/2),383,tx+tplus,375,fill="white",outline = "white")
    tx = tx + tplus
dx = 75
dplus = 29
for dt in range(2):
    screen.create_line(dx,450,dx+dplus,426,width = 2, fill = "grey30")
    dx = dx + 2*dplus
screen.create_line(104,426,133,450,width = 2, fill = "grey30")
screen.create_line(162,426,191,450,width = 2, fill = "grey30")
dx2 = -5
for dt in range(2):
    screen.create_line(dx2,575,dx2+dplus,551,width = 2, fill = "grey30")
    dx2 = dx2 + 2*dplus
screen.create_line(24,551,53,575,width = 2, fill = "grey30")
screen.create_line(82,551,111,575,width = 2, fill = "grey30")

#SIGN
screen.create_rectangle(210,560,216,625, fill = "palegoldenrod")
screen.create_rectangle(163,560,263,590, fill = "palegoldenrod")
screen.create_text(213,575, text = "<-CHICKFEST;)", font = "Arial 10")

#HORIZON
screen.create_line(0,624,800,624,width = 2)

#GRASS
for g1 in range(25):
    gx1 = randint(0,800)
    gy1 = randint(630,800)
    gx2 = gx1 + 5
    gy2 = gy1 - 5
    gx3 = gx2
    gy3 = gy2
    gx4 = gx3 + 5
    gy4 = gy3 + 5
    gx5 = gx4
    gy5 = gy4
    gx6 = gx5 + 5
    gy6 = gy5 - 5
    gx7 = gx6
    gy7 = gy6
    gx8 = gx7 + 5
    gy8 = gy7 + 5
    screen.create_line(gx1,gy1,gx2,gy2, fill = "black")
    screen.create_line(gx3,gy3,gx4,gy4, fill = "black")
    screen.create_line(gx5,gy5,gx6,gy6, fill = "black")
    screen.create_line(gx7,gy7,gx8,gy8, fill = "black")
    
#CLOUD 1
zx = []
zy = []
zx.append(-100)
zy.append(-100)
for z in range(45):
    zx.append(randint(75,300))
    zy.append(randint(50,150))
    zxx = zx[z] + 70
    zyy = zy[z] + 50
    cloud1 = screen.create_oval(zx[z],zy[z],zxx,zyy, fill = "white", outline = "white")
    
#CLOUD 2
yx = []
yy = []
yx.append(-100)
yy.append(-100)
for y in range(45):
    yx.append(randint(450,650))
    yy .append(randint(250,390))
    yxx = yx[y] + 70
    yyy = yy[y] +50
    cloud2 = screen.create_oval(yx[y],yy[y],yxx,yyy, fill = "white", outline = "white")
    
word2 = screen.create_text(400,515, text = "It's clear again!", font = "Arial 25")
screen.update()
sleep(2)
screen.delete(word2)
screen.update()

word3 = screen.create_text(400,515, text = "Something's coming...", font = "Arial 25")
screen.update()
screen.delete(word3)
sleep(2)
screen.update()

word4 = screen.create_text(400,515, text = "No, wait! Several things are coming!", font = "Arial 25")
screen.update()
sleep(2)
screen.delete(word4)
screen.update()   

#BABY BIRDS
#INITIAL VALUES AND EMPTY ARRAYS
numbirds = 15
birdx = []
birdxspeed = []
heady = []
body = []
wing = []
beak = []
leg1 = []
leg2 = []
foot1 = []
foot2 = []
head = []
eye = []

for i in range(0,numbirds):
    birdx.append(randint(750,800))
    birdxspeed.append(uniform(4,6))
    heady.append(randint(3,6))
    body.append(0)
    beak.append(0)
    leg1.append(0)
    leg2.append(0)
    foot1.append(0)
    foot2.append(0)
    wing.append(0)
    eye.append(0)
    head.append(0)

#ANIMATION
mbx = 750
for cheep in range(250):

    #MAMA BIRD
    msizex = 55
    msizey = 40
    mspeed = 6
    mhead1 = screen.create_line(mbx + 12,575,mbx + 22, 565, fill = "red", width = 4)
    mhead2 = screen.create_line(mbx + 21,575,mbx + 30, 560, fill = "red", width = 4)
    mhead3 = screen.create_line(mbx + 26,575,mbx + 34, 565, fill = "red", width = 4)
    mfoot1 = screen.create_line(mbx+18,625,mbx+28,625, width = 3)
    mfoot2 = screen.create_line(mbx+30,625,mbx+40,625, width = 3)
    mleg1 = screen.create_line(mbx+ 23, 580, mbx + 23, 625, width = 3)
    mleg2 = screen.create_line(mbx+ 33, 580, mbx + 33, 625, width = 3)
    mgobble = screen.create_oval(mbx - 1, 610,mbx+10,595,fill = "red", outline = "red")
    mbody = screen.create_oval(mbx, 610 - msizey, mbx + msizex, 610, fill = "saddlebrown", outline = "saddlebrown")
    mwing = screen.create_oval(mbx + 15,589,mbx + 45,600,fill = "sandybrown", outline = "black")
    mbeak = screen.create_polygon(mbx - 7,590, mbx + 4,594,mbx+4,586, fill = "yellow" , outline = "black")
    meye = screen.create_oval(mbx + 8, 578,mbx + 12, 588, fill = "black")
    mtext = 0
    mtext1 = 0
    mtext2 = 0
    if mbx < 630:
        mtext = screen.create_text(mbx - 10,540, text = "So what if Brenda's babies can catch fish!", font = "Arial 18")
    if mbx < 450:
        screen.delete(mtext)
        mtext1 = screen.create_text(mbx - 10,540, text = "Mine cluck louder than hers!", font = "Arial 18")
    if mbx < 250:
        screen.delete(mtext1)
        mtext2 = screen.create_text(mbx - 10,540, text = "Natural selection my tail-feathers...", font = "Arial 18")
    mbx = mbx - mspeed

    #BABY BIRDS
    for i in range(numbirds):
        foot1[i] = screen.create_line(birdx[i]+16,625,birdx[i]+10,625, width = 3)
        foot2[i] = screen.create_line(birdx[i]+23,625,birdx[i]+17,625, width = 3)
        leg1[i] = screen.create_line(birdx[i]+ 13, 605, birdx[i] + 13, 625, width = 3)
        leg2[i] = screen.create_line(birdx[i]+ 20, 605, birdx[i] + 20, 625, width = 3)
        head[i] = screen.create_line(birdx[i]+8,599,birdx[i]+12,599 - heady[i], fill ="red3",width = 3)
        body[i] = screen.create_oval(birdx[i],599,birdx[i]+27,617, fill = "white", outline = "white")
        wing[i] = screen.create_oval(birdx[i]+7,607,birdx[i]+20,611,fill = "red3", outline = "red3")
        eye[i] = screen.create_oval(birdx[i] + 5, 602, birdx[i]+8, 605, fill = "black")
        beak[i] = screen.create_polygon(birdx[i] - 4,609,birdx[i] + 3, 613, birdx[i] + 3, 605, fill = "yellow", outline = "black")
        birdx[i] = birdx[i] - birdxspeed[i]

    screen.update()
    sleep(0.03)
    
    screen.delete(mbody,mfoot1,mfoot2,mleg1,mleg2,mwing,mbeak,meye, mhead1,mhead2,mhead3,mgobble,mtext,mtext1,mtext2)
    for i in range(numbirds):
        screen.delete(body[i],leg1[i],leg2[i],eye[i],beak[i],foot1[i],foot2[i],head[i],wing[i])

#STOLEN GRIDLINES (SORRY)
##spacing = 50
##
##for x in range(0, 1000, spacing): 
##    screen.create_line(x, 25, x, 1000, fill="blue")
##    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N)
##
##for y in range(0, 1000, spacing):
##    screen.create_line(25, y, 1000, y, fill="blue")
##    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W)





