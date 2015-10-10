__author__ = 'kkk'
from pico2d import*

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


open_canvas()

dice=Dice()

running =True

diceteam=[Dice() for i in range(6)]


for i in diceteam:
    i.frameyy=random.randint(0,5)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


while running:
    handle_events()
    for boy in diceteam:
        boy.update()
    clear_canvas()
    for boy in diceteam:
        boy.draw()
    update_canvas()
    delay(0.1)

close_canvas()
