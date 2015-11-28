__author__ = 'kkk'
from pico2d import*
import game_framework
import battlemap
import title
import map
import json
import random
global dice_num
global font


class E_stat():
    global statpng
    global statbar
    global enamy
    global font
    global smallfont
    global turnnumber
    image=None
    blood=None
    armor=None
    def __init__(self):
        if E_stat.image==None:
            E_stat.image=load_image("png\\statbar.png")
        if E_stat.blood==None:
            E_stat.blood=load_image("png\\Blood.png")
        if E_stat.armor==None:
            E_stat.armor=load_image("png\\armor.png")
        self.onoff=0;


    def draw(self):
        if self.onoff==0:
            self.image.clip_draw(0,0,159,250,800-80,600-120)
            self.blood.clip_draw(70*(battlemap.enamy.hp-1),0,70,99,800-122,600-49)
            self.armor.clip_draw(84*(battlemap.enamy.df-1),0,84,99,800-50,600-49)
            map.font.draw(800-150,600-130,'STR :')
            map.font.draw(800-40,600-130,"%d"%battlemap.enamy.str,color=(200,0,0))


class Stat_downside():
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
        if Stat_downside.image==None:
            Stat_downside.image=load_image("png\\statbar.png")
        if Stat_downside.blood==None:
            Stat_downside.blood=load_image("png\\Blood.png")
        if Stat_downside.armor==None:
            Stat_downside.armor=load_image("png\\armor.png")
        if Stat_downside.chracter==None:
            Stat_downside.chracter=load_image("png\\chracter.png")
        Stat_downside.damage=0
        self.onoff=0;
        self.total_frame=0
        self.time=0
        self.currenttime=0
        self.frame=0


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
        map.font.draw(800-150,600-190-355,'Gold :')
        map.font.draw(800-40,600-190-355,"%d"%map.chracter.gold,color=(0,0,200))
        map.font.draw(800-150,600-220-355,'AGI :')
        map.font.draw(800-40,600-220-355,"%d"%map.chracter.agi,color=(100,100,100))
        map.smallfont.draw(800-150,600-110-355,'Maxhp :')
        map.smallfont.draw(800-100,600-110-355,"%d"%map.chracter.hp,color=(200,0,0))
        self.chracter.clip_draw(0,0,89,119,800-200,600-200-355)