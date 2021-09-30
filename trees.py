import cv2
import numpy as np
from math import pi, sin, cos
from time import sleep
from random import randint

def line_build(dot, ang, leng):
    # возвращает конечную точку линии ( tuple ) по начальной точке (dot), её длины (leng) и углу наклона(ang)

    ang += 90 
    return ( int( dot [ 0 ]  +  sin( ang * pi/180 ) * leng), int(dot [ 1 ]  +cos( ang* pi/180 ) * leng) )






# создаем фоновый цвет для нашего канваса с помощью функции array()
clr = np.array([220, 230, 250], dtype=np.uint8())

# создаем канвас нашего изображения с помощью функции ones()
# для покраски в нужный нам цветумножаем канвас на созданный ранее массив 
cnv = np.ones((1080, 1920, 3), dtype=np.uint8()) * clr

# запускаем наш канвас
cv2.imshow('tree', cnv)
# ожидаем любой кнопки
cv2.waitKey()

# запускаем основной цикл
while True:
    # начальные значения нашего дерева
    
    cur_rules = 'A' # константа L-sys
    
    leng = 200 # стартовая длина 
    ang = 90 # стартовый угол
    start_thik = randint(10, 14) # стартовая толщина и число итераций
    start_dot = (960+ randint(-700,700),1080)
    branches = 2 # количество ветвей после исполнения правила ( правило Aоставляет возможность роста двум ветвям)
    tree_color = (randint(2, 16), randint(2, 16), randint(2, 16)) # случайный цвет листьев
    
    list_of_dots = [[start_dot  , ang, branches]] # 
    
    rules = {'A': 'BA', 'B':'AA'} # основные правила L-sys
    for i in range ( start_thik):

        buf_cur_rules = cur_rules 
        cur_rules = '' # Очищаем для перезаписи

        
        copy_list = list_of_dots.copy()
        list_of_dots = [] # Очищаем для перезаписи
        
        #dev_ang = randint(-25,10)
        dev_ang  = 0
        for j in range( len( buf_cur_rules  ) ):
            
            if buf_cur_rules [ j ] =='A' and i != 14:
                cur_branch = copy_list[0]
                copy_list[0][2] -= 1 # отнимаем из счетчика доступных ветвей

                if copy_list[0][2] == 0: # если нет доступных ветвей 
                    copy_list.pop(0)     #  удаляем информацию о характеристиках ветки
            
                color = (tree_color[0] * i, tree_color[1]*i, tree_color[2]*i)
                cur_rules = cur_rules + rules['A']

                if i != 0:
                    dev_ang = randint(15, 55)
                
                start_dot = cur_branch[0]
                ang = cur_branch[1]

                cv2.line(cnv,
                             start_dot,
                             line_build( start_dot,
                                                ang + dev_ang ,
                                                int( leng  / (1+i) ) ) ,
                             color,
                             start_thik-i)
                
                list_of_dots = list_of_dots +  [ [ line_build( start_dot, ang + dev_ang , int( leng /(1+i) ) ) , ang + dev_ang, 2 ] ]

            if  buf_cur_rules [ j ] == 'B' and i != 14:
                cur_branch = copy_list[0]
                copy_list[0][2] -= 1 # отнимаем из счетчика доступных ветвей
                
                if copy_list[0][2] == 0: # если нет доступных ветвей 
                    copy_list.pop(0)     #  удаляем информацию о характеристиках ветки

                color = (tree_color[0] * i, tree_color[1]*i, tree_color[2]*i)
                cur_rules = cur_rules + rules['B']

                if i != 0:
                    dev_ang = randint(-55, -15)

                start_dot = cur_branch[0]
                ang = cur_branch[1]

                cv2.line(cnv,
                             start_dot,
                             line_build( start_dot,
                                                ang + dev_ang ,
                                                int( leng  / (1+i) ) ) ,
                             color,
                             start_thik-i)
                
                list_of_dots = list_of_dots +  [ [ line_build( start_dot, ang + dev_ang , int( leng /(1+i) ) ) , ang + dev_ang , 2 ] ]
            

        cv2.imshow('tree', cnv)
        sleep(0.01 + 0.01 * i/1.5)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    sleep(0.2)
                
                
