from tkinter import *
from math import *
from time import *

class myClock:
    def __init__(self,rootwindows):
        self.root=rootwindows
        self.root.title("我愛Python")
        
        self.frame0=Frame(self.root)
        self.frame0.pack()

        self.label0=Label(self.frame0,text="分：秒")
        self.label0.pack(side = LEFT)

        self.frame1=Frame(self.root)
        self.frame1.pack()
        self.entry1=Entry(self.frame1,width=3)
        self.entry1.pack(side = LEFT)
        self.entry2=Entry(self.frame1,width=3)
        self.entry2.pack(side = LEFT)
        

        self.button1=Button(self.frame1,text ="Enter",width=3,command=self.getTime)
        self.button1.pack(side = LEFT)
        
        

        self.frame2=Frame(self.root)
        self.frame2.pack()

        self.v = StringVar()
        self.labelTime=Label(self.frame2,textvariable=self.v)
        self.labelTime.pack()
           
        self.frame=Frame(self.root)       
        self.frame.pack()
        
        self.canvas=Canvas(self.frame,height=300,width=400)
        self.canvas.pack()       
        self.secArmLen=100 #秒針長度
        self.center=200,150 #建構"(200,150)" 也就是中心點的座標
        self.clock=self.canvas.create_oval(100,50,300,250)#黑色線的圓圈
        self.secArmSeg=self.canvas.create_line(200,150,200,50)#黑色線的秒針
        self.ticButton=Button(self.frame,text="Start",command=self.secArmMove)
        self.ticButton.pack()
        self.ticNum=0
        
        self.stop = False
    def secArmMove(self):
        
        if self.stop == False:
            self.ticNum+=1
            nx=self.secArmLen*cos(((15-self.ticNum%60)*6)/360*2*3.14159)#出函數就沒了，內定函數
            ny=self.secArmLen*sin((15-self.ticNum%60)/30*3.14159)
            self.canvas.coords(self.secArmSeg,200,150,200+nx,150-ny)
            self.seconds-=1
            mins=int(self.seconds)//60
            secs=int(self.seconds)%60
            
            if self.seconds == 0:
                self.stop = True

            self.v.set(str(mins)+":"+str(secs))
            self.root.after(1000,self.secArmMove)

    def getTime(self):
        self.mins = int(self.entry1.get())
        self.seconds = int(self.entry2.get())
        self.seconds = int( self.mins*60 + self.seconds )


root=Tk()
clock=myClock(root)
root.mainloop()
