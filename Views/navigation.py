import tkinter as tk
from .home_page import HomePageFrame
from .question_page import QuestionPageFrame
from .data_training import TrainingFrame


class NavBar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        menu_styles = {"tearoff": 0, "bd": 5,
                       "activebackground": "#d9d9d9",
                       "background": "#FFFFFF",
                       "activeforeground": "#000000"}


        menu_file = tk.Menu(self, menu_styles)
        self.add_cascade(label="Home", menu=menu_file)
        menu_file.add_command(label="Data list",
                              command=lambda:
                              parent.show_frame(HomePageFrame))
        menu_file.add_command(label="Question list",
                              command=lambda:
                              parent.show_frame(QuestionPageFrame))
        menu_file.add_separator()
        menu_file.add_command(label="Exit",
                              command=lambda:
                              parent.Quit_application())


        menu_pricing = tk.Menu(self, menu_styles)
        self.add_cascade(label="Data training", menu=menu_pricing)
        menu_pricing.add_command(label="Data training",
                                 command=lambda:
                                 parent.show_frame(TrainingFrame))

        # Help
        menu_help = tk.Menu(self, menu_styles)
        self.add_cascade(label="Help", menu=menu_help)
        menu_help.add_command(label="About...",
                              command=lambda:
                              parent.AboutMe())
