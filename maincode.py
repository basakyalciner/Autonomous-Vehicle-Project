# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 21:45:49 2020

@author: a
"""

# -*- coding: utf-8 -*-

import numpy as np 
import RPi.GPIO as GPIO 
import time  
   
GPIO.setmode(GPIO.BOARD)    
   
MOTOR1A = 19   
MOTOR1B = 21   
MOTOR1E = 38 
MOTOR2A = 26   
MOTOR2B = 36  
MOTOR2E = 33 
 
'''
DEĞİŞİKLİKLER:
    1- Pwm yerine dönüş için alternatif çözüm bulundu:
    sağa veya sola döneceği zaman ileri gitmeini sağlayan forward() kodu 1/5 oranında çalıştırılarak
    robotun yolu ortalaması sağlandı.
    
    2- Araç önünde ya da arkasında engelle karşılaştığında mesafe 5cm veya daha küçükse motorları durduracak bunun için
    stopFunc() isimli fonksiyon yazıldı ve yerleştirildi.
    
'''    
 

# MOTORLAR
def forward(n= 0.5): 
    MOTOR1A = 19   
    MOTOR1B = 21   
    MOTOR1E = 38 
    MOTOR2A = 26   
    MOTOR2B = 36  
    MOTOR2E = 33
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(MOTOR1A,GPIO.OUT)   
    GPIO.setup(MOTOR1B,GPIO.OUT)   
    GPIO.setup(MOTOR1E,GPIO.OUT) 
    GPIO.setup(MOTOR2A,GPIO.OUT)   
    GPIO.setup(MOTOR2B,GPIO.OUT)   
    GPIO.setup(MOTOR2E,GPIO.OUT) 
      
     
    GPIO.output(MOTOR1A,GPIO.HIGH) 
    GPIO.output(MOTOR1B,GPIO.LOW) 
    GPIO.output(MOTOR1E,GPIO.HIGH) 
 
    GPIO.output(MOTOR2A,GPIO.HIGH) 
    GPIO.output(MOTOR2B,GPIO.LOW) 
    GPIO.output(MOTOR2E,GPIO.HIGH)
        
     
    time.sleep(n)
     
    GPIO.output(MOTOR1E,GPIO.LOW)  
    GPIO.output(MOTOR1A,GPIO.LOW) 
    GPIO.output(MOTOR1B,GPIO.LOW) 
    GPIO.output(MOTOR2E,GPIO.LOW)  
    GPIO.output(MOTOR2A,GPIO.LOW) 
    GPIO.output(MOTOR2B,GPIO.LOW) 
    GPIO.cleanup()    
 
def left(): 
    MOTOR1A = 19   
    MOTOR1B = 21   
    MOTOR1E = 38 
    MOTOR2A = 26   
    MOTOR2B = 36  
    MOTOR2E = 33  
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(MOTOR1A,GPIO.OUT)   
    GPIO.setup(MOTOR1B,GPIO.OUT)   
    GPIO.setup(MOTOR1E,GPIO.OUT) 
    GPIO.setup(MOTOR2A,GPIO.OUT)   
    GPIO.setup(MOTOR2B,GPIO.OUT)   
    GPIO.setup(MOTOR2E,GPIO.OUT) 
    GPIO.output(MOTOR1A,GPIO.HIGH) 
    GPIO.output(MOTOR1B,GPIO.LOW) 
    GPIO.output(MOTOR1E,GPIO.HIGH) 
 
    GPIO.output(MOTOR2A,GPIO.LOW) 
    GPIO.output(MOTOR2B,GPIO.HIGH) 
    GPIO.output(MOTOR2E,GPIO.HIGH) 
     
    time.sleep(0.5) 
     
    GPIO.output(MOTOR1E,GPIO.LOW)  
    GPIO.output(MOTOR1A,GPIO.LOW) 
    GPIO.output(MOTOR1B,GPIO.LOW) 
    GPIO.output(MOTOR2E,GPIO.LOW)  
    GPIO.output(MOTOR2A,GPIO.LOW) 
    GPIO.output(MOTOR2B,GPIO.LOW) 
    GPIO.cleanup()     
        
def right(): 
    MOTOR1A = 19   
    MOTOR1B = 21   
    MOTOR1E = 38 
    MOTOR2A = 26   
    MOTOR2B = 36  
    MOTOR2E = 33  
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(MOTOR1A,GPIO.OUT)   
    GPIO.setup(MOTOR1B,GPIO.OUT)   
    GPIO.setup(MOTOR1E,GPIO.OUT) 
    GPIO.setup(MOTOR2A,GPIO.OUT)   
    GPIO.setup(MOTOR2B,GPIO.OUT)   
    GPIO.setup(MOTOR2E,GPIO.OUT) 
    GPIO.output(MOTOR1A,GPIO.LOW) 
    GPIO.output(MOTOR1B,GPIO.HIGH) 
    GPIO.output(MOTOR1E,GPIO.HIGH) 
 
    GPIO.output(MOTOR2A,GPIO.HIGH) 
    GPIO.output(MOTOR2B,GPIO.LOW) 
    GPIO.output(MOTOR2E,GPIO.HIGH) 
     
    time.sleep(0.5) 
     
    GPIO.output(MOTOR1E,GPIO.LOW)  
    GPIO.output(MOTOR1A,GPIO.LOW) 
    GPIO.output(MOTOR1B,GPIO.LOW) 
    GPIO.output(MOTOR2E,GPIO.LOW)  
    GPIO.output(MOTOR2A,GPIO.LOW) 
    GPIO.output(MOTOR2B,GPIO.LOW) 
    GPIO.cleanup()    
    
def backward(n=0.5): 
 
    MOTOR1A = 19   
    MOTOR1B = 21   
    MOTOR1E = 38 
    MOTOR2A = 26   
    MOTOR2B = 36  
    MOTOR2E = 33
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(MOTOR1A,GPIO.OUT)   
    GPIO.setup(MOTOR1B,GPIO.OUT)   
    GPIO.setup(MOTOR1E,GPIO.OUT) 
    GPIO.setup(MOTOR2A,GPIO.OUT)   
    GPIO.setup(MOTOR2B,GPIO.OUT)   
    GPIO.setup(MOTOR2E,GPIO.OUT) 
     
    GPIO.output(MOTOR1A,GPIO.LOW) 
    GPIO.output(MOTOR1B,GPIO.HIGH) 
    GPIO.output(MOTOR1E,GPIO.HIGH) 
 
    GPIO.output(MOTOR2A,GPIO.HIGH) 
    GPIO.output(MOTOR2B,GPIO.LOW) 
    GPIO.output(MOTOR2E,GPIO.HIGH) 
     
    time.sleep(n) 
     
    GPIO.output(MOTOR1E,GPIO.LOW)  
    GPIO.output(MOTOR1A,GPIO.LOW) 
    GPIO.output(MOTOR1B,GPIO.LOW) 
    GPIO.output(MOTOR2E,GPIO.LOW)  
    GPIO.output(MOTOR2A,GPIO.LOW) 
    GPIO.output(MOTOR2B,GPIO.LOW) 
    GPIO.cleanup() 
    
def stopFunc():
    MOTOR1A = 19   
    MOTOR1B = 21   
    MOTOR1E = 38 
    MOTOR2A = 26   
    MOTOR2B = 36  
    MOTOR2E = 33
    
    GPIO.output(MOTOR1E,GPIO.LOW)  
    GPIO.output(MOTOR1A,GPIO.LOW) 
    GPIO.output(MOTOR1B,GPIO.LOW) 
    GPIO.output(MOTOR2E,GPIO.LOW)  
    GPIO.output(MOTOR2A,GPIO.LOW) 
    GPIO.output(MOTOR2B,GPIO.LOW) 
    GPIO.cleanup() 
    
# ----------------------------------------  
# SENSÖRLER
def fw_sensor(): 
    TRIG = 11 
    ECHO = 13 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG,GPIO.OUT) 
    GPIO.setup(ECHO,GPIO.IN) 
    data_ort=[] 
    for j in range(5): 

        GPIO.output(TRIG, True) 
        time.sleep(0.1) 
        GPIO.output(TRIG, False) 
 
        while GPIO.input(ECHO)==0: 
            pulse_start = time.time() 
 
        while GPIO.input(ECHO)==1: 
            pulse_end = time.time() 
 
        pulse_duration = pulse_end - pulse_start 
 
        distance = pulse_duration * 17160 
        distance = round(distance, 2) 
        data_ort.append(distance) 
         
    average=sum(data_ort)/len(data_ort)   
    GPIO.cleanup()
    print('kizlar')
    return average 
 
def left_sensor(): 
    TRIG = 16 
    ECHO = 22 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG,GPIO.OUT) 
    GPIO.setup(ECHO,GPIO.IN) 
    data_ort=[] 
    for j in range(5): 
        print(j)
        GPIO.output(TRIG, True) 
        time.sleep(0.1) 
        GPIO.output(TRIG, False) 
 
        while GPIO.input(ECHO)==0: 
            pulse_start = time.time() 
 
        while GPIO.input(ECHO)==1: 
            pulse_end = time.time() 
 
        pulse_duration = pulse_end - pulse_start 
 
        distance = pulse_duration * 17160 
        distance = round(distance, 2) 
        data_ort.append(distance) 
         
    average=sum(data_ort)/len(data_ort)    
    GPIO.cleanup()
    print('erkekler')
    return average 
 
def right_sensor(): 
    TRIG = 15 
    ECHO = 37 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG,GPIO.OUT) 
    GPIO.setup(ECHO,GPIO.IN) 
    data_ort=[] 
    for j in range(5): 
 
        GPIO.output(TRIG, True) 
        time.sleep(0.1) 
        GPIO.output(TRIG, False) 
 
        while GPIO.input(ECHO)==0: 
            pulse_start = time.time() 
 
        while GPIO.input(ECHO)==1: 
            pulse_end = time.time() 
 
        pulse_duration = pulse_end - pulse_start 
 
        distance = pulse_duration * 17160 
        distance = round(distance, 2) 
        data_ort.append(distance) 
         
    average=sum(data_ort)/len(data_ort)   
    GPIO.cleanup()
    print('ziplayan top emre')
    return average 
 
def bw_sensor(): 
    TRIG = 29 
    ECHO = 31 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG,GPIO.OUT) 
    GPIO.setup(ECHO,GPIO.IN) 
    data_ort=[] 
    for j in range(5): 
 
        GPIO.output(TRIG, True) 
        time.sleep(0.1) 
        GPIO.output(TRIG, False) 
 
        while GPIO.input(ECHO)==0: 
            pulse_start = time.time() 
 
        while GPIO.input(ECHO)==1: 
            pulse_end = time.time() 
 
        pulse_duration = pulse_end - pulse_start 
 
        distance = pulse_duration * 17160 
        distance = round(distance, 2) 
        data_ort.append(distance) 
         
    average=sum(data_ort)/len(data_ort)    
    GPIO.cleanup()
    print('baydarin sensoru')
    return average 

# PWM' e benzeyen ama PWM olmayan şey 
#-------------------------------------------

def pwmcik_fw(sensor):
    if sensor >= 30:
        n = 0.5
        return forward(n)
    elif 25 <= sensor < 30:
        n = 0.4
        return forward(n)
    elif 20 <= sensor < 25:
        n = 0.3
        return forward(n)
    else:
        n = 0.2
    return forward(n)

def pwmcik_bw(sensor):
    if sensor >= 30:
        n = 0.5
        return backward(n)
    elif 25 <= sensor < 30:
        n = 0.4
        return backward(n)
    elif 20 <= sensor < 25:
        n = 0.3
        return backward(n)
    else:
        n = 0.2
    return backward(n)

#-------------------------------------------
 
a,b = 1,1 
start_a,start_b = 1,1 
maze = np.ones((10,10)) 
maze[1,1] = 0 
yon = "+x" 
while True: 
    sol_sensor= int(input('sols:')) 
    on_sensor = int(input('ons:'))
    sag_sensor = int(input('sags:')) 
    arka_sensor = int(input('arka:'))
    print(sol_sensor,on_sensor,sag_sensor,arka_sensor)
    if sol_sensor > 10: 
        if yon == "+x": 
            yon="+y" 
            b+=1 
            maze[a,b]=0 
                        
        elif yon == "+y": 
            yon ="-x" 
            a-=1 
            maze[a,b]=0 
             
        elif yon == "-x": 
            yon = "-y" 
            b-=1 
            maze[a,b]=0 
        else: 
            yon = "+x" 
            a+=1 
            maze[a,b]=0
        forward(0.1)
        left()
        time.sleep(1)
        forward()
        time.sleep(1)
    elif on_sensor > 10:
        if yon == "+x": 
             
            a+=1 
            maze[a,b]=0
                        
        elif yon == "+y": 
           
            b+=1 
            maze[a,b]=0 
             
        elif yon == "-x": 
            
            a-=1 
            maze[a,b]=0 
        else: 
             
            b-=1 
            maze[a,b]=0 

        pwmcik_fw(on_sensor)
        time.sleep(1)
             
    elif sag_sensor > 10: 
        if yon == "+x": 
            yon="-y" 
            b-=1 
            maze[a,b]=0 
                        
        elif yon == "+y": 
            yon ="+x" 
            a+=1 
            maze[a,b]=0 
             
        elif yon == "-x": 
            yon = "+y" 
            b+=1 
            maze[a,b]=0 
        else: 
            yon = "-x" 
            a-=1 
            maze[a,b]=0 
        forward(0.1)
        time.sleep(1)
        right()
        time.sleep(1)
        forward()
        time.sleep(1)
    elif arka_sensor > 10:
        if yon == "+x": 
            yon="-x" 
            a-=1 
            maze[a,b]=0 
                        
        elif yon == "+y": 
            yon ="-y" 
            b-=1 
            maze[a,b]=0 
             
        elif yon == "-x": 
            yon = "+x" 
            a+=1 
            maze[a,b]=0 
        elif yon == "-y": 
            yon = "+y" 
            b+=1 
            maze[a,b]=0
        pwmcik_bw(arka_sensor)
        
        time.sleep(1)
    if b == 0:     
         maze = np.append(np.ones((maze.shape[0],1)),maze,axis=1)   
         b += 1 
         start_b += 1      
          
    if a == 0: 
        maze = np.append(np.ones((1, maze.shape[1])),maze,axis=0) 
        a += 1 
        start_a += 1 
         
    if a == maze.shape[0]-1: 
        maze = np.append(maze,np.ones((1, maze.shape[1])),axis=0) 
         
    if b == maze.shape[1]-1: 
        maze = np.append(maze,np.ones((maze.shape[0],1)),axis=1) 
     
    if a == start_a and b == start_b: 
        break 
 
 
liste = list(maze) 
liste2 = [] 
for j in liste: 
    j = str(j) 
    liste2.append(j) 
def MazeToTxt(liste): 
    dosya = open("maze.txt", "w") 
    # Burası sıkıntı çıkarabilir mcks. 
    for i in liste: 
        dosya = open("maze.txt", "a") 
        i = i+"\n" 
        dosya.write(i) 
        dosya.close() 
    return "Labirent Txt Dosyasına yazdırıldı" 
 
 
MazeToTxt(liste2) 
GPIO.output(MOTOR1E,GPIO.LOW)  
GPIO.output(MOTOR1A,GPIO.LOW) 
GPIO.output(MOTOR1B,GPIO.LOW) 
GPIO.output(MOTOR2E,GPIO.LOW)  
GPIO.output(MOTOR2A,GPIO.LOW) 
GPIO.output(MOTOR2B,GPIO.LOW) 
GPIO.cleanup() 
 


       
