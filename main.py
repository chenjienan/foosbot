#!/usr/bin/python

from Tkinter import *
import tkMessageBox


class IdleMode:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.btn_1 = Button(self.frame, text="Need 1", height=20, width=15)
        self.btn_2 = Button(self.frame, text="Need 2", height=20, width=15)
        self.btn_3 = Button(self.frame, text="Need 3", height=20, width=15)
        self.start_btn = Button(self.frame, text="START", bg="green", height=20, width=15, command=self.go_to_game)
        self.done_btn = Button(self.frame, text="DONE", bg="red", height=20, width=15)

        self.btn_1.pack(side=LEFT)
        self.btn_2.pack(side=LEFT)
        self.btn_3.pack(side=LEFT)
        self.start_btn.pack(side=LEFT)
        self.done_btn.pack(side=LEFT)

        self.label = Label(self.master,
                           bg="blue",
                           fg="black",
                           text="How many player do you need?",
                           height=5,
                           width=50,
                           font=(None, 20))

        self.label.pack()
        self.frame.pack()

    def go_to_game(self):
        self.new_window = Toplevel(self.master)
        self.new_window.attributes("-fullscreen", True)
        self.app = GameMode(self.new_window)
        
        
class GameMode:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.quit_btn = Button(self.frame, text="QUIT", height=20, width=20, command=self.confirm_quit)
    
        self.label = Label(self.master,
                           bg="red",
                           fg="black",
                           text="We are in the Game!",
                           height=5,
                           width=50,
                           font=(None, 20))
        
        self.label.pack()
        self.quit_btn.pack()
        self.frame.pack()

    def back_to_idle(self):
        self.master.destroy()

    def confirm_quit(self):
        result = tkMessageBox.askyesno("Confirmation", "Do you want to end your game?", icon='warning', parent=self.master)
        if result:
            self.back_to_idle()

            
def main():
    root = Tk()
    app = IdleMode(root)
    root.attributes("-fullscreen", True)
    root.mainloop()


if __name__ == '__main__':
    main()
    print "Done"
