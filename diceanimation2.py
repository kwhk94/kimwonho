__author__ = 'kkk'
from pico2d import*

import random
import game_framework
import json
import map



class Dice():
    image = None
    def __init__(self):
        if Dice.image==None:
            Dice.image=load_image('png\\DICE-4.png')
        self.frame=0
        self.xpos=random.randint(70,540)
        self.frameyy=0
    def update(self):
        if(self.frame<21):
            self.frame=self.frame+1
    def draw(self):
         self.image.clip_draw((self.frame)*140,283*(6-(self.frameyy)),140,240,self.xpos,300)




def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key==SDLK_a:
            for i in diceteam:
                i.frame=0
        elif event.type == SDL_KEYDOWN and event.key==SDLK_b:
             game_framework.pop_state()
        elif event.type == SDL_KEYDOWN and event.key==SDLK_c:
            num=0
            for i in diceteam:
                i.frame=0
                i.frameyy=random.randint(1,6)
                i.xpos=random.randint(50+70*num,50+90*num)
                num+=1
                dice_num=[(diceteam[i].frameyy for i in  range(map.chracter.hp))]
        elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_o):
             print(dice_num)



def enter():
    global diceteam
    global dice_num
    diceteam=[Dice() for i in range(map.chracter.hp)]

def exit():
    global diceteam
    del(diceteam)


def pause():
    global dice_num
    global chracter

def resume():
    global dice_num
    global chracter


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
    dice_num=[diceteam[i].frameyy for i in range(map.chracter.hp)]
    delay(0.03)