import math
import pandas as pd
print('This program calculates the coordinates in open traverse serie')
print('--------------------------------------------------------------')

first_known = input('Enter the point ID of first known point    :')
first_y = float(input('Enter the Y coordinates of first known point (m)  :'))
first_x = float(input('Enter the x coordinates of first known point (m)  :'))

second_known = input('Enter the point ID of second known point    :')
second_y = float(input('Enter the Y coordinates of second known point (m)  :'))
second_x = float(input('Enter the x coordinates of second known point (m)  :'))

unknown_number = int(input('Enter the number of unknown traverse points   :'))

points = []
for i in range(unknown_number):
    p = input('Enter the point ID of unknown point    :')
    points.append(p)
c = False
if(len(points)== 1):
    c = True
    
#Edit Data
point_id = []
point_id.append(first_known)
point_id.append(second_known)
for i in points[:len(points)-1]:
    point_id.append(i)

point_id_2=[]
point_id_2.append(second_known)
point_id_2.extend(points)
#-----------------------

traverse_member = []
traverse_member.append(second_known)
for i in range(len(points)):
    traverse_member.append(points[i])
    if (i == len(points) -2):
        break

traverse_angle = []
for i in traverse_member:
    traverse_angle.append(float(input('Enter the traverse angle of {} (grad)    :'.format(i))))
    
horizontal_distance = []

for i in range(len(point_id_2)):
    a = float(input('Enter the horizontal distance between {} and {} (m)    :'
                    .format(point_id_2[i],point_id_2[i+1])))
    horizontal_distance.append(a)
    if(i == len(point_id_2)-2):
        break
    
def radFromGrad(grad):
    return math.pi*grad/200
def gradFromRad(rad):
    return rad*200/math.pi

#calculate first azimuth
delta_y = second_y - first_y
delta_x = second_x - first_x
t = abs(math.atan(delta_y/delta_x))
t = gradFromRad(t)

if (delta_y > 0 and delta_x < 0):
    t = 200 - t
elif (delta_y < 0 and delta_x < 0):
    t = 200 + t
elif (delta_y > 0 and delta_x < 0):
    t = 400 - t

#Calculate the azimuth between points A and B

azimuth = []
azimuth.append(t)
for i in traverse_angle:
    b = i
    K = t + b
    if (K < 200):
        t = K +200
        azimuth.append(t)
    elif(K > 200 and K < 600):
        t = K - 200
        azimuth.append(t)
    else:
        t = K - 600
        azimuth.append(t)

if (c == True):
    azimuth.pop()
#Calculate Delta X and Delta Y
d_y = []
d_x = []
Sn = horizontal_distance
for i in range(len(Sn)):
    d_y.append(Sn[i] * math.sin(radFromGrad(azimuth[i+1])))
    d_x.append(Sn[i] * math.cos(radFromGrad(azimuth[i+1])))


#Calculate Coordinate
x_coordinate = []
y_coordinate = []

x_coordinate.append(second_x)
y_coordinate.append(second_y)


for i in range(len(horizontal_distance)):
    X_new = x_coordinate[i] + d_x[i] 
    Y_new = y_coordinate[i] + d_y[i]
    x_coordinate.append(X_new)
    y_coordinate.append(Y_new)

d_y.insert(0,None)
d_x.insert(0,None)


y_coordinate.pop(0)
x_coordinate.pop(0)

table_1  = pd.DataFrame({
    'Point ID':point_id,
    'Point ID 2':point_id_2,
    'Azimuth':azimuth,
    'Delta Y':d_y,
    'Delta X':d_x
    })
table_2  = pd.DataFrame({
    'Point ID':points,
    'Coordinate (Y)':y_coordinate,
    'Coordinate (X)':x_coordinate
    })

print(table_1)
print(table_2)  
