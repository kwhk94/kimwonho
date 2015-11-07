__author__ = 'kkk'
from pico2d import*
import game_framework
import diceanimation2
import title
import json
import random
global dice_num
global font

class Dice():
    def __init__(self):
        self.image=load_image('png\\DICE-4.png')
        self.frame=0
        self.xpos=random.randint(70,540)
        self.frameyy=0
    def update(self):
        if(self.frame<21):
            self.frame=self.frame+1
    def draw(self):
         self.image.clip_draw((self.frame)*140,283*self.frameyy,140,240,self.xpos,300)

global xpos,ypos
xpos,ypos=0,0

class Map():
    image = None
    maponoff=None
    global xpos,ypos
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
                       load_image('png\\realmap (7).png'),load_image('png\\realmap (9).png')]
        self.number=0
        self.mapnumber=1
        if Map.maponoff==None:
            Map.maponoff=0



    def draw(self):
        global xpos,ypos
        if self.number==0:
          self.image[self.mapnumber].clip_draw(0,0,400,385,etc["mapx"][0]+xpos,etc["mapy"][0]+ypos)
        elif self.number==1:
            self.image[self.mapnumber].clip_draw(0,0,400,385,etc["mapx"][1]+xpos,etc["mapy"][1]+ypos)
        elif self.number==2:
            self.image[self.mapnumber].clip_draw(0,0,400,385,etc["mapx"][2]+xpos,etc["mapy"][2]+ypos)
        elif self.number==3:
            self.image[self.mapnumber].clip_draw(0,0,400,385,etc["mapx"][3]+xpos,etc["mapy"][3]+ypos)
        elif self.number==4:
            self.image[self.mapnumber].clip_draw(0,0,400,385,etc["mapx"][4]+xpos,etc["mapy"][4]+ypos)
        elif self.number==5:
            self.image[self.mapnumber].clip_draw(0,0,400,385,etc["mapx"][5]+xpos,etc["mapy"][5]+ypos)

class Tile():
      global xpos,ypos
      x,y=[],[]
      global etc_file
      global timer
      ring_image=None
      etc_file= open('etc\\etc.txt','r')
      etc=json.load(etc_file)
      etc_file.close()
      TileType={
          0:etc["TileType"]["0"],
          1:etc["TileType"]["1"],
          2:etc["TileType"]["2"],
          3:etc["TileType"]["3"],
          4:etc["TileType"]["4"],
          5:etc["TileType"]["5"],
          6:etc["TileType"]["6"],
          7:etc["TileType"]["7"],
          8:etc["TileType"]["8"],
          9:etc["TileType"]["9"]
      }
      def __init__(self):
          for i in range(6):
                    Tile.x.append([etc["mapx"][i]+etc["tilexsize"][j]+xpos for j in range(7)])
          for i in range(6):
                    Tile.y.append([etc["mapy"][i]+etc["tileysize"][j]+ypos for j in range(7)])
          Tile.type=[self.TileType[i] for i in range(10)]
          if Tile.ring_image==None:
                Tile.ring_image=load_image('png\\ring.png')
          self.time=0

      def update(self):

           global xpos,ypos
           for i in range(6):
              for j in range(7):
                  Tile.x[i][j]=etc["mapx"][i]+etc["tilexsize"][j]+xpos
                  Tile.y[i][j]=etc["mapy"][i]+etc["tileysize"][j]+ypos

           for j in range(6):
               for i in range(10):
                   if map[j].mapnumber==i:
                        Tile.type[j]=self.TileType[i]
           if timer%4==0:
               self.time+=1


      def draw(self):
          global chracter
          global mouse_x,mouse_y
          for j in range(6):
           for i in range(7):
             if Tile.x[j][i]<chracter.state[0]+150 and Tile.x[j][i]>chracter.state[0]-150 \
                     and Tile.y[j][i]<chracter.state[1]+150 and Tile.y[j][i]>chracter.state[1]-150 and \
                 Tile.type[j][i]!=0 :
              self.ring_image.clip_draw(62*(self.time%4),0,64,66,Tile.x[j][i],Tile.y[j][i])
          #self.ring_image.clip_draw(62*(self.time%4),0,64,66,mouse_x,mouse_y)

class Stat():
    global statpng
    global statbar
    global font


    def __init__(self):
        self.image=load_image("png\\statbar.png")
        self.blood=load_image("png\\Blood.png")
        self.armor=load_image("png\\armor.png")
        self.onoff=0;
    def draw(self):
        if self.onoff==0:
            self.image.clip_draw(0,0,159,250,800-80,600-120)
            self.blood.clip_draw(70*(chracter.hp-1),0,70,99,800-122,600-49)
            self.armor.clip_draw(84*(chracter.df-1),0,84,99,800-50,600-49)
            font.draw(800-150,600-120,'STR :')
            font.draw(800-40,600-120,"%d"%chracter.str,color=(200,0,0))
            font.draw(800-150,600-150,'LUK :')
            font.draw(800-40,600-150,"%d"%chracter.luk,color=(0,200,0))
            font.draw(800-150,600-180,'INT :')
            font.draw(800-40,600-180,"%d"%chracter.int,color=(0,0,200))
            font.draw(800-150,600-210,'AGI :')
            font.draw(800-40,600-210,"%d"%chracter.agi,color=(100,100,100))


