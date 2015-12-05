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
    str=None

    def __init__(self):
        if Enamy.image==None:
            Enamy.image=[load_image('png\\mon-1.png'),load_image('png\\mon-2.png'),
                         load_image('png\\mon-3.png'),load_image('png\\mon-4.png'),
                          load_image('png\\mon-5.png'),load_image('png\\mon-6.png'),
                         load_image('png\\mon-7.png'),load_image('png\\mon-8.png'),
                         load_image('png\\mon-9.png'),load_image('png\\mon-10.png'),
                         load_image('png\\mon-11.png'),load_image('png\\mon-12.png'),
                         load_image('png\\mon-13.png'),load_image('png\\mon-14.png'),
                         load_image('png\\mon-15.png')]
        if map.Chracter.type==2 or map.Chracter.type==1:
            if map.turnnumber<80:
                self.number=random.randint(0,1+(int)(map.turnnumber/30))
            else : self.number=random.randint(0,4)
        if map.Chracter.type==3:
            if map.turnnumber<80:
                self.number=random.randint(5,6+(int)(map.turnnumber/30))
            else : self.number=random.randint(5,9)
        if map.Chracter.type==5:
            if map.turnnumber<70:
                self.number=random.randint(10,11+(int)(map.turnnumber/30))
            else : self.number=random.randint(10,13)
        if map.Chracter.type==20:
            self.number=14

        self.hplist=Stat_data["hplist"]
        self.dflist=Stat_data["dflist"]
        self.strlist=Stat_data["strlist"]
        if Enamy.blood==None:
            Enamy.blood=load_image("png\\Blood.png")
        if Enamy.armor==None:
            Enamy.armor=load_image("png\\armor.png")
        #if Enamy.str==None:
         #   Enamy.str=load_image("png\\armor.png")
        Enamy.Chracter_x, Enamy.Chracter_y=0,0
        if map.turnnumber<130:
            Enamy.hp=self.hplist[ self.number]-1+(int)(map.turnnumber/30)#적군 벨런스 조정
            Enamy.maxhp=self.hplist[ self.number]-1+(int)(map.turnnumber/30)#적군 벨런스 조정
        else :
            Enamy.hp=self.hplist[ self.number]+2
            Enamy.maxhp=self.hplist[ self.number]+2
        if map.turnnumber<70:
             Enamy.df=self.dflist[ self.number]-2+(int)(map.turnnumber/30)
             Enamy.str=self.strlist[ self.number]-2+(int)(map.turnnumber/30)
             Enamy.maxdf=self.dflist[ self.number]-2+(int)(map.turnnumber/30)
        else :
             Enamy.df=self.dflist[ self.number]
             Enamy.str=self.strlist[ self.number]
             Enamy.maxdf=self.dflist[ self.number]


    def draw(self):
        global battleturn
        Enamy.image[self.number].clip_draw(0,0,400,300,200,450);
        Enamy.blood.clip_draw(70*(Enamy.maxhp-1),0,70,99,800-437,600-144)
        Enamy.armor.clip_draw(84*(Enamy.maxdf-1),0,84,99,800-447,600-240)
       # Enamy.str.clip_draw(84*(Enamy.maxdf-1),0,84,99,800-447,600-240)
