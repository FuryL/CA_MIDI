import sys
import copy
import pygame
import threading
import os
import re
import mido
#import numpy as np
#import pygame_menu


windowx=768
windowy=768
pygame.init()
size=windowx,windowy
world = dict()
running = False
length = 12
colorwhite=(255,255,255)
colorblack=(0,0,0)
path = 'camidi.mid'
num_show = False


def shownum(num):
    global num_show
    if num == False:
        num_show = True
    else:
        num_show = False


def start_game():
    update_thread = threading.Thread(target=update)
    update_thread.start()
    while True:
        edit()


def update():
    global window,num_show
    while True:
        window.fill(colorwhite)
        world_copy = world.copy()

        #绘制格子
        for x in range(0,windowx//length+1):
            for y in range(0,windowy//length+1):
                pygame.draw.rect(window,colorblack,(x*length,y*length,length,length),1)

        #填色 活的格子
        for cellular in world_copy:
            x, y = cellular
            if x in range(0,windowx//length+1) and y in range(0,windowy//length+1) and world_copy[(x,y)]:
                pygame.draw.rect(window,colorblack,((x)*length,(y)*length,length,length))
    
        #显示行列数字
        if num_show:
            font = pygame.font.SysFont('Times', 8 )
            
            for row in range(0,windowx//length+1):
                numwide=4
                text = font.render(str(row), True, (0, 128, 0), None)
                text2 = font.render(str(row+64)[-2:], True, (0, 128, 0), None)
                if row>9:
                    numwide=2
                window.blit(text, (row*length+numwide, 1))
                window.blit(text2, (row*length+2, windowy//2+1))
            
            for col in range(1,windowy//length//2):
                numwide=4
                text = font.render(str(col), True, (128, 0, 0), None)
                if col>9:
                    numwide=2
                window.blit(text, (numwide, col*length+1))
                window.blit(text, (numwide, (col+32)*length+1))

        pygame.display.flip()
        clock.tick(60)


#编辑,按键操作
def edit():
    global windowx, windowy, length, origin, window, running
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]//length
            y = event.pos[1]//length
            if event.button == 1:
                 running = False
                 while pygame.MOUSEBUTTONUP not in map(lambda x:x.type, pygame.event.get()):
                     x = pygame.mouse.get_pos()[0]//length
                     y = pygame.mouse.get_pos()[1]//length
                     world[(x,y)] = True
                     search_range = ((x-1,y-1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1),(x-1,y))
                     for space in search_range:
                         if not world.__contains__(space):
                             world[space] = False
            elif event.button == 3:
                world[(x,y)] = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if running:
                running = False
            else:
                running = True
                rule()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            running = False
            music()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False
            shownum(num_show)

        elif event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        clock.tick(60)


#规则 生成 死亡
def rule():
    global world, running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False 
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                running = False
                music()          
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False
                shownum(num_show)
            elif event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                
        clock.tick(60)
        next_generation_world = dict()
        world_copy = world.copy()
        for cellular in world_copy:
            x, y = cellular
            search_range = ((x-1,y-1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1),(x-1,y))
            count = 0
            for location in search_range:
                if world_copy.__contains__(location) and world_copy[location]:
                    count += 1
        
            #如果一个细胞周围有3个细胞为生，则该细胞为生，即该细胞若原先为死，则转为生，若原先为生，则保持不变
            #如果一个细胞周围有2个细胞为生，则该细胞的生死状态保持不变
            if count == 3 or (count==2 and world_copy[cellular]):
                next_generation_world[cellular] = True
                for space in search_range:
                    if not next_generation_world.__contains__(space):
                        next_generation_world[space] = False
            elif count == 0:
                pass
            else:
                next_generation_world[cellular] = False

        if world_copy == next_generation_world or running == False:
            running = False
            return None
        world = next_generation_world
    return None


def auto_save_file(path):
    directory, file_name = os.path.split(path)
    while os.path.isfile(path):
        if re.search('(\d+)\)\.', file_name) is None:
            file_name = file_name.replace('.', '(1).')
        else:
            current_number = int(re.findall('(\d+)\)\.',file_name)[-1])
            new_number = current_number + 1
            file_name = file_name.replace(f'({current_number}).', f'({new_number}).')
        path = os.path.join(file_name)
    return path


#生成MIDI
def music():
    global path
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)
    track.append(mido.MetaMessage('set_tempo', tempo=500000, time=0))
    a=[]

    for i in world:
        x,y=i
        if world[i]==True and x>=0 and y>=0 and x<64 and y<64:
            if y>31 :
                x=x+64
                y=y-32
            a.append((x,y))
    a.sort(key=lambda x:x[1])
    
    lasty=a[0][1]
    count1=0
    count2=0
    oncount=0
    offcount=0
    llasty=lasty
    for i in a:
        x,y=i
        count2 += 1
        if x in range(0,windowx//length*2) and y in range(0,windowy//length*2):
            if x<21 or x>108:continue

            if lasty==y:
                if oncount==0:
                    track.append(mido.Message('note_on', note=x, velocity=96, time=480*y))
                    oncount=1
                else:
                    track.append(mido.Message('note_on', note=x, velocity=96, time=480*(y-lasty)))
                
            if lasty!=y:
                offcount=0
                for j in a[count1:count2-1]:
                    x2,y2=j
                    if x2<21 or x2>108:continue
                    
                    if offcount==0:
                        track.append(mido.Message('note_off', note=x2, velocity=96, time=480))
                        offcount=1  
                    elif offcount==1:
                        track.append(mido.Message('note_off', note=x2, velocity=96, time=0))
                      
                count1=count2-1
                llasty=lasty
                lasty=y
                track.append(mido.Message('note_on', note=x, velocity=96, time=480*(y-llasty-1)))
    offcount=0         
    for i in a[count1:]:
        x,y=i
        if x<21 or x>108:continue

        if offcount==0:
             track.append(mido.Message('note_off', note=x, velocity=96, time=480))
             offcount=1
        if offcount==1:
            track.append(mido.Message('note_off', note=x, velocity=96, time=0))

    mid.save(auto_save_file(path))


screencaption = pygame.display.set_caption('CA_MIDI')
os.environ['SDL_VIDEO_CENTERED'] = '1'
window=pygame.display.set_mode(size)
clock = pygame.time.Clock()
start_game()