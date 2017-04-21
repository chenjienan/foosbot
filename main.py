#!/usr/bin/python

from Tkinter import *
import tkMessageBox
import slack_api


class IdleMode:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.prompt = StringVar()

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
            text="CANCEL",
            bg="red",
            fg="white",
            activeforeground="white",
            activebackground="red",
            command=self.clear_game,
            height=20,
            width=16,
            font=(None, 10))

        self.start_btn = Button(
            self.frame,
            text="START",
            bg="green",

            fg="white",
            activeforeground="white",
            activebackground="green",
            height=20,
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
                               height=5,
                               width=50,
                               font=(None, 20))

        self.bottom_label = Label(self.master,
                                  height=2,
                                  width=50,
                                  textvariable=self.prompt,
                                  font=(None, 10))

        self.top_label.pack()
        self.bottom_label.pack()
        self.frame.pack()


    def go_to_game(self):
        self.prompt.set("")
        slack_api.send_message("An epic foosball game has begun!")
        self.new_window = Toplevel(self.master)
        self.new_window.attributes("-fullscreen", True)
        self.app = GameMode(self.new_window)

    def need_1_player(self):
        self.prompt.set("Last Request: 1 player")
        slack_api.send_message("Need 1 player")

    def need_2_players(self):
        self.prompt.set("Last Request: 2 players")
        slack_api.send_message("Need 2 players")

    def need_3_players(self):
        self.prompt.set("Last Request: 3 players")
        slack_api.send_message("Need 3 players")

    def clear_game(self):
        self.prompt.set("")
        slack_api.send_message("Nobody's coming? Alright, cancelling game request :crying_cat_face:")


class GameMode:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master, borderwidth=5, relief="sunken")
        self.frame.grid(row=0, column=0)

        self.quit_btn = Button(
            self.frame,
            width=100, height=8,
            text="Instant Replay",
            ).grid(row=0, column=0,columnspan=2)

        self.team1Frame = Frame(self.frame, borderwidth=5, relief="sunken", width=50, height=10)
        self.team1Label = Label(self.team1Frame,
                                text="Team 1",
                                width=50, height=2)

        
        self.team1Frame.grid(row=1, column=0)
        
        self.team2Frame = Frame(self.frame, borderwidth=5, relief="sunken", width=50, height=10)
        self.team2Frame.grid(row=1, column=1)

        
        self.quit_btn = Button(
            self.frame,
            text="DONE",
            width=100, height=3,
            command=self.confirm_quit
            ).grid(row=2, column=0,columnspan=2)

        

    
        
    def back_to_idle(self):
        self.master.destroy()

    def confirm_quit(self):
        result = tkMessageBox.askyesno("Confirmation", "Do you want to end your game?", icon='warning', parent=self.master)
        if result:
            self.back_to_idle()
            slack_api.send_message("Game finished!")


def main():
    root = Tk()
    app = IdleMode(root)
    root.attributes("-fullscreen", True)
    root.mainloop()


if __name__ == '__main__':
    main()
    print "Done"
