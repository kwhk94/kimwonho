__author__ = 'kkk'
from pico2d import*
import game_framework
import battlemap
import title
import json
import random
global dice_num
global font
import gameover
import mapclass
from Tileclass import Tile as Tile
from Tileclass import Move as Move

global xpos,ypos
xpos,ypos=0,0

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





class Music():
    bgm=None
    def __init__(self):
        if self.bgm==None:
            self.bgm=load_music('etc\\bgm.ogg')
            self.bgm.set_volume(12)
            self.bgm.repeat_play()


class Stat():
    global statpng
    global statbar
    global font
    global smallfont
    global turnnumber
    image=None
    blood=None
    armor=None
    def __init__(self):
        if Stat.image==None:
            Stat.image=load_image("png\\statbar.png")
        if Stat.blood==None:
            Stat.blood=load_image("png\\Blood.png")
        if Stat.armor==None:
            Stat.armor=load_image("png\\armor.png")
        self.onoff=0;


    def draw(self):
        if self.onoff==0:
            self.image.clip_draw(0,0,159,250,800-80,600-120)
            self.blood.clip_draw(70*(chracter.hp-1),0,70,99,800-122,600-49)
            self.armor.clip_draw(84*(chracter.df-1),0,84,99,800-50,600-49)
            font.draw(800-150,600-130,'STR :')
            font.draw(800-40,600-130,"%d"%chracter.str,color=(200,0,0))
            font.draw(800-150,600-160,'LUK :')
            font.draw(800-40,600-160,"%d"%chracter.luk,color=(0,200,0))
            font.draw(800-150,600-190,'Gold')
            font.draw(800-40,600-190,"%d"%chracter.gold,color=(200,200,0))
            font.draw(800-150,600-220,'AGI :')
            font.draw(800-40,600-220,"%d"%chracter.agi,color=(100,100,100))
            smallfont.draw(800-150,600-110,'Maxhp :')
            smallfont.draw(800-100,600-110,"%d"%chracter.maxhp,color=(200,0,0))
        font.draw(800-350,600-20,'Turn')
        font.draw(800-410,600-20,"%d"%turnnumber,color=(150,100,100))



class Chracter():
    image = None
    state=[200,50]
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
        Chracter.maxhp=Stat_data["HP"]
        Chracter.df=Stat_data["DF"]
        Chracter.maxdf=Stat_data["DF"]
        Chracter.str=Stat_data["STR"]
        Chracter.agi=Stat_data["AGI"]
        Chracter.luk=Stat_data["LUK"]
        Chracter.gold=Stat_data["Gold"]
        Chracter.type=1


    def update(self):
        global xpos,ypos
        global tile
        global mouse_x,mouse_y
        global map
        global tiletype
        global turntype
        global timer
        ON,OFF=1,0
        Chracter.state=[200+xpos+ Chracter.Chracter_x,50+ypos+Chracter.Chracter_y]
        for j in range(8):
           for i in range(7):
             if tile.x[j][i]<chracter.state[0]+150 and tile.x[j][i]>chracter.state[0]-150 \
                     and tile.y[j][i]<chracter.state[1]+150 and tile.y[j][i]>chracter.state[1]-150 \
                     and Tile.type[j][i]!=0 and turntype==0:#캐릭터의 주위 타일
                 if not( tile.x[j][i]+20>chracter.state[0] and tile.x[j][i]-20<chracter.state[0] and tile.y[j][i]+20>chracter.state[1]
                         and tile.y[j][i]-20<chracter.state[1] ):
                    if mouse_x<tile.x[j][i]+25 and mouse_x>tile.x[j][i]-25 and mouse_y< tile.y[j][i]+25 and mouse_y>tile.y[j][i]-25 :
                        Chracter.Chracter_x+= tile.x[j][i]-Chracter.state[0]
                        Chracter.Chracter_y+=  tile.y[j][i]-Chracter.state[1]
                        Chracter.type=Tile.type[j][i] #캐릭터 위치타일의 타입을 입력
                        mouse_x=-1000         #마우스위치를 유지시키면 화면이 움직일시 마우스 클릭위치에따라 이벤트가 중복 발생할수있다
                        mouse_y=-1000
                        tiletype=Tile.type[j][i]
                        turntype=1
                 if map[j].maponoff==OFF:
                    map[j].maponoff=ON;
                    map[j].mapnumber=random.randint(2,9)
                    if j==7:
                        map[j].mapnumber=10



    def draw(self):
         global xpos,ypos
         global turntype
         self.image.clip_draw(0,0,89,119,Chracter.state[0],Chracter.state[1])

class Card():
    image=None
    result=None
    def __init__(self):
        if self.image==None:
            self.image=[load_image('png\\card1.png'),
                        load_image('png\\card2.png'),
                        load_image('png\\card3.png'),
                        load_image('png\\card4.png'),
                        load_image('png\\card5.png'),
                        load_image('png\\card6.png'),
                        load_image('png\\card7.png')]
        if self.result==None:
            self.result=[load_image('png\\result.png'),
                         load_image('png\\result 2.png'),
                         load_image('png\\result 3.bmp')]



def changemap():
    global turntype
    global mouse_x,mouse_y
    game_framework.push_state(battlemap)
    turntype=0
    mouse_x,mouse_y=-1000,-1000   #마우스위치를 유지시키면 화면이 돌아올때 이벤트가중복발생된다


