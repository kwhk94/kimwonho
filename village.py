__author__ = 'kkk'
__author__ = 'kkk'
from pico2d import*

import random
import game_framework
import json
import map



class Dice():
    image = None
    global battleturn
    TIME_PER_ACTION=1
    ACTION_PER_TIME=1.0/TIME_PER_ACTION
    FRAMES_PER_ACTION=22
    ON,OFF=1,0

    def __init__(self):
        if Dice.image==None:
            Dice.image=load_image('png\\DICE-4.png')

        self.frame=0
        self.xpos=random.randint(70,540)
        self.number=0
        self.total_frame=0
        self.time=0
        self.currenttime=0

    def update(self):
         global battleturn
         global turntime
         global time_num
         self.time = get_time() - self.currenttime
         self.currenttime += self.time
         self.total_frame+=Dice.FRAMES_PER_ACTION*Dice.ACTION_PER_TIME*self.time
         if battleturn==2:  #주사위를 굴리는 단계
            self.frame=int(self.total_frame)%22
            if self.frame==21:
                turntime=time_num
                battleturn=3

    def draw(self):
         self.image.clip_draw(1+(self.frame)*140,283*(6-(self.number)),140,240,self.xpos,150)


class Stat():
    global statpng
    global statbar
    global font
    global smallfont
    global turnnumber

    image=None
    blood=None
    armor=None
    chracter=None
    global battletrun

    def __init__(self):
        if Stat.image==None:
            Stat.image=load_image("png\\statbar.png")
        if Stat.blood==None:
            Stat.blood=load_image("png\\Blood.png")
        if Stat.armor==None:
            Stat.armor=load_image("png\\armor.png")
        if Stat.chracter==None:
            Stat.chracter=load_image("png\\chracter.png")
        Stat.damage=0
        self.onoff=0;
        self.total_frame=0
        self.time=0
        self.currenttime=0
        self.frame=0



    def update(self):
        global battleturn
        global turntime
        if battleturn==1 :
            for i in range(map.chracter.str):
                if  dice_num[i]>=5: #주사위 성공 체크 숫자
                    stat.damage+=1
                if i==map.chracter.str-1:
                    turntime=time_num
                    battleturn=2


    def draw(self):
        global battleturn
        global turntime
        global time_num
        self.image.clip_draw(0,0,159,250,800-80,600-120-355)
        self.blood.clip_draw(70*(map.chracter.hp-1),0,70,99,800-122,600-49-355)
        self.armor.clip_draw(84*(map.chracter.df-1),0,84,99,800-50,600-49-355)
        map.font.draw(800-150,600-130-355,'STR :')
        map.font.draw(800-40,600-130-355,"%d"%map.chracter.str,color=(200,0,0))
        map.font.draw(800-150,600-160-355,'LUK :')
        map.font.draw(800-40,600-160-355,"%d"%map.chracter.luk,color=(0,200,0))
        map.font.draw(800-150,600-190-355,'INT :')
        map.font.draw(800-40,600-190-355,"%d"%map.chracter.int,color=(0,0,200))
        map.font.draw(800-150,600-220-355,'AGI :')
        map.font.draw(800-40,600-220-355,"%d"%map.chracter.agi,color=(100,100,100))
        map.smallfont.draw(800-150,600-110-355,'Maxhp :')
        map.smallfont.draw(800-100,600-110-355,"%d"%map.chracter.hp,color=(200,0,0))
        self.chracter.clip_draw(0,0,89,119,800-200,600-200-355)






def handle_events():
    global running
    global dice_num
    global startdice
    global stat
    global battleturn
    global turntime

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
        elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_i):
                 stat.onoff= not stat.onoff
        elif event.type == SDL_KEYDOWN and event.key==SDLK_c:
            if  battleturn==0 or battleturn==5:
                num=0
                stat.currentime=get_time()
                turntime=time_num
                for i in diceteam:
                    i.total_frame=0
                    i.currenttime=get_time()
                    i.frame=0
                    i.number=random.randint(1,6)
                    i.xpos=random.randint(50+70*num,50+90*num)
                    num+=1
                    dice_num=[diceteam[i].number for i in  range(map.chracter.str)]
                battleturn=1
        elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_o):
             print(dice_num)






def enter():
    global diceteam
    global dice_num
    global current_time
    global enamy
    global stat
    global battleturn
    global e_stat
    global time_num
    global turntime
    turntime=0
    time_num=0
    stat=Stat()
    map.turntype=0
    map.turnnumber+=1
    battleturn=0
    diceteam=[Dice() for i in range(map.chracter.luk)]
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
    global stat
    global enamy
    global time_num
    frametime=get_frame_time()
    time_num+=frametime
    for boy in diceteam:
           boy.update()
    stat.update()



def draw():
    global dice_num
    global enamy
    global diceteam
    global time_num
    global battleturn
    global e_stat
    #print("%f,%f"%(battleturn,stat.damage))
    clear_canvas()
    if battleturn>0:
        for dice in diceteam:
            dice.draw()
    stat.draw()




    update_canvas()
    dice_num=[diceteam[i].number for i in range(map.chracter.luk)]

    delay(0.03)