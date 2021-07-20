import math
import pandas as pd 
print('Program for Electrometric Tacheometry Computation')
print('-------------------------------------------------')
stati_traver = input('Enter the stationary traverse ID')
refer_traver = input('Enter the referenced traverse ID')

first_Y = float(input('Enter the Y coordinates of {} (m)     :'.format(stati_traver)))
first_X = float(input('Enter the X coordinates of {} (m)     :'.format(stati_traver)))
first_height = float(input('Enter the height of {}  (m)'.format(stati_traver)))

second_Y = float(input('Enter the Y coordinates of {} (m)     :'.format(refer_traver)))
second_X = float(input('Enter the X coordinates of {} (m)     :'.format(refer_traver)))
second_height = float(input('Enter the height of {}  (m)'.format(refer_traver)))

point_id = float(input('Enter the point ID of detail point    :'))
hori_direction = float(input('Enter the horizontal direction of point {} (grad)   :'.format(point_id)))
verti_angle = float(input('Enter the vertical angle of point {} (grad )  :'.format(point_id)))

slope_dist = float(input('Enter the slope distance between {} and 1 (m)   :'.format(stati_traver,point_id)))
height_i = float(input('Enter the height of instrument (m)    :'))
height_r = float(input('Enter the height of reflector (m)    :'))

def radFromGrad(grad):
    return math.pi*grad/200
def gradFromRad(rad):
    return rad*200/math.pi

delta_h = slope_dist * math.cos(radFromGrad(verti_angle)) + height_i - height_r
elevation = second_height + delta_h
hor_dist = slope_dist * math.sin(radFromGrad(verti_angle))

dx = second_X - first_X
dy = second_Y - first_Y

t1 = abs(math.atan(dy/dx))
t1 = gradFromRad(t1)

if (dy > 0 and dx < 0):
    t1 = 200 - t1
elif (dy < 0 and dx < 0):
    t1 = 200 + t1
elif (dy > 0 and dx < 0):
    t1 = 400 - t1
    
K = t1 + verti_angle

if K < 200 :
    t = K + 200
elif K > 200 and  K < 600:
    t = K -200
elif K > 600:
    t = K -600

coord_x = first_X + hor_dist * math.cos(radFromGrad(t))
coord_y = first_Y + hor_dist * math.sin(radFromGrad(t))


table = pd.DataFrame({'PointID': [stati_traver],
                      'PointID2':[point_id],
                      'Hor. Dist':[hor_dist],
                      'Delta H':[delta_h],
                      'Elevation':[elevation],
                      'Coord.(Y)':[coord_y],
                      'Coord. (X)':[coord_x]
                      })
print(table)
