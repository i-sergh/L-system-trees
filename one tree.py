import cv2
import numpy as np
from random import randint
from math import pi, sin, cos
from time import sleep
                        #B    #G  #R
clr = np.array([220, 230, 250], dtype=np.uint8() )

cnv = np.ones ( (1080, 1920, 3), dtype=np.uint8() ) * clr


def endDot (dot, ang, leng):
    ang +=  90
    return (  int(   dot[0]  + sin(ang * pi/180 ) *leng    )   , int(   dot[1]  + cos(ang * pi/180 ) *leng    ) )


cv2.imshow('tree',  cnv)

cv2.waitKey()


#####


cur_rules = 'A' # аксиома оно же будет содержать все правила

kubik = randint(0,3)

# генерирует по одному из указаных правил
if kubik == 1:
    # Акация
    rules = {'A' : 'AB', 'B': 'AA' }
elif kubik == 2:
    #Тополиный пух
    rules = {'A' : 'AB', 'B': 'BB' }
elif kubik == 3:
    #Плакучий одуванчик
    rules = {'A' : 'BB', 'B': 'BB' }
else:
    # прямое  дерево
    rules = {'A' : 'AB', 'B': 'AB' }

#rules = {'A' : 'AAB', 'B': 'B' }    

leng = 200 # длина px

situas = randint( 0, 3)
ang = 90
start_thik = randint(6, 12)
start_dot = (960+ randint( -700, 700) , 1080)

tree_color = [ randint(0,16), randint(0,16), randint(0,16) ]
branches = len(rules['A']) # сколько веток порождает правило
list_of_dots =[ [start_dot, ang, branches]  ] # параметры точек

for i in range(start_thik ):

    buf_cur_rules = cur_rules # копируем список правил
    cur_rules = ''                      # не забываем очистить
    
    copy_list = list_of_dots.copy() #копируем список точек
    list_of_dots = []                         # не забываем очистить
    
    dev_ang = randint(-5, 5) #отклонение
    for j in range( len(  buf_cur_rules  ) ):
        if buf_cur_rules[ j ] == 'A' :
            
            cur_branch = copy_list[0] #достаем ветку
            copy_list[0][2] -= 1
            
            color = (tree_color[0] * i, tree_color[1]*i, tree_color[2]*i)
            
            if copy_list[0][2] == 0: #удаляем уже использованные правила
                copy_list.pop(0)
                
            cur_rules = cur_rules + rules['A']


            if i != 0:
                dev_ang = randint(15, 55) # выравниваем угол отклонения

            start_dot = cur_branch[0] 
            ang = cur_branch[1]
            end_dot = endDot( start_dot,  ang + dev_ang , int( leng / ( 1+i ) ) )
            cv2.line(
                    cnv,
                    start_dot,
                    end_dot,
                    color,
                    start_thik-i
                    )
            list_of_dots = list_of_dots + [  [
                                                                end_dot,
                                                                ang + dev_ang, #угол, под которым лежит наша ветвь
                                                                len(rules['A']) # количество порождаемых ветвей по правилу
                                                                ] ]
        if buf_cur_rules[ j ] == 'B' :

            cur_branch = copy_list[0]
            copy_list[0][2] -= 1


            color = (tree_color[0] * i, tree_color[1]*i, tree_color[2]*i)

            if copy_list[0][2] == 0:
                copy_list.pop(0)

            cur_rules = cur_rules + rules['B']

            if i != 0:
                dev_ang = randint(-55, -15)

            start_dot = cur_branch[0]
            ang = cur_branch[1]
            end_dot  = endDot(start_dot, ang + dev_ang, int(leng/ (1+i)))

            cv2.line(
                    cnv,
                    start_dot,
                    end_dot,
                    color,
                    start_thik-i
                    )
            list_of_dots = list_of_dots + [ [
                end_dot,
                ang + dev_ang,
                len(rules['B'])
                ] ]
            
    cv2.imshow('tree', cnv)
    sleep(0.01 + 0.01 * i/1.5)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
