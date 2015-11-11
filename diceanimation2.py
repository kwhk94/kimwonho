__author__ = 'kkk'
from pico2d import*

import random
import game_framework
import json
import map



class Dice():
    image = None
    TIME_PER_ACTION=0.8
    ACTION_PER_TIME=1.0/TIME_PER_ACTION
    FRAMES_PER_ACTION=22
    ON,OFF=1,0

    def __init__(self):
        if Dice.image==None:
            Dice.image=load_image('png\\DICE-4.png')
        self.total_frame=0
        self.frame=0
        self.xpos=random.randint(70,540)
        self.number=0
        self.ONOFF=self.OFF
        self.time=0
        self.currenttime=0

    def update(self):
         self.time = get_time() - self.currenttime
         self.currenttime += self.time
         self.total_frame+=Dice.FRAMES_PER_ACTION*Dice.ACTION_PER_TIME*self.time
         if self.ONOFF==self.OFF:
            self.frame=int(self.total_frame)%22
            if self.frame==21:
                self.ONOFF=self.ON

    def draw(self):
         self.image.clip_draw(1+(self.frame)*140,283*(6-(self.number)),140,240,self.xpos,300)




def handle_events():
    global running
    global dice_num
    global startdice
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key==SDLK_a:
            for i in diceteam:
                i.frame=0
                i.total_frame=0
                i.currenttime=get_time()
                i.ONOFF=i.OFF
        elif event.type == SDL_KEYDOWN and event.key==SDLK_b:
             game_framework.pop_state()
        elif event.type == SDL_KEYDOWN and event.key==SDLK_c:
            num=0
            for i in diceteam:
                i.total_frame=0
                i.currenttime=get_time()
                i.frame=0
                i.number=random.randint(1,6)
                i.xpos=random.randint(50+70*num,50+90*num)
                num+=1
                i.ONOFF=i.OFF
                dice_num=[diceteam[i].number for i in  range(map.chracter.hp)]
        elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_o):
             print(dice_num)



def enter():
    global diceteam
    global dice_num
    global current_time
    map.turntype=0
    map.turnnumber+=1
    diceteam=[Dice() for i in range(map.chracter.hp)]
    dice_num=[]
    current_time=get_time()

def exit():
    global diceteam
    del(diceteam)


def pause():
    global dice_num
    global chracter

def resume():
    global dice_num
    global chracter


def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time



def update():
    global diceteam
    for boy in diceteam:
           boy.update()



def draw():
    global dice_num
    clear_canvas()
    for dice in diceteam:
        dice.draw()
    update_canvas()
    dice_num=[diceteam[i].number for i in range(map.chracter.hp)]
    delay(0.03)