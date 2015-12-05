__author__ = 'kkk'
from pico2d import*
import game_framework
import battlemap
import title
import json
import random
import map
global dice_num
global font
import gameover
import mapclass
from Tileclass import Tile as Tile
from Tileclass import Move as Move
from cardclass import Card as Card
from statclass import Stat_downside as Stat

def handle_events():
    global running,xpos,ypos,actionnumber
    global map,move,tile,turnnumber,cardnumber
    global stat,mouse_x,mouse_y,statonoff,itemnumber
    global pausenum,dice_num,tiletype,turntype
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
             game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                if turntype==2 :
                    turntype=4
                elif turntype==10 or turntype==9:
                    map.turnnumber+=1
                    game_framework.pop_state()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_p):
                if pausenum==1: pausenum=0
                elif pausenum==0:pausenum=1
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_o):
                 print(actionnumber)
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_i):
                 stat.onoff= not stat.onoff
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_q):
                 game_framework.pop_state()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_KP_MINUS):
                if turntype==3 and itemnumber>0:
                    itemnumber-=1
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_KP_PLUS):
                if turntype==3 and itemnumber<map.chracter.gold:
                    itemnumber+=1
            if (event.type,event.button)==(SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT):
                     mouse_x,mouse_y=event.x,599-event.y
                     if turntype==1 or turntype==3:
                         actionnumber=click_card()
def result(num):
    global turntype,turnnumber,chracter,itemnumber
    if turntype==2:  ## 랜덤 상황
        if num>=0 and num<5:
                if map.chracter.maxhp>1:
                    map.chracter.hp-=1
                    map.chracter.maxhp-=1
        elif num>=5 and num<10:
                map.chracter.gold=0
        elif num>15 and num<map.chracter.luk*5+15 and map.chracter.luk<5:
                map.chracter.luk+=1
        else :
                 pass
    if turntype==3:
        if num==0:
            map.chracter.gold-=(map.chracter.str-2)*2
            map.chracter.str+=1
            turntype=9
        elif num==1:
            map.chracter.gold-=map.chracter.df*5
            map.chracter.df+=1
            turntype=9
        elif num==2:
            map.chracter.gold-=itemnumber
            map.chracter.hp+=itemnumber
            turntype=9


def click_card():
    global mouse_x,mouse_y
    global turntype
    num=[0,0,0]
    for i in num :
        num[i]=random.randint(0,100)
    if turntype==1:
         if mouse_x>50 and mouse_x<250 and mouse_y>200 and mouse_y<500 :
              mouse_x,mouse_y=-100,-100
              turntype=2
              result(num[0])
              return num[0]

         elif mouse_x>300 and mouse_x<500 and mouse_y>200 and mouse_y<500 :
               mouse_x,mouse_y=-100,-100
               turntype=3

         elif mouse_x>550 and mouse_x<750 and mouse_y>200 and mouse_y<500 :
               mouse_x,mouse_y=-100,-100
               if map.chracter.hp<map.chracter.maxhp:
                     map.chracter.hp+=1
               turntype=10
    if turntype==3:
         if mouse_x>50 and mouse_x<250 and mouse_y>200 and mouse_y<500 :
              mouse_x,mouse_y=-100,-100
              print("0")
              if (map.chracter.str-2)*2<=map.chracter.gold and map.chracter.str<12:
                   result(0)

         elif mouse_x>300 and mouse_x<500 and mouse_y>200 and mouse_y<500 :
               mouse_x,mouse_y=-100,-100
               if (map.chracter.df)*5<=map.chracter.gold and map.chracter.df<5:
                    result(1)

         elif mouse_x>550 and mouse_x<750 and mouse_y>200 and mouse_y<500 :
               mouse_x,mouse_y=-100,-100
               if map.chracter .gold>0:
                    result(2)





def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time



