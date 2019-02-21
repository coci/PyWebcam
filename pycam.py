
import cv2
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime
from tkinter import messagebox


def CreateWidgets():

    root.label = Label(root,bg = "darkslategray", fg = "white",
                       text = "WEBCAM FEED", font = ('Comic Sans MS',20))
    root.label.pack(padx = 10, pady = 10)

    root.videoLabel = Label(root, bg = "darkslategray")
    root.videoLabel.pack(padx = 10, pady = 10)

    root.captureButton = Button(root, text = "CAPTURE", command = Capture,
                                bg = "LIGHTBLUE", font = ('Comic Sans MS', 10))
    root.captureButton.pack(padx = 10, pady = 10, fill = BOTH)

    
    root.cap = cv2.VideoCapture(0)

    width, height = 640, 480

  
    root.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)

    root.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    
    ShowFeed()

#---

# Defining ShowFeed() function to display webcam feed
def ShowFeed():

    
    _, frame = root.cap.read()

   
    frame = cv2.flip(frame, 1)

   
    cv2.putText(frame,datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                (20, 30), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

    
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    
    videoImg = Image.fromarray(cv2image)

    imgtk = ImageTk.PhotoImage(image = videoImg)

 
    root.videoLabel.configure(image=imgtk)


    root.videoLabel.imgtk = imgtk

    
    root.videoLabel.after(10, ShowFeed)

#---

def Capture():

    name = datetime.now().strftime('%d-%m-%Y %H-%M-%S')

    imgName = name + ".jpg"

    ret, frame = root.cap.read()


    success = cv2.imwrite(imgName, frame)

    if success :
        messagebox.showinfo("SUCCESS", "IMAGE CAPTURED")

#---

root = tk.Tk()

root.title("webcam")
root.configure(background = "darkslategray")
root.resizable(False,False)

CreateWidgets()

root.mainloop()