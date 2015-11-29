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


class Enamy():
    image = None
    global xpos,ypos
    global Stat_data
    Stat_file= open('etc\\enamy.txt','r')
    Stat_data=json.load(Stat_file)
    Stat_file.close()

    blood=None
    armor=None

    def __init__(self):
        if Enamy.image==None:
            Enamy.image=[load_image('png\\mon-1.png'),load_image('png\\mon-2.png'),
                         load_image('png\\mon-3.png'),load_image('png\\mon-4.png')]
        self.number=random.randint(0,3)
        self.hplist=Stat_data["hplist"]
        self.dflist=Stat_data["dflist"]
        self.strlist=Stat_data["strlist"]
        if Enamy.blood==None:
            Enamy.blood=load_image("png\\Blood.png")
        if Enamy.armor==None:
            Enamy.armor=load_image("png\\armor.png")
        Enamy.Chracter_x, Enamy.Chracter_y=0,0
        Enamy.hp=self.hplist[ self.number]-1+(int)(map.turnnumber/100)#적군 벨런스 조정
        Enamy.maxhp=self.hplist[ self.number]-1+(int)(map.turnnumber/100)#적군 벨런스 조정
        Enamy.df=self.dflist[ self.number]-1+(int)(map.turnnumber/100)
        Enamy.str=self.strlist[ self.number]-1+(int)(map.turnnumber/100)
        Enamy.maxdf=self.dflist[ self.number]-1+(int)(map.turnnumber/100)

    def draw(self):
        global battleturn
        Enamy.image[self.number].clip_draw(0,0,400,300,200,450);
        Enamy.blood.clip_draw(70*(Enamy.hp-1),0,70,99,800-440,600-140)
        Enamy.armor.clip_draw(84*(Enamy.maxdf-1),0,84,99,800-440,600-240)