def drawcard(num):
    global cardnumber
    global turntype,font
    road,wood=1,8
    if turntype==1 or turntype==10:
        card.image[(cardnumber+1)%7].clip_draw(0,0,200,300,150,350)#draw_rectangle(300,200,500,500)
        card.villege.clip_draw(0,0,200,300,400,350) #draw_rectangle(50,200,250,500)
        font.draw(340,380,"물건을 산다",color=(150,350,0))
        card.villege.clip_draw(0,0,200,300,650,350) #draw_rectangle(50,200,250,500)
        font.draw(590,380,"휴식한다",color=(150,350,0))

    elif turntype==2:
            if num>=0 and num<5:
                 card.villege.clip_draw(0,0,266,399,150,350)
                 font.draw(90,380,"음식을 잘못먹었다",color=(150,350,0))
                 font.draw(90,350,"최대체력이 감소한다",color=(150,350,0))
            elif num>=5 and num<15:
                 card.villege.clip_draw(0,0,266,399,150,350)
                 font.draw(90,380,"누군가가 돈을",color=(150,350,0))
                 font.draw(90,350,"훔쳐가버렸다!",color=(150,350,0))
            elif num>=15 and num<(map.chracter.luk*5+15):
                 card.villege.clip_draw(0,0,266,399,150,350)
                 font.draw(90,380,"상징적인 물건을",color=(150,350,0))
                 font.draw(90,350,"얻었다.",color=(150,350,0))
                 font.draw(90,320,"행운이 증가한다",color=(150,350,0))
                 font.draw(90,290,"(최대 5까지)",color=(150,350,0))
            else:
                 card.villege.clip_draw(0,0,266,399,150,350)
                 font.draw(90,380,"아무일도",color=(150,350,0))
                 font.draw(90,350,"일어나지 않았다",color=(150,350,0))

    elif turntype==3 or turntype==9:
        card.villege.clip_draw(0,0,200,300,150,350) #draw_rectangle(50,200,250,500)
        font.draw(90,380,"무기를 산다",color=(150,350,0))
        font.draw(90,350,"가격 : %d"%((map.chracter.str-2)*2),color=(150,350,0))
        font.draw(90,320,"데미지 +1",color=(150,350,0))
        card.villege.clip_draw(0,0,200,300,400,350) #draw_rectangle(50,200,250,500)
        font.draw(340,380,"방어구를 산다",color=(150,350,0))
        font.draw(340,350,"가격 : %d"%((map.chracter.df)*5),color=(150,350,0))
        font.draw(340,320,"방어력 +1",color=(150,350,0))
        font.draw(340,290,"(최대방어력 5",color=(150,350,0))
        font.draw(340,260,"를 넘지 못한다)",color=(150,350,0))
        card.villege.clip_draw(0,0,200,300,650,350) #draw_rectangle(50,200,250,500)
        font.draw(590,380,"회복한다.",color=(150,350,0))
        font.draw(590,350,"골드 1당 1회복",color=(150,350,0))
        font.draw(590,320,"%d 회복"%itemnumber,color=(150,350,0))
        card.villege.clip_draw(25,30,130,50,645,550) #draw_rectangle(50,200,250,500)
        font.draw(590,550,"+,-키로 수치조절",color=(255,0,0))


    if turntype==4:
         result(actionnumber)
         map.turnnumber+=1
         game_framework.pop_state()


def enter():
    global map, move,chracter,tile
    global pausenum,mouse_x,mouse_y,dice_num
    global stat,font,smallfont,bigfont
    global timer,tiletype,turntype,turnnumber
    global current_time,bgm,card, actionnumber
    global xpos,ypos,cardnumber, itemnumber,backpicture
    backpicture=load_image('png\\villege.jpg')
    itemnumber=0;
    xpos,ypos=0,0
    actionnumber=0
    card=Card()
    cardnumber=random.randint(0,100);
    turntype=1
    tiletype=0
    timer=0
    font=load_font('ConsolaMalgun.ttf',14)
    bigfont=load_font('ConsolaMalgun.ttf',30)
    stat=Stat()
    pausenum=0
    mouse_x,mouse_y =0,0
    tile=Tile()
    current_time = get_time()




def exit():
    pass


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
    backpicture.draw_to_origin(0,0)
    stat.draw()
    drawcard(actionnumber)
    if turntype==10 or turntype ==9:
         bigfont.draw(200,100,"PRESS SPACE!",color=(230,0,0))
    if map.chracter.hp==0:
        game_framework.push_state(gameover)
    delay(0.01)


    update_canvas()

