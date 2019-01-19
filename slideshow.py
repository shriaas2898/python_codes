from tkinter import *
import time

images=["DSC_0511","DSC_0512"]
def slide():
    #while True:
        for i in images:
            image = PhotoImage(file=i+".JPG.png")
            label = Label(image=image)
            #label.place(x=0,y=0)
            label.pack(fill=BOTH,expand=2)
            #time.sleep(5)

fr = Tk()
btn=Button(fr,text="start",command=slide)
btn.pack()
fr.mainloop()
