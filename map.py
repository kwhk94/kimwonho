__author__ = 'kkk'
from pico2d import*
import game_framework
import diceanimation2
import title

import random

class Dice():
    def __init__(self):
        self.image=load_image('DICE-4.png')
        self.frame=0
        self.xpos=random.randint(70,540)
        self.frameyy=0
    def update(self):
        if(self.frame<21):
            self.frame=self.frame+1
    def draw(self):
         self.image.clip_draw((self.frame)*140,283*self.frameyy,140,240,self.xpos,300)

global xpos,ypos
xpos,ypos=0,0

class Map():
    image = None

    global xpos,ypos
    def __init__(self):
        if Map.image==None:
            Map.image=[load_image('realmap (12).png'),load_image('realmap (8).png')]
        self.number=0

    def draw(self):
        global xpos,ypos
        if self.number==0:
          self.image[0].clip_draw(0,0,400,385,200+xpos,50+ypos)
        elif self.number==1:
            self.image[1].clip_draw(0,0,400,385,136+xpos,390+ypos)
        elif self.number==2:
            self.image[1].clip_draw(0,0,400,385,465+xpos,286+ypos)
        elif self.number==3:
            self.image[1].clip_draw(0,0,400,385,136-62+xpos,390+344+ypos)
        elif self.number==4:
            self.image[1].clip_draw(0,0,400,385,136+267+xpos,390+238+ypos)
        elif self.number==5:
            self.image[1].clip_draw(0,0,400,385,465+267+xpos,286+238+ypos)

class Move():
    global xpos,ypos
    stop,rightmove,leftmove,upmove,downmove=0,1,2,3,4
    def __init__(self):
        self.state=self.stop

    def Stop(self):
        xpos,ypos
        self.state=self.stop
    def Rightmove(self):
        global xpos,ypos
        xpos=xpos-1
        self.state=self.rightmove

    def Leftmove(self):
        global xpos,ypos
        xpos=xpos+1
        self.state=self.leftmove
    def Upmove(self):
        global xpos,ypos
        ypos=ypos-1
        self.state=self.upmove
    def Downmove(self):
        global xpos,ypos
        ypos=ypos+1
        self.state=self.downmove
    def update(self):
        self.handle_state[self.state](self)

    handle_state={
        stop:Stop,
        rightmove:Rightmove,
        leftmove:Leftmove,
        upmove:Upmove,
        downmove:Downmove
        }
class Chracter():
    image = None

    global xpos,ypos
    def __init__(self):
        if Chracter.image==None:
            Chracter.image=load_image('Chracter.png')
        self.number=0

    def draw(self):
         global xpos,ypos
         self.image.clip_draw(0,0,89,119,200+xpos,50+ypos)


def handle_events():
    global running
    global xpos,ypos
    global map
    global move
    Stop,Right,Left,UP,DOWN=0,1,2,3,4
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
             game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(title)
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_a):
                 game_framework.push_state(diceanimation2)
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_RIGHT):
                if move.state==move.stop :
                    move.state=move.rightmove
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_LEFT):
                if move.state==move.stop :
                    move.state=move.leftmove
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_UP):
                if move.state==move.stop :
                    move.state=move.upmove
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_DOWN):
                if move.state==move.stop :
                    move.state=move.downmove
            elif(event.type==SDL_KEYUP):
                move.state=move.stop





def enter():
    global map
    global move
    global chracter
    chracter=Chracter()
    move=Move()
    map=[Map() for i in range(6)]



def exit():
    global map
    del(map)


def pause():
    global dice_num
    for i in range(6):
         dice_num=[i]


def resume(): pass

def update():
    global map
    global move
    a=0
    move.update()
    map =[Map() for i in range(6)]
    for i in map:
        i.number=a
        a=a+1

def draw():
    global dice_num
    global chracter


    clear_canvas()
    global map

    for m in map:
         m.draw()
    chracter.draw()
    update_canvas()