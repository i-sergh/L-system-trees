import cv2
import numpy as np
from math import pi, sin, cos
from time import sleep
from random import randint
def line_build(dot, ang, leng):
    ang += 90
    return (int(dot [ 0 ]  +  sin( ang * pi/180 ) * leng), int(dot [ 1 ]  +cos( ang* pi/180 ) * leng) )
def color_gen(color, df):
    return (randint(color[0]-df, color[0]), randint(color[1]-df, color[1]), randint(color[2], color[2]) )
cnv = np.ones((1080, 1920, 3), dtype=np.uint8()) * 255

axi = 'A'
omni = axi
leng = 300
color = (0, 0, 0)
ang = 45 #+ randint(-18, 18)
start_tik = 16
start_dot = (960,1080)
last_dot =(960,1080 )

#cv2.line(cnv,(960,1080 ), last_dot , (0, 0, 0), start_tik)
dotty = [[start_dot  , ang]]
rules = {'A': 'AB', 'B':'BA'}
while True:
    cnv = np.ones((1080, 1920, 3), dtype=np.uint8()) * randint(100,150)
    
    axi = 'A'
    omni = axi
    leng = 200
    color = (0, 0, 0)
    ang = 90
    start_tik = 14
    start_dot = (960,1080)
    last_dot =(960,1080 )
    branches =2 
    mas = [
                #(2, 8 ,16),
                #(8, 2, 16),
                #(2, 16, 8),
                #(16, 2, 8),
                (randint(2, 16), randint(2, 16), randint(2, 16)),
                (randint(2, 16), randint(2, 16), randint(2, 16)),
                (randint(2, 16), randint(2, 16), randint(2, 16)),
                (randint(2, 16), randint(2, 16), randint(2, 16)),
                (randint(2, 16), randint(2, 16), randint(2, 16)),
                (randint(2, 16), randint(2, 16), randint(2, 16)),
                (randint(2, 16), randint(2, 16), randint(2, 16))
        ]
    mask_color = (randint(2, 16), randint(2, 16), randint(2, 16))#mas[randint(0,len(mas)-1)] 
    #cv2.line(cnv,(960,1080 ), last_dot , (0, 0, 0), start_tik)
    dotty = [[start_dot  , ang, branches]]
    rules = {'A': 'BA', 'B':'AA'}
    for i in range ( start_tik):
        omni = axi
        axi = ''
        otkl = randint(-25,0)
        dotty_dotty = dotty.copy()
        dotty = []
        for j in range( len( omni ) ):
        
            
            if omni [ j ] =='A' and i != 14:
                
                DOTTY = dotty_dotty[0]
                dotty_dotty[0][2] -= 1
                if dotty_dotty[0][2] == 0:
                    dotty_dotty.pop(0)
                    
                color = (mask_color[0] * i, mask_color[1]*i, mask_color[2]*i)
                axi = axi + rules['A']
            
                if i != 0:
                    otkl = randint(15, 55)
                    
                start_dot = DOTTY[0]   
                ang = DOTTY[1]  
                cv2.line(cnv, start_dot,  line_build( start_dot, ang + otkl, int( leng  / (1+i) ) ) , color, start_tik-i)
              
                dotty = dotty + [[line_build( start_dot, ang + otkl, int(leng /(1+i)) ) , ang + otkl, 2 ]]
                
                
            if omni [ j ] == 'B' and i != 14:
                DOTTY = dotty_dotty[0]
                dotty_dotty[0][2] -= 1
                if dotty_dotty[0][2] == 0:
                    dotty_dotty.pop(0)
                color = (mask_color [0]* i, mask_color[1]*i, mask_color[2]*i)
                axi = axi + rules['B']
                if i != 0:
                    otkl = randint(-55, -15)
                start_dot =DOTTY[0]   
                ang = DOTTY[1]
                cv2.line(cnv, start_dot,  line_build( start_dot, ang + otkl, int( leng  / (1+i) ) ) , color, start_tik-i)

                dotty = dotty + [[line_build( start_dot, ang + otkl, int(leng /(1+i)) ) , ang + otkl , 2]]

           
        
            
            
        cv2.imshow('tree', cnv)
        sleep(0.01 + 0.01 * i/1.5)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    #cv2.waitKey()
    sleep(0.6)
        
    
    
    
