#!/usr/bin/python

from Tkinter import *


window = Tk()
frame = Frame(window)

btn_1 = Button(frame, text="Need 1")
btn_2 = Button(frame, text="Need 2")
btn_3 = Button(frame, text="Need 3")
btn_4 = Button(frame, text="START")
btn_5 = Button(frame, text="DONE")

btn_1.pack(side=LEFT)
btn_2.pack(side=LEFT)
btn_3.pack(side=LEFT)
btn_4.pack(side=LEFT)
btn_5.pack(side=LEFT)

label = Label(window, text="How many player do you need?")
label.pack()
frame.pack()

window.attributes("-fullscreen", True)
window.mainloop()
print "Done"
