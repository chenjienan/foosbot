#!/usr/bin/python

from Tkinter import *
import tkMessageBox
import slack


class IdleMode:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.btn_1 = Button(
            self.frame,
            text="1",
            font=(None, 80),
            height=13,
            width=2,
            command=self.need_1_player
        )
        
        self.btn_2 = Button(
            self.frame,
            text="2",
            font=(None, 80),
            height=13,
            width=2,
            command=self.need_2_players
        )
        
        self.btn_3 = Button(
            self.frame,
            text="3",
            font=(None, 80),
            height=13,
            width=2,
            command=self.need_3_players
        )
        
        self.done_btn = Button(
            self.frame,
            text="DONE",
            bg="red",
            fg="white",
            activeforeground="white",
            activebackground="red",
            height=13,
            width=16,
            font=(None, 10))
        
        self.start_btn = Button(
            self.frame,
            text="START",
            bg="green",
            
            fg="white",
            activeforeground="white",
            activebackground="green",
            height=13,
            width=16,
            font=(None, 10),
            command=self.go_to_game)

        self.btn_1.pack(side=LEFT)
        self.btn_2.pack(side=LEFT)
        self.btn_3.pack(side=LEFT)
        self.done_btn.pack(side=LEFT)
        self.start_btn.pack(side=LEFT)

        self.top_label = Label(self.master,
                               bg="blue",
                               fg="white",
                               text="Players needed",
                               height=3,
                               width=50,
                               font=(None, 20))

        self.bottom_label = Label(self.master,
                                  height=2,
                                  width=50,
                                  text = "test",
                                  font=(None, 10))

        self.top_label.pack()
        self.frame.pack()
        self.bottom_label.pack()

    def go_to_game(self):
        self.new_window = Toplevel(self.master)
        self.new_window.attributes("-fullscreen", True)
        self.app = GameMode(self.new_window)

    def need_1_player(self):
        slack.send_message("Need 1 player")
        
    def need_2_players(self):
        slack.send_message("Need 2 players")
        
    def need_3_players(self):
        slack.send_message("Need 3 players")
        
        
        
class GameMode:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.quit_btn = Button(self.frame, text="QUIT", height=20, width=20, command=self.confirm_quit)
    
        self.label = Label(self.master,
                           bg="red",
                           fg="white",
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
