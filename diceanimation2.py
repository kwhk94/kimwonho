__author__ = 'kkk'
from pico2d import*

import random
import game_framework
import map

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



def enter():
    global diceteam
    diceteam=[Dice() for i in range(6)]
    for i in diceteam:
        i.frameyy=random.randint(0,5)



def exit():
    global diceteam
    del(diceteam)


def pause(): pass


def resume(): pass

def update():
    global diceteam
    for boy in diceteam:
        boy.update()


def draw():
    clear_canvas()
    for boy in diceteam:
        boy.draw()
    update_canvas()
    delay(0.05)