def handle_events():
    global running,xpos,ypos,actionnumber
    global map,move,tile,turnnumber,cardnumber
    global stat,mouse_x,mouse_y,statonoff
    global pausenum,dice_num,tiletype,turntype

    Stop,Right,Left,UP,DOWN=0,1,2,3,4
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
             game_framework.quit()
        else:
            move.handle_events(event)
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                if turntype==1 and (Chracter.type==2 or Chracter.type==3 or Chracter.type==5 or Chracter.type==20):
                 changemap()
                elif turntype==1 and Chracter.type==1:
                    statonoff=stat.onoff
                    cardnumber=random.randint(0,100);
                    turntype=2
                elif turntype==2 and Chracter.type==1:
                    turntype=3
                elif turntype==3 and Chracter.type==1:
                    turntype=4
                elif turntype==4 and Chracter.type==1:
                    turntype=0
                else :
                    if turntype!=0 and turntype!=3:
                        turnnumber+=1
                    turntype=0
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_a):
                 game_framework.push_state(battlemap)
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_p):
                if pausenum==1: pausenum=0
                elif pausenum==0:pausenum=1
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_o):
                 print(battlemap.dice_num)
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_i) and turntype!=2:
                 stat.onoff= not stat.onoff
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_q):
                 print(chracter.hp)
            if (event.type,event.button)==(SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT):
                     mouse_x,mouse_y=event.x,599-event.y
                     if turntype==2:
                         actionnumber=click_card()




def result(num):
    global turntype,turnnumber,chracter
    turnnumber+=1
    if num>=0 and num<chracter.luk*5:
        if chracter.hp<chracter.maxhp:
            turntype=0
            chracter.hp+=1


    elif num>=chracter.luk*5 and num<chracter.luk*5+10:
        turntype=0
        chracter.hp-=1

    else :
        turntype=0







def click_card():
    global mouse_x,mouse_y
    global turntype
    num=[0,0,0]
    for i in num :
        num[i]=random.randint(0,100)
    stat.onoff=statonoff
    if mouse_x>50 and mouse_x<250 and mouse_y>200 and mouse_y<500 :
        mouse_x,mouse_y=-100,-100
        turntype=3
        return num[0]
    elif mouse_x>300 and mouse_x<500 and mouse_y>200 and mouse_y<500 :
        mouse_x,mouse_y=-100,-100
        turntype=3
        return num[1]
    elif mouse_x>550 and mouse_x<750 and mouse_y>200 and mouse_y<500 :
        mouse_x,mouse_y=-100,-100
        turntype=3
        return num[2]
    else :
        turntype=3
        return num[0]





def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time




def drawcard(num):
    global cardnumber
    global turntype
    if turntype==2:
        stat.onoff=1
        card.image[cardnumber%7].clip_draw(0,0,200,300,150,350) #draw_rectangle(50,200,250,500)
        card.image[(cardnumber+1)%7].clip_draw(0,0,200,300,400,350)#draw_rectangle(300,200,500,500)
        card.image[(cardnumber+2)%7].clip_draw(0,0,200,300,650,350)#draw_rectangle(550,200,750,500)
    if turntype==3:
        if num<80:
            card.result[0].clip_draw(0,0,266,399,150,350)
        elif num>=70 and num<90:
             card.result[1].clip_draw(0,0,266,399,150,350)
        else :
             card.result[2].clip_draw(0,0,266,399,150,350)

    if turntype==4:
         result(actionnumber)
         turntype=0


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
    global smallfont
    global bigfont
    global timer
    global tiletype
    global turntype
    global turnnumber
    global current_time
    global bgm
    global card, actionnumber
    global xpos,ypos
    xpos,ypos=0,0
    actionnumber=0
    card=Card()
    bgm=Music()
    turnnumber=1
    turntype=0
    tiletype=0
    timer=0
    font=load_font('etc\\font.ttf',30)
    smallfont=load_font('etc\\font.ttf',10)
    bigfont=load_font('etc\\font.ttf',50)
    stat=Stat()
    pausenum=0
    countumber=0
    map =[mapclass.Map() for i in range(8)]
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
    current_time = get_time()




def exit():
    del(map)
    del(tile)
    del(chracter)
    del(move)
    del(pausenum)
    del(mouse_x,mouse_y)
    del(dice_num)
    del(stat)
    del(font)
    del(smallfont)
    del(timer)
    del(tiletype)
    del(turntype)


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
    global turntype
    frame_time=get_frame_time()
    if pausenum==0:
        chracter.update()
        move.update()
        tile.update(frame_time)



    global statbar






def draw():
    global dice_num
    global chracter
    global tile
    global statbar
    global statpng
    global timer
    global map
    global bigfont
    global turntype
    global actionnumber


    clear_canvas()
    handle_events()

    for m in map:
         m.draw()


    tile.draw()
    chracter.draw()
    stat.draw()
    timer+=1
    if turntype==1:
         bigfont.draw(200,100,"PRESS SPACE!",color=(230,0,0))
    drawcard(actionnumber)
    if chracter.hp==0:
        game_framework.push_state(gameover)
    delay(0.01)


    update_canvas()
