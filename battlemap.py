__author__ = 'kkk'
from pico2d import*

import random
import game_framework
import json
import map
import enamyclass
import statclass
import gameover
import Youwin


class Dice():
    image = None
    global battleturn
    TIME_PER_ACTION=1
    ACTION_PER_TIME=1.0/TIME_PER_ACTION
    FRAMES_PER_ACTION=22
    ON,OFF=1,0
    sound=None

    def __init__(self):
        if Dice.image==None:
            Dice.image=load_image('png\\DICE-4.png')
        self.frame=0
        self.xpos=random.randint(70,540)
        self.ypos=0
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

    def draw(self):
         global dicebgm
         if self.frame==0:
             dicebgm.play()

         self.image.clip_draw(1+(self.frame)*140,283*(6-(self.number)),140,240,self.xpos,100+self.ypos*100)



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
        elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_i):
                 stat.onoff= not stat.onoff
        elif event.type == SDL_KEYDOWN and event.key==SDLK_a: #전투 초기화
            if  battleturn==0 or battleturn==7:
                num=0
                stat.currentime=get_time()
                turntime=time_num
                for i in diceteam:
                    i.total_frame=0
                    i.currenttime=get_time()
                    i.frame=0
                    i.number=random.randint(1,6)
                    i.xpos=random.randint(50+70*(num%6),50+90*(num%6))
                    num+=1
                    dice_num=[diceteam[i].number for i in  range(map.chracter.str)]
                battleturn=1
        elif  (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
            if map.chracter.type==20 and battleturn==8:
                game_framework.push_state(Youwin)
            if battleturn==8:
                game_framework.pop_state()




def battleupdate():
    global battleturn,turntime,t_time,time_num,dice_num,enamy_dice
    global stat,diceteam,chracter,sword,shield
    if battleturn==1 :
            for i in range(map.chracter.str):
                if  dice_num[i]>=5: #주사위 성공 체크 숫자
                    stat.damage+=1
                if i==map.chracter.str-1:
                    turntime=time_num
                    battleturn=2
    if battleturn==2:  #주사위를 굴리는 단계
            for self in diceteam :
                self.frame=int(self.total_frame)%22
                if self.frame==21:
                     turntime=time_num
                     battleturn=3
    if battleturn==4:
            if time_num-t_time>0.5: #2초씩 데미지계산
                if stat.damage>0:
                    if enamy.df>0:
                        enamy.df-=1
                        shield.set_volume(125)
                        shield.play()
                        shield.set_volume(24)
                    else :
                        enamy.hp-=1
                        sword.set_volume(125)
                        sword.play()
                        sword.set_volume(24)
                    stat.damage-=1
                    if enamy.hp==0: #경험치 초과로인한 레벨업
                        map.chracter.gold+=enamy.maxhp
                        map.chracter.exp+=enamy.maxhp
                        battleturn=8
                    t_time=time_num
                elif stat.damage==0:
                    enamy.df=enamy.maxdf
                    num=0
                    for i in enamy_dice:
                        i.number=random.randint(1,6)
                        i.xpos=random.randint(50+70*(num%6),50+90*(num%6))
                        num+=1
                    dice_num=[enamy_dice[i].number for i in  range(enamy.str)]
                    for i in range(enamy.str):
                        if  dice_num[i]>=5: #주사위 성공 체크 숫자
                            e_stat.damage+=1
                        if i==enamy.str-1:
                            for i in enamy_dice:
                                i.frame=0
                                i.total_frame=0
                                i.currenttime=get_time()
                                i.frame=0
                            turntime=time_num
                            battleturn=5

    if battleturn ==5:
        for self in enamy_dice :
                self.frame=int(self.total_frame)%22
                if self.frame==21:
                     turntime=time_num
                     t_time=turntime
                     battleturn=6
    if battleturn==6:
            if time_num-t_time>0.5: #2초씩 데미지계산
                if e_stat.damage>0:
                    if map.chracter.df>0:
                        map.chracter.df-=1
                        shield.play()
                    else :
                        map.chracter.hp-=1
                        sword.play()
                    e_stat.damage-=1
                    t_time=time_num
                elif e_stat.damage==0:
                    map.chracter.df=map.chracter.maxdf
                    battleturn=7
    if battleturn==8: #레벨업에따른 체력 상승
        if map.chracter.maxhp<3:
            map.chracter.exp-=2
            map.chracter.hp+=1
            map.chracter.maxhp+=1
        elif map.chracter.maxhp<=5:
            if map.chracter.exp>(map.chracter.hp-2)*2:
                map.chracter.exp-=(map.chracter.hp-2)*2
                map.chracter.hp+=1
                map.chracter.maxhp+=1

        elif map.chracter.maxhp<12 :
            if map.chracter.exp>(map.chracter.hp-6)*3+10:
                map.chracter.exp-=(map.chracter.hp-6)*3+10
                map.chracter.hp+=1
                map.chracter.maxhp+=1




def battledraw():
    global battleturn,turntime,t_time,time_num
    if battleturn>=3 and battleturn<=4  and time_num-turntime>1: #일정시간이 지난후 데미지계산
                map.font.draw(800-250,600-420,"%d"%stat.damage,color=(250,250,250))
                map.font.draw(800-330,600-380,'Damage :',color=(255,100,100))
                if battleturn==3:
                        battleturn=4
                        t_time=time_num
    if battleturn>=6 and battleturn<=7  and time_num-turntime>1: #일정시간이 지난후 데미지계산
                map.font.draw(800-250,600-420,"%d"%e_stat.damage,color=(250,250,250))
                map.font.draw(800-330,600-380,'Damage :',color=(255,100,100))


def enter():
    global diceteam, dice_num,current_time,battleturn,enamy_dice
    global enamy,stat,battlturn,e_stat,sword,shield,bgm,dicebgm
    global time_num  #지속적인 게임 시간
    global turntime #턴이 지나갈때마다의 순간 시간
    global backP
    if map.chracter.type==2:
        backP=load_image("png\\dungen2.jpg")
    elif map.chracter.type==3:
        backP=load_image("png\\castle.jpg")
    elif map.chracter.type==5:
        backP=load_image("png\\tower.jpg")
    elif map.chracter.type==20:
        backP=load_image("png\\castle.jpg")
    bgm=load_music('etc\\bgm.ogg')
    bgm.set_volume(18)
    bgm.repeat_play()
    turntime=0
    time_num=0

    sword=load_wav('etc\\sword.ogg')
    shield=load_wav('etc\\defend.ogg')
    dicebgm=load_wav('etc\\dice.ogg')
    dicebgm.set_volume(10)
    sword.set_volume(125)
    shield.set_volume(128)
    e_stat=statclass.E_stat()
    stat=statclass.Stat_downside()
    enamy=enamyclass.Enamy()
    map.turntype=0
    map.turnnumber+=1
    battleturn=0
    diceteam=[Dice() for i in range(map.chracter.str)]
    enamy_dice=[Dice() for i in range(enamy.str)]
    dice_num=[]
    current_time=get_time()

def exit():
    # global diceteam
    # global enamy
    # del(diceteam)
    # del(enamy)
    pass

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
    global enamy,enamy_dice
    global time_num
    frametime=get_frame_time()
    time_num+=frametime
    for boy in diceteam:
           boy.update()
    for boy in enamy_dice:
           boy.update()
    battleupdate()



def draw():
    global dice_num
    global enamy,enamy_dice
    global diceteam
    global time_num
    global battleturn
    global e_stat
    global backP
    #print("%f,%f"%(battleturn,stat.damage))
    clear_canvas()
    backP.draw_to_origin(0,0)
    if battleturn>0 and battleturn<5:
         num=0
         for dice in diceteam:
            dice.ypos=1*((int)(num/6))
            num+=1
            dice.draw()
    if battleturn>=5 and battleturn<8:
        num=0
        for dice in enamy_dice:
            dice.ypos=1*((int)(num/6))
            num+=1
            dice.draw()
    battledraw()
    enamy.draw()
    stat.draw()
    e_stat.draw()
    if map.chracter.hp==0:
        game_framework.push_state(gameover)
    if battleturn==8:
         map.bigfont.draw(200,100,"PRESS SPACE!",color=(230,0,0))
    if battleturn==9:
        map.bigfont.draw(200,100,"LEVEL UP!",color=(230,0,0))
    if battleturn==0:
        map.bigfont.draw(200,100,"PRESS A!",color=(230,0,0))
    update_canvas()

    delay(0.03)