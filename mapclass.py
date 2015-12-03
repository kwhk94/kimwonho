__author__ = 'kkk'
import json
from pico2d import*
import game_framework
import map



class Map():
    image = None
    maponoff=None
    global etc
    etc_file= open('etc\\etc.txt','r')
    etc=json.load(etc_file)
    etc_file.close()

    def __init__(self):
        if Map.image==None:
            Map.image=[load_image('png\\realmap (12).png'),load_image('png\\realmap (8).png'),
                       load_image('png\\realmap (1).png'),load_image('png\\realmap (2).png'),
                       load_image('png\\realmap (3).png'),load_image('png\\realmap (4).png'),
                       load_image('png\\realmap (5).png'),load_image('png\\realmap (6).png'),
                       load_image('png\\realmap (7).png'),load_image('png\\realmap (10).png'),
                       load_image('png\\realmap (9).png')]
        self.number=0
        self.mapnumber=1
        if Map.maponoff==None:
            Map.maponoff=0



    def draw(self):
        if self.number==0:
          self.image[self.mapnumber].clip_draw(0,0,400,385,etc["mapx"][0]+map.xpos,etc["mapy"][0]+map.ypos)
        elif self.number==1:
            self.image[self.mapnumber].clip_draw(0,0,400,385,etc["mapx"][1]+map.xpos,etc["mapy"][1]+map.ypos)
        elif self.number==2:
            self.image[self.mapnumber].clip_draw(0,0,400,385,etc["mapx"][2]+map.xpos,etc["mapy"][2]+map.ypos)
        elif self.number==3:
            self.image[self.mapnumber].clip_draw(0,0,400,385,etc["mapx"][3]+map.xpos,etc["mapy"][3]+map.ypos)
        elif self.number==4:
            self.image[self.mapnumber].clip_draw(0,0,400,385,etc["mapx"][4]+map.xpos,etc["mapy"][4]+map.ypos)
        elif self.number==5:
            self.image[self.mapnumber].clip_draw(0,0,400,385,etc["mapx"][5]+map.xpos,etc["mapy"][5]+map.ypos)
        elif self.number==6:
            self.image[self.mapnumber].clip_draw(0,0,400,385,etc["mapx"][6]+map.xpos,etc["mapy"][6]+map.ypos)
        elif self.number==7:
            self.image[self.mapnumber].clip_draw(0,0,400,385,etc["mapx"][7]+map.xpos,etc["mapy"][7]+map.ypos)
