import tkinter
import PIL.Image,PIL.ImageTk
import cv2
import imutils
import time
from functools import partial
import threading

stream= cv2.VideoCapture("runout3.mp4")
flag=True
def play(speed):
    global flag
    print(f"you clicked on play.speed is {speed}")
    
    frame1= stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1 + speed)
    
    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame= imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor = tkinter.NW)
    if flag:
         canvas.create_text(132,26,fill="black",font = "Times 20 bold",text= "Decision Pending")
    flag= not flag   

def out():
    thread=threading.Thread(target=pending,args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")

def pending(decision):
    frame=cv2.cvtColor(cv2.imread("Decision.png"),cv2.COLOR_BGR2RGB)
    frame= imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image= frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    time.sleep(1)
    
    frame=cv2.cvtColor(cv2.imread("Ad.png"),cv2.COLOR_BGR2RGB)
    frame= imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image= frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    time.sleep(1.5)

    if(decision =='out'):
        decisionImg="Out.png"
    else:
        decisionImg= "Notout.png"   
    
    frame=cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)
    frame= imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image= frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

def notout():
    thread=threading.Thread(target=pending,args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")         

SET_WIDTH=650
SET_HEIGHT=369

window=tkinter.Tk()
window.title("THIRD UMPIRE")
img=cv2.imread("Welcome.png")
cv_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()

btn=tkinter.Button(window,text="<<previous(fast)",width=50,command=partial
(play,-25))
btn.pack()

btn=tkinter.Button(window,text="<<previous(slow)",width=50,command=partial
(play,-2))
btn.pack()

btn=tkinter.Button(window,text="next(fast)>>",width=50,command=partial
(play,25))
btn.pack()

btn=tkinter.Button(window,text="next(slow)>>",width=50,command=partial
(play,2))
btn.pack()

btn=tkinter.Button(window,text="Give out",width=50,command=out)
btn.pack()

btn=tkinter.Button(window,text="Give Not Out",width=50,command=notout)
btn.pack()


window.mainloop()