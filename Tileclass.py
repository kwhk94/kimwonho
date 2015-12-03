__author__ = 'kkk'

import json
from pico2d import*
import game_framework
import map


class Tile():
      global xpos,ypos
      x,y=[],[]
      global etc
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
          9:etc["TileType"]["9"],
          10:etc["TileType"]["10"]
      }


      TIME_PER_ACTION=0.5
      ACTION_PER_TIME=1.0/TIME_PER_ACTION
      FRAMES_PER_ACTION=4


      def __init__(self):
          if Tile.x==[]:
            for i in range(8):
                    Tile.x.append([etc["mapx"][i]+etc["tilexsize"][j]+map.xpos for j in range(7)])
          if Tile.y==[]:
             for i in range(8):
                    Tile.y.append([etc["mapy"][i]+etc["tileysize"][j]+map.ypos for j in range(7)])
          Tile.type=[self.TileType[i] for i in range(11)]
          if Tile.ring_image==None:
                Tile.ring_image=load_image('png\\ring.png')
          self.frame=0
          self.total_frame=0

      def update(self,frame_time):

           global xpos,ypos
           for i in range(8):
              for j in range(7):
                  Tile.x[i][j]=etc["mapx"][i]+etc["tilexsize"][j]+map.xpos
                  Tile.y[i][j]=etc["mapy"][i]+etc["tileysize"][j]+map.ypos

           for j in range(8):
               for i in range(11):
                   if map.map[j].mapnumber==i:
                        Tile.type[j]=self.TileType[i]
           self.total_frame+=Tile.FRAMES_PER_ACTION*Tile.ACTION_PER_TIME*frame_time
           self.frame=int(self.total_frame)%4



      def draw(self):
          global chracter
          global mouse_x,mouse_y
          for j in range(8):
           for i in range(7):
             if Tile.x[j][i]<map.chracter.state[0]+150 and Tile.x[j][i]>map.chracter.state[0]-150 \
                     and Tile.y[j][i]<map.chracter.state[1]+150 and Tile.y[j][i]>map.chracter.state[1]-150 and \
                 Tile.type[j][i]!=0 :
              self.ring_image.clip_draw(62*(self.frame%4),0,64,66,Tile.x[j][i],Tile.y[j][i])
          #self.ring_image.clip_draw(62*(self.time%4),0,64,66,mouse_x,mouse_y)




class Move():
    stop,rightmove,leftmove,upmove,downmove=0,1,2,3,4
    def __init__(self):
        self.state=self.stop

    def Stop(self):
        map.xpos,map.ypos
        self.state=self.stop

    def Rightmove(self):
        if map.xpos>-100:
         map.xpos=map.xpos-2
        self.state=self.rightmove

    def Leftmove(self):
        if map.xpos<100:
         map.xpos=map.xpos+2
        self.state=self.leftmove

    def Upmove(self):
        if map.ypos>-600:
         map.ypos=map.ypos-2
        self.state=self.upmove

    def Downmove(self):
        if map.ypos<20:
         map.ypos=map.ypos+2
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

    def  handle_events(self,event):
              if event.type == SDL_QUIT:
                    game_framework.quit()
              else:
                    if(event.type,event.key)==(SDL_KEYDOWN,SDLK_RIGHT):
                        if self.state==self.stop :
                            self.state=self.rightmove
                    elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_LEFT):
                        if self.state==self.stop :
                             self.state=self.leftmove
                    elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_UP):
                          if self.state==self.stop :
                                 self.state=self.upmove
                    elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_DOWN):
                         if self.state==self.stop :
                                self.state=self.downmove
                    elif(event.type==SDL_KEYUP):
                            self.state=self.stop
