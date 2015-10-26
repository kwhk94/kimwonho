__author__ = 'kkk'
from pico2d import*
import game_framework
import diceanimation2
import title

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

global xpos,ypos
xpos,ypos=0,0

class Map():
    image = None
    maponoff=None
    global xpos,ypos

    def __init__(self):
        if Map.image==None:
            Map.image=[load_image('realmap (12).png'),load_image('realmap (8).png'),
                       load_image('realmap (1).png'),load_image('realmap (2).png'),
                       load_image('realmap (3).png'),load_image('realmap (4).png'),
                       load_image('realmap (5).png'),load_image('realmap (6).png'),
                       load_image('realmap (7).png'),load_image('realmap (9).png')]
        self.number=0
        self.mapnumber=1
        if Map.maponoff==None:
            Map.maponoff=0



    def draw(self):
        global xpos,ypos
        if self.number==0:
          self.image[self.mapnumber].clip_draw(0,0,400,385,200+xpos,50+ypos)
        elif self.number==1:
            self.image[self.mapnumber].clip_draw(0,0,400,385,136+xpos,390+ypos)
        elif self.number==2:
            self.image[self.mapnumber].clip_draw(0,0,400,385,465+xpos,286+ypos)
        elif self.number==3:
            self.image[self.mapnumber].clip_draw(0,0,400,385,74+xpos,734+ypos)
        elif self.number==4:
            self.image[self.mapnumber].clip_draw(0,0,400,385,403+xpos,628+ypos)
        elif self.number==5:
            self.image[self.mapnumber].clip_draw(0,0,400,385,732+xpos,524+ypos)

