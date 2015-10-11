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

class Map():
    def __init__(self):
        self.image=[load_image('realmap(12).png'),load_image('realmap(8).png')]
        self.number=0
    def draw(self):
        if self.number==0:
          self.image[0].clip_draw(0,0,400,385,200,50)
        elif self.number==1:
            self.image[1].clip_draw(0,0,400,385,136,390)
        elif self.number==2:
            self.image[1].clip_draw(0,0,400,385,465,286)
        elif self.number==3:
            self.image[1].clip_draw(0,0,400,385,135/2-2,447)



open_canvas()


map =[Map() for i in range(3)]

map[1].number=1
map[2].number=2

running =True



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        if event.type == SDL_KEYDOWN and event.key==SDLK_a:
            for i in diceteam:
                i.frame=0




while running:
    handle_events()
    clear_canvas()
    for m in map:
        m.draw()
    update_canvas()
    delay(0.1)

close_canvas()
