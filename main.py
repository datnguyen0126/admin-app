import tkinter as tk
from setups.setup import Setup_database_tables, check_configurations
import os
from Views import *
from models.config import Configurations

# Portfolio Reconciliation and Management System (PRMS)

DATABASE_NAME = Configurations.DATABASE_NAME
# SETUP #
check_configurations()

if not os.path.exists(DATABASE_NAME):
    current_dir = os.getcwd()
    db_path = current_dir + r"\{}".format(DATABASE_NAME)  # create database
    Setup_database_tables(db_path)
###


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Traning app")
        main_frame = tk.Frame(self, bg="#84CEEB", height=900, width=1600)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        self.resizable(0, 0)
        self.geometry("1600x900")
        self.frames = {}
        pages = (HomePageFrame,
                 TrainingFrame,
                 QuestionPageFrame)

        for page in pages:
            frame = page(parent=main_frame, app=self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePageFrame)
        menubar = navigation.NavBar(self)
        tk.Tk.config(self, menu=menubar)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def AboutMe(self):
        AboutPageWindow()

    def Quit_application(self):
        self.destroy()


if __name__ == "__main__":
    root = Application()
    root.mainloop()
