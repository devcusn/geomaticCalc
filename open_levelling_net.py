import pandas as pd
print('This program calculates the elevations in open levelling net')
print('-------------------------------------------------------------')
point_known = input('Enter the point ID of known point :  ')
elevation = float(input('Enter the elevation of point {} :  '.format(point_known)))
unknown = int(input('Enter the number of unknown points :'))
unknown_list = []
BS = []
FS = []

for i in range(1,unknown+1):
    v = input('Enter the point ID of unknown point {}  :'.format(i))
    unknown_list.append(v)
    
BS_point_known = float(input('Enter the BS reading of point {} (m)  :'.format(point_known)))

for i in unknown_list:
    FS_value = float(input('Enter the FS reading of point {} (m)  :'.format(i)))
    FS.append(FS_value)
    if(i != unknown_list[len(unknown_list)-1]):
        BS_value = float(input('Enter the BS reading of point {} (m)  :'.format(i)))
        BS.append(BS_value)


#edit data
points = []
points.append(point_known)

for i in unknown_list:
    points.append(i)
    
BS_list = []
BS_list.append(BS_point_known)
for i in BS:
    BS_list.append(i)
FS_list = FS

#height differeces
height_list = []
for i in range(len(unknown_list)):
    height_list.append(BS_list[i] - FS_list[i])
    
#The elevations of points are calculated sequentially as
el_list = []
el_list.append(elevation)
for i in range(len(unknown_list)):
    el_list.append(el_list[i] + height_list[i])


first_table = pd.DataFrame({
    'Point ID':points[0:len(points)-1],
    'Point ID2':points[1:len(points)],
    'Delta H':height_list
    })
print('---------------------------------')
second_table = pd.DataFrame({
    'Point ID':points[1:len(points)],
    'Elevation':el_list[1:]
    })

print(first_table)
print(second_table)
    



























