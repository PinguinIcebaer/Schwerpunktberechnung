import numpy as np
import cv2
import os

sourcePath = "python\Schwerpunkt\Amoebe_1.jpg"
targetPath = "python\Schwerpunkt\Amoebe_SP.jpg"

img = cv2.imread(sourcePath, cv2.COLOR_BGR2HSV)

widthP = len(img[0])
heightP = len(img)

area = widthP*heightP
arrPixl =[]

print(widthP, heightP, area)

print(img[0])

counter = 0

for x in range(0, widthP, 1):
    for y in range(0, heightP, 1):

        if img[y][x][0]  >= 130 or img[y][x][1]  >= 130 or img[y][x][2]  >= 250:   
            # img[y][x][2] = 255
            img[y][x][0] = 0
            img[y][x][1] = 0
            counter = counter+1
            coordinates = [x, y]
            arrPixl.append(coordinates)



print(counter)
print(len(arrPixl))
print(arrPixl)

#schwerpunkt ausrechnen
x_schwerpunkt = 0
y_schwerpunkt = 0

for i in range (0, len(arrPixl), 1):
    x_schwerpunkt = x_schwerpunkt + 0.5 + arrPixl[i][0]

x_schwerpunkt = x_schwerpunkt/len(arrPixl)

for i in range (0, len(arrPixl), 1):
    y_schwerpunkt = y_schwerpunkt + 0.5 + arrPixl[i][1]

y_schwerpunkt = y_schwerpunkt/len(arrPixl)

print(round(x_schwerpunkt))
print(round(y_schwerpunkt))

#schwerpunkt auf dem bild markieren

img = cv2.line(img, (round(x_schwerpunkt), 0), (round(x_schwerpunkt), heightP), (0, 0, 0) , 2) 
img = cv2.line(img, (0, round(y_schwerpunkt)), (widthP, round(y_schwerpunkt)), (0, 0, 0) , 2)
img = cv2.circle(img, (round(x_schwerpunkt), round(y_schwerpunkt)), 30, (0, 0, 0) , 2)
# img = cv2.circle(img, (round(x_schwerpunkt), round(y_schwerpunkt)), 60, (0, 0, 0) , 2)



img = cv2.imwrite(targetPath, img)










