import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk
import cv2
import numpy as np



def calc_schwerpunkt(event):
    global img, label
    file_path = event.data

    #bild in HSV format einlesen
    img = cv2.imread(file_path, cv2.COLOR_BGR2HSV)


    original_img = img.copy()

    
    widthP = len(img[0])
    heightP = len(img)

    area = widthP*heightP
    arrPixl =[]
    counter = 0

    #fläche markieren und zugehörige pixel in array speichern
    for x in range(0, widthP, 1):
        for y in range(0, heightP, 1):

            if img[y][x][0]  >= 130 or img[y][x][1]  >= 130 or img[y][x][2]  >= 250:   
                counter = counter+1
                coordinates = [x, y]
                arrPixl.append(coordinates)

    #schwerpunkt ausrechnen
    x_schwerpunkt = 0
    y_schwerpunkt = 0

    for i in range (0, len(arrPixl), 1):
        x_schwerpunkt = x_schwerpunkt + 0.5 + arrPixl[i][0]

    x_schwerpunkt = x_schwerpunkt/len(arrPixl)

    for i in range (0, len(arrPixl), 1):
        y_schwerpunkt = y_schwerpunkt + 0.5 + arrPixl[i][1]

    y_schwerpunkt = y_schwerpunkt/len(arrPixl)

    #schwerpunkt markieren
    original_img = cv2.line(original_img, (round(x_schwerpunkt), 0), (round(x_schwerpunkt), heightP), (0, 0, 0) , 2) 
    original_img = cv2.line(original_img, (0, round(y_schwerpunkt)), (widthP, round(y_schwerpunkt)), (0, 0, 0) , 2)
    original_img = cv2.circle(original_img, (round(x_schwerpunkt), round(y_schwerpunkt)), 30, (0, 0, 0) , 2) 

    
    image = Image.fromarray(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))
    image.thumbnail((root.winfo_screenwidth(), root.winfo_screenheight()))
    photo = ImageTk.PhotoImage(image)
    
    if label is not None:
        label.destroy()
    label = tk.Label(image=photo, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), borderwidth=2, relief="solid")
    label.image = photo 
    label.pack()


root = TkinterDnD.Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.title("Bildschwerpunkt-Berechnung")
root.configure(bg='lightgrey')
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', calc_schwerpunkt)

label = tk.Label(text="Schwerpunktsberechner")


img = None

root.mainloop()