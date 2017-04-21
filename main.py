#!/usr/bin/python

from Tkinter import *
import tkMessageBox
import slack_api
import picamera
import camera
import shutil
import config
import subprocess


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
        slack_api.send_message(":soccer:  *An epic foosball game has begun!*")
        self.new_window = Toplevel(self.master)
        self.new_window.attributes("-fullscreen", True)
        self.app = GameMode(self.new_window)

    def need_1_player(self):
        self.prompt.set("Last Request: 1 player")
        slack_api.send_message("1", "players_needed")
        
    def need_2_players(self):
        self.prompt.set("Last Request: 2 players")
        slack_api.send_message("2", "players_needed")
        
    def need_3_players(self):
        self.prompt.set("Last Request: 3 players")
        slack_api.send_message("3", "players_needed")
        
    def clear_game(self):
        self.prompt.set("")
        slack_api.send_message(":soccer: Nobody's coming? Alright, cancelling game request :crying_cat_face:")


class GameMode:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.grid(row=0, column=0)
        self.team1Score = IntVar()
        self.team1Score.set(0)
        self.team1Color = StringVar()
        self.team1Color.set("medium blue")
        
        self.team2Score = IntVar()
        self.team2Score.set(0)
        self.team2Color = StringVar()
        self.team2Color.set("darkorange1")
        

        self.quit_btn1 = Button(
            self.frame,
            width=32, height=2,
            font=(None, 29),
            text="Instant Replay (not available yet)",
            bg="purple",
            command=self.create_instant_replay
            ).grid(row=0, column=0,columnspan=2)

        self.team1Frame = Frame(self.frame, borderwidth=2, relief="sunken"
                                , width=49, height=10,bg=self.team1Color.get())
        self.team1Label = Label(
            self.team1Frame,
            text="Team 1",
            width=49,
            height=2,
            bg=self.team1Color.get())
        self.team1Label.grid(row=0, column=0,columnspan=2)
        
        self.team1_addPnt_btn = Button(
            self.team1Frame,
            width=2,
            height=1,
            text="+",
            font=(None, 82),
            command=self.team1_addPoint,
            bg=self.team1Color.get()
            ).grid(row=1, column=0)

        self.team1Label = Label(
            self.team1Frame,
            textvariable=self.team1Score,
            font=(None, 80),
            width=2,
            height=1,
            bg=self.team1Color.get())
        self.team1Label.grid(row=1, column=1,rowspan=2)
        
        self.team1_removePnt_btn = Button(
            self.team1Frame,
            width=2,
            height=1,
            text="-",
            font=(None, 82),
            command=self.team1_removePoint,
            bg=self.team1Color.get()
            ).grid(row=2, column=0)


        self.team1Frame.grid(row=1, column=0)


        
        self.team2Frame = Frame(
            self.frame, borderwidth=2, relief="sunken"
            , width=49, height=10,bg=self.team2Color.get())
        
        self.team2Label = Label(
            self.team2Frame,
            text="Team 2",
            width=49,
            height=2,
            bg=self.team2Color.get())
        self.team2Label.grid(row=0, column=0,columnspan=2)
        self.team2Label = Label(
            self.team2Frame,
            textvariable=self.team2Score,
            font=(None, 80),
            width=2,
            height=1,
            bg=self.team2Color.get())
        self.team2Label.grid(row=1, column=0,rowspan=2)

        self.team2_addPnt_btn = Button(
            self.team2Frame,
            width=2,
            height=1,
            text="+",
            font=(None, 82),
            command=self.team2_addPoint,
            bg=self.team2Color.get()
            ).grid(row=1, column=1)

        self.team2_removePnt_btn = Button(
            self.team2Frame,
            width=2,
            height=1,
            text="-",
            font=(None, 82),
            command=self.team2_removePoint,
            bg=self.team2Color.get()
            ).grid(row=2, column=1)
        self.team2Frame.grid(row=1, column=1)

        self.quit_btn = Button(
            self.frame,
            text="DONE",
            width=35, height=1,
            font=(None, 27),
            command=self.confirm_quit,
            bg="green"
            ).grid(row=2, column=0,columnspan=2)

        camera.start_recording()
        

    def team1_addPoint(self):
        self.team1Score.set(self.team1Score.get()+1)
        self.reportScore()

    def team1_removePoint(self):
        self.team1Score.set(self.team1Score.get()-1)
        self.reportScore()

    def team2_addPoint(self):
        self.team2Score.set(self.team2Score.get()+1)
        self.reportScore()

    def team2_removePoint(self):
        self.team2Score.set(self.team2Score.get()-1)
        self.reportScore()

    def reportScore(self):
        slack_api.send_message(
            ":soccer: *Current Game Update* \n Team 1 - "
            + str(self.team1Score.get()) + " VS Team 2 - "
            + str(self.team2Score.get()))

    def back_to_idle(self):
        self.master.destroy()

    def confirm_quit(self):
        result = tkMessageBox.askyesno("Confirmation", "Do you want to end your game?", icon='warning', parent=self.master)
        if result:
            self.back_to_idle()
            slack_api.send_message(":soccer: *Game finished!*")

    def create_instant_replay(self):
        shutil.copyfile(config.video_path, config.replay_video_path)
        #self.instantReplay = subprocess.Popen(['omxplayer', config.replay_video_path])
        #self.instantReplay.wait()
        

            
def main():
    root = Tk()
    app = IdleMode(root)
    root.attributes("-fullscreen", True)
    root.mainloop()


if __name__ == '__main__':
    main()
    print "Done"
