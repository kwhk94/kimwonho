__author__ = 'kkk'
from pico2d import*

import random

class Dice():
    def __init__(self):
        self.image=load_image('DICE-2.png')
        self.frame=0
    def update(self):
        if(self.frame<21):
            self.frame=self.frame+1
    def draw(self):
         self.image.clip_draw((self.frame)*35,0,35,480,400,300)


open_canvas()

dice=Dice()


running =True


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
    dice.update()
    clear_canvas()
    dice.draw()
    update_canvas()
    delay(0.1)

close_canvas()
