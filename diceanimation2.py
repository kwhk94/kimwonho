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

        self.frame=0
        self.xpos=random.randint(70,540)
        self.number=0
        self.ONOFF=self.OFF
        self.total_frame=0
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
    TIME_PER_ACTION=0.8
    ACTION_PER_TIME=1.0/TIME_PER_ACTION
    FRAMES_PER_ACTION=22

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


    def update(self):
        global battletrun
        self.time = get_time() - self.currenttime
        self.currenttime += self.time
        self.total_frame+=Dice.FRAMES_PER_ACTION*Dice.ACTION_PER_TIME*self.time
        if battletrun==1 :
            for i in range(map.chracter.str):
                if  dice_num[i]>=5:
                    Stat.damage+=1
                if i==map.chracter.str-1:
                    battletrun+=1


    def draw(self):
        if self.onoff==0:
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
            if battletrun>=2:
                map.font.draw(800-250,600-420,"%d"%Stat.damage,color=(100,100,100))
                map.font.draw(800-330,600-380,'Damage :',color=(100,100,100))





def handle_events():
    global running
    global dice_num
    global startdice
    global stat
    global battletrun
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
            if  battletrun==0:
                num=0
                for i in diceteam:
                    i.total_frame=0
                    i.currenttime=get_time()
                    i.frame=0
                    i.number=random.randint(1,6)
                    i.xpos=random.randint(50+70*num,50+90*num)
                    num+=1
                    i.ONOFF=i.OFF
                    dice_num=[diceteam[i].number for i in  range(map.chracter.str)]
                battletrun+=1
        elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_o):
             print(dice_num)

class Enamy():
    image = None
    global xpos,ypos

    def __init__(self):
        Stat_file= open('etc\\Stat.txt','r')
        Stat_data=json.load(Stat_file)
        Stat_file.close()
        if Enamy.image==None:
            Enamy.image=[load_image('png\\mon-1.png'),load_image('png\\mon-2.png'),
                         load_image('png\\mon-3.png'),load_image('png\\mon-4.png')]
        self.number=random.randint(0,3)
        Enamy.Chracter_x, Enamy.Chracter_y=0,0
        Enamy.hp=Stat_data["HP"]
        Enamy.maxhp=Stat_data["HP"]
        Enamy.df=Stat_data["DF"]
        Enamy.str=Stat_data["STR"]
        Enamy.agi=Stat_data["AGI"]
        Enamy.luk=Stat_data["LUK"]
        Enamy.int=Stat_data["INT"]

    def draw(self):
         Enamy.image[0].clip_draw(0,0,400,300,200,450);




def enter():
    global diceteam
    global dice_num
    global current_time
    global enamy
    global stat
    global battletrun
    stat=Stat()
    enamy=Enamy()
    map.turntype=0
    map.turnnumber+=1
    battletrun=0;
    diceteam=[Dice() for i in range(map.chracter.str)]
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
    for boy in diceteam:
           boy.update()
    stat.update()



def draw():
    global dice_num
    global enamy
    clear_canvas()
    for dice in diceteam:
        dice.draw()
    enamy.draw()
    stat.draw()




    update_canvas()
    dice_num=[diceteam[i].number for i in range(map.chracter.str)]

    delay(0.03)