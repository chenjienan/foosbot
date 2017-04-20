#!/usr/bin/python

from Tkinter import *


window = Tk()
frame = Frame(window)

btn_1 = Button(frame, text="Need 1", height=20, width=15)
btn_2 = Button(frame, text="Need 2", height=20, width=15)
btn_3 = Button(frame, text="Need 3", height=20, width=15)
btn_4 = Button(frame, text="START", bg="green", height=20, width=15)
btn_5 = Button(frame, text="DONE", bg="red", height=20, width=15)

btn_1.pack(side=LEFT)
btn_2.pack(side=LEFT)
btn_3.pack(side=LEFT)
btn_4.pack(side=LEFT)
btn_5.pack(side=LEFT)

label = Label(window,
              bg="blue",
              fg="black",
              text="How many player do you need?",
              height=5,
              width=50,
              font=(None, 20))
label.pack()
frame.pack()

window.attributes("-fullscreen", True)
window.mainloop()
print "Done"
