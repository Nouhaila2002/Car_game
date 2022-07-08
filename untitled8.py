# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 01:53:02 2022

@author: Meryem
"""

#create pygame window 
import pygame
from pygame.locals import *
import random

size = width , height =(800,800) #tuple 800px
road_width = int(width/1.6)
roadmark_width = int(width/80)
right_lane = width/2 + road_width/4;
left_lane = width/2 - road_width/4
speed=1


pygame.init()
running = True
#set window size
screen=pygame.display.set_mode(size)
#set title 
pygame.display.set_caption("man game")
#set background color 
screen.fill((60,220,0))




#apply changes
pygame.display.update()


#load player image
car = pygame.image.load("car.png")
car_location = car.get_rect()
car_location.center = right_lane , height*0.8

#load enemy image
car2 = pygame.image.load("enemyCar.png")
car2_location = car2.get_rect()
car2_location.center = left_lane , height*0.2


counter = 0

#game loop
while running:
    counter+=1
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("LEVEL UP",speed)
    #animate enemy vehicle
    car2_location[1] +=1
    if car2_location[1] > height :
        if random.randint(0, 1) == 0:
            car2_location.center=right_lane,-200
        else:
            car2_location.center=left_lane,-200
            
    #end game
    if car_location[0] == car2_location[0] and car2_location[1] >car_location[1] - 250: #250px : image size
        print("GAME OVER! YOU LOST!")
        break 
    #event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            running=False   
        if event.type == KEYDOWN: #import all the keyboard event
            if event.key in [K_a , K_LEFT]:
                car_location = car_location.move([-int(road_width/2),0]) #0:because we won't change the height
            if event.key in [K_d , K_RIGHT]:
                car_location = car_location.move([int(road_width/2),0]) #0:because we won't change the height

                

    #to not duplicate the car
    #draw graphics
    pygame.draw.rect(
        screen, #where we want draw
        (50,50,50), #color
        (width/2-road_width/2,0,road_width,height)  # X and Y from wich X and Y we want to start the to any X and Y we want end
    )
    
    pygame.draw.rect(   
        screen, #where we want draw
        (255,240,60),
        (width/2-roadmark_width/2,0,roadmark_width,height)  # X and Y from wich X and Y we want to start the to any X and Y we want end
    )
    
    pygame.draw.rect(
        screen,
        (255,255,255),
        (width/2-road_width/2 + roadmark_width*2,0,roadmark_width,height)  # X and Y from wich X and Y we want to start the to any X and Y we want end
    
    )
    
    pygame.draw.rect(
        screen,
        (255,255,255),
        (width/2+road_width/2 - roadmark_width*3,0,roadmark_width,height)  # X and Y from wich X and Y we want to start the to any X and Y we want end
    )

                
    screen.blit(car,car_location) #to not load the image every time , waste resource
    screen.blit(car2,car2_location) #to not load the image every time , waste resource
    pygame.display.update()
            
            
pygame.quit()






