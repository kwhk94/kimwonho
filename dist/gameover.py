import game_framework
import map
from pico2d import *
import battlemap


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image,time_num,current_time
    time_num=get_time()
    current_time=get_time()
    image = load_image('png\\gameover.png')


def exit():
    # global image
    # del(image)
    close_canvas()


def update():
    global current_time
    current_time=get_time()

def draw():
    global image,current_time,time_num
    clear_canvas()
    image.clip_draw(0,0,800,600,400,300)
    if current_time-time_num>1:
         map.bigfont.draw(50,450,"SCORE",color=(250,250,250))

    if current_time-time_num>2:
         map.font.draw(100,400,"hp  :",color=(250,250,250))
         map.font.draw(300,400,'%d'%(map.chracter.maxhp*100),color=(255,100,100))
    if current_time-time_num>3:
         map.font.draw(100,350,"DF  :",color=(250,250,250))
         map.font.draw(300,350,'%d'%(map.chracter.maxdf*300),color=(255,100,100))
    if current_time-time_num>4:
         map.font.draw(100,300,"turn  :",color=(250,250,250))
         map.font.draw(300,300,'-%d'%(map.turnnumber*10),color=(255,100,100))
    if current_time-time_num>5:
         map.font.draw(100,250,"DAMAGE  :",color=(250,250,250))
         map.font.draw(300,250,'%d'%(map.chracter.str*100),color=(255,100,100))

    if current_time-time_num>6:
         map.font.draw(100,200,"DEATH  :",color=(250,250,250))
         map.font.draw(300,200,'%d'%(-1000),color=(255,100,100))

    if current_time-time_num>7:
         map.font.draw(100,150,"Total  :",color=(250,250,250))
         map.font.draw(300,150,'%d'%(map.chracter.hp*100-map.turnnumber*10+map.chracter.df*300+map.chracter.str*100-1000),color=(255,100,100))
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
             game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.quit()


def pause(): pass


def resume(): pass




__author__ = 'kkk'