class Tile():
      global xpos,ypos
      x,y=None,None
      TileType={
          0:[1,1,1,0,0,0,1],
          1:[1,1,1,1,1,1,1],
          2:[1,1,1,1,1,1,1],
          3:[0,1,1,1,1,1,1],
          4:[0,0,1,1,1,1,1],
          5:[1,0,1,1,1,1,1],
          6:[1,0,0,1,0,1,1],
          7:[1,1,0,1,1,1,1],
          8:[1,1,1,1,1,1,1],
          9:[1,1,1,1,1,1,1]
      }
      def __init__(self):
          if Tile.x == None:
              Tile.x=[[200+xpos,200+xpos+200*(1/3),200+xpos+200*(2/3),200+xpos+200*(1/3)
                          ,200+xpos-200*(1/3),200+xpos-200*(2/3),200+xpos-200*(1/3)],
                      [136+xpos,136+xpos+200*(1/3),136+xpos+200*(2/3),136+xpos+200*(1/3),
                       136+xpos-200*(1/3),136+xpos-200*(2/3),136+xpos-200*(1/3)],
                          [465+xpos,465+xpos+200*(1/3),465+xpos+200*(2/3),465+xpos+200*(1/3),
                       465+xpos-200*(1/3),465+xpos-200*(2/3),465+xpos-200*(1/3)],
                          [74+xpos,74+xpos+200*(1/3),74+xpos+200*(2/3),74+xpos+200*(1/3),
                       74+xpos-200*(1/3),74+xpos-200*(2/3),74+xpos-200*(1/3)],
                          [403+xpos,403+xpos+200*(1/3),403+xpos+200*(2/3),403+xpos+200*(1/3),
                       403+xpos-200*(1/3),403+xpos-200*(2/3),403+xpos-200*(1/3)],
                          [732+xpos,732+xpos+200*(1/3),732+xpos+200*(2/3),732+xpos+200*(1/3),
                       732+xpos-200*(1/3),732+xpos-200*(2/3),732+xpos-200*(1/3)]
                      ]
          if Tile.y == None:
              Tile.y=[[50+ypos,50+ypos+100,50+ypos,50+ypos-100,50+ypos-100,50+ypos,50+ypos+100],
                     [390+ypos,390+ypos+100,390+ypos,390+ypos-100,390+ypos-100,390+ypos,390+ypos+100],
                     [286+ypos,286+ypos+100,286+ypos,286+ypos-100,286+ypos-100,286+ypos,286+ypos+100],
                     [734+ypos,734+ypos+100,734+ypos,734+ypos-100,734+ypos-100,734+ypos,734+ypos+100],
                     [628+ypos,628+ypos+100,628+ypos,628+ypos-100,628+ypos-100,628+ypos,628+ypos+100],
                     [524+ypos,524+ypos+100,524+ypos,524+ypos-100,524+ypos-100,524+ypos,524+ypos+100]]
          Tile.type=[[1,1,1,0,0,0,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]]
          self.ring_image=load_image('ring.png')
          self.time=0
          self.time2=0

      def update(self):
           global xpos,ypos
           Tile.x=[[200+xpos,200+xpos+200*(1/3),200+xpos+200*(2/3),200+xpos+200*(1/3)
                          ,200+xpos-200*(1/3),200+xpos-200*(2/3),200+xpos-200*(1/3)],
                      [136+xpos,136+xpos+200*(1/3),136+xpos+200*(2/3),136+xpos+200*(1/3),
                       136+xpos-200*(1/3),136+xpos-200*(2/3),136+xpos-200*(1/3)],
                          [465+xpos,465+xpos+200*(1/3),465+xpos+200*(2/3),465+xpos+200*(1/3),
                       465+xpos-200*(1/3),465+xpos-200*(2/3),465+xpos-200*(1/3)],
                          [74+xpos,74+xpos+200*(1/3),74+xpos+200*(2/3),74+xpos+200*(1/3),
                       74+xpos-200*(1/3),74+xpos-200*(2/3),74+xpos-200*(1/3)],
                          [403+xpos,403+xpos+200*(1/3),403+xpos+200*(2/3),403+xpos+200*(1/3),
                       403+xpos-200*(1/3),403+xpos-200*(2/3),403+xpos-200*(1/3)],
                          [732+xpos,732+xpos+200*(1/3),732+xpos+200*(2/3),732+xpos+200*(1/3),
                       732+xpos-200*(1/3),732+xpos-200*(2/3),732+xpos-200*(1/3)]]
           Tile.y=[[50+ypos,50+ypos+100,50+ypos,50+ypos-100,50+ypos-100,50+ypos,50+ypos+100],
                     [390+ypos,390+ypos+100,390+ypos,390+ypos-100,390+ypos-100,390+ypos,390+ypos+100],
                     [286+ypos,286+ypos+100,286+ypos,286+ypos-100,286+ypos-100,286+ypos,286+ypos+100],
                     [734+ypos,734+ypos+100,734+ypos,734+ypos-100,734+ypos-100,734+ypos,734+ypos+100],
                     [628+ypos,628+ypos+100,628+ypos,628+ypos-100,628+ypos-100,628+ypos,628+ypos+100],
                     [524+ypos,524+ypos+100,524+ypos,524+ypos-100,524+ypos-100,524+ypos,524+ypos+100]
                   ]
           for j in range(6):
               for i in range(10):
                   if map[j].mapnumber==i:
                        Tile.type[j]=self.TileType[i]
           self.time2+=1
           if self.time2%8==0:
            self.time=self.time+1
           delay(0.01)

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
        if Chracter.image==None:
            Chracter.image=load_image('Chracter.png')
        self.number=0
        Chracter.Chracter_x, Chracter.Chracter_y=0,0

    def update(self):
        global xpos,ypos
        global tile
        global mouse_x,mouse_y
        global map
        Chracter.state=[200+xpos+ Chracter.Chracter_x,50+ypos+Chracter.Chracter_y]
        for j in range(6):
           for i in range(7):
             if tile.x[j][i]<chracter.state[0]+150 and tile.x[j][i]>chracter.state[0]-150 \
                     and tile.y[j][i]<chracter.state[1]+150 and tile.y[j][i]>chracter.state[1]-150 and Tile.type[j][i]!=0:#캐릭터의 주위 타일
                 if mouse_x<tile.x[j][i]+25 and mouse_x>tile.x[j][i]-25 and mouse_y< tile.y[j][i]+25 and mouse_y>tile.y[j][i]-25 :
                    Chracter.Chracter_x+= tile.x[j][i]-Chracter.state[0]
                    Chracter.Chracter_y+=  tile.y[j][i]-Chracter.state[1]
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
    global mouse_x,mouse_y
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
            elif (event.type)==(SDL_MOUSEBUTTONDOWN):
                global mouse_x,mouse_y
                mouse_x,mouse_y=event.x,599-event.y





def enter():
    global map
    global move
    global chracter
    global tile
    global mouse_x,mouse_y
    a=0
    map =[Map() for i in range(6)]
    for i in map:
        i.number=a
        a=a+1
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
    for i in range(6):
         dice_num=[i]


def resume(): pass

def update():
    global map
    global move
    global chracter
    global tile
    chracter.update()

    move.update()
    tile.update()







def draw():
    global dice_num
    global chracter
    global tile


    clear_canvas()
    handle_events()
    global map

    for m in map:
         m.draw()


    tile.draw()
    chracter.draw()
    update_canvas()