class Move():
    global xpos,ypos
    stop,rightmove,leftmove,upmove,downmove=0,1,2,3,4
    def __init__(self):
        self.state=self.stop

    def Stop(self):
        xpos,ypos
        self.state=self.stop
    def Rightmove(self):
        global xpos,ypos
        if xpos>-100:
         xpos=xpos-2
        self.state=self.rightmove

    def Leftmove(self):
        global xpos,ypos
        if xpos<100:
         xpos=xpos+2
        self.state=self.leftmove
    def Upmove(self):
        global xpos,ypos
        if ypos>-600:
         ypos=ypos-2
        self.state=self.upmove
    def Downmove(self):
        global xpos,ypos
        if ypos<20:
         ypos=ypos+2
        self.state=self.downmove
    def update(self):
        self.handle_state[self.state](self)



    handle_state={
        stop:Stop,
        rightmove:Rightmove,
        leftmove:Leftmove,
        upmove:Upmove,
        downmove:Downmove
        }

class Chracter():
    image = None
    state=[200+xpos,50+ypos]
    global xpos,ypos
    def __init__(self):
        Stat_file= open('etc\\Stat.txt','r')
        Stat_data=json.load(Stat_file)
        Stat_file.close()
        if Chracter.image==None:
            Chracter.image=load_image('png\\Chracter.png')
        self.number=0
        Chracter.Chracter_x, Chracter.Chracter_y=0,0
        Chracter.hp=Stat_data["HP"]
        Chracter.df=Stat_data["DF"]
        Chracter.str=Stat_data["STR"]
        Chracter.agi=Stat_data["AGI"]
        Chracter.luk=Stat_data["LUK"]
        Chracter.int=Stat_data["INT"]


    def update(self):
        global xpos,ypos
        global tile
        global mouse_x,mouse_y
        global map
        Chracter.state=[200+xpos+ Chracter.Chracter_x,50+ypos+Chracter.Chracter_y]
        for j in range(6):
           for i in range(7):
             if tile.x[j][i]<chracter.state[0]+150 and tile.x[j][i]>chracter.state[0]-150 \
                     and tile.y[j][i]<chracter.state[1]+150 and tile.y[j][i]>chracter.state[1]-150 \
                     and Tile.type[j][i]!=0:#캐릭터의 주위 타일
                 if mouse_x<tile.x[j][i]+25 and mouse_x>tile.x[j][i]-25 and mouse_y< tile.y[j][i]+25 and mouse_y>tile.y[j][i]-25 :
                    Chracter.Chracter_x+= tile.x[j][i]-Chracter.state[0]
                    Chracter.Chracter_y+=  tile.y[j][i]-Chracter.state[1]
                    mouse_x=-100
                    mouse_y=-100
                 if map[j].maponoff==0:
                    map[j].maponoff=1;
                    map[j].mapnumber=random.randint(2,9)



    def draw(self):
         global xpos,ypos
         self.image.clip_draw(0,0,89,119,Chracter.state[0],Chracter.state[1])


def handle_events():
    global running
    global xpos,ypos
    global map
    global move
    global tile
    global stat
    global mouse_x,mouse_y
    global pausenum
    global dice_num
    Stop,Right,Left,UP,DOWN=0,1,2,3,4
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
             game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(title)
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_a):
                 game_framework.push_state(diceanimation2)
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_RIGHT):
                if move.state==move.stop :
                    move.state=move.rightmove
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_LEFT):
                if move.state==move.stop :
                    move.state=move.leftmove
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_UP):
                if move.state==move.stop :
                    move.state=move.upmove
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_DOWN):
                if move.state==move.stop :
                    move.state=move.downmove
            elif(event.type==SDL_KEYUP):
                move.state=move.stop
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_p):
                if pausenum==1: pausenum=0
                elif pausenum==0:pausenum=1
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_o):
                 print(diceanimation2.dice_num)
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_i):
                 stat.onoff= not stat.onoff
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_q):
                 print(chracter.hp)
        if (event.type,event.button)==(SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT):
             global mouse_x,mouse_y
             mouse_x,mouse_y=event.x,599-event.y





def enter():
    global map
    global move
    global chracter
    global tile
    global pausenum
    global mouse_x,mouse_y
    global dice_num
    global stat
    global font
    global timer
    timer=0
    font=load_font('etc\\font.ttf',30)
    stat=Stat()
    pausenum=0
    countumber=0
    map =[Map() for i in range(6)]
    for i in map:
        i.number=countumber
        countumber=countumber+1
    map[0].maponoff=1
    map[0].mapnumber=0
    mouse_x,mouse_y =0,0
    tile=Tile()
    chracter=Chracter()
    move=Move()
    #map[0].mapononff=1



def exit():
    del(map)
    del(tile)
    del(chracter)
    del(move)


def pause():
    global dice_num
    global chracter


def resume():
    global dice_num
    global chracter

def update():
    global map
    global move
    global chracter
    global tile
    if pausenum==0:
        chracter.update()
        move.update()
        tile.update()
    global statbar








def draw():
    global dice_num
    global chracter
    global tile
    global statbar
    global statpng
    global timer

    clear_canvas()
    handle_events()
    global map

    for m in map:
         m.draw()


    tile.draw()
    chracter.draw()
    stat.draw()
    timer+=1
    delay(0.01)


    update_canvas()
