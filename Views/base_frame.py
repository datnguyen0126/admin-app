import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path
import webbrowser
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import matplotlib.pyplot as plt

PARENT_PATH = Path(__file__).parent.parent
sys.path.insert(0, str(PARENT_PATH))

from Presenters import presenters as p

frame_styles = {"relief": "groove",
                "bd": 3, "bg": "#94b4d1",
                "fg": "#073bb3", "font": ("Arial", 9, "bold")}

class BaseFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        main_frame = tk.Frame(self, bg="#94b4d1", height=900, width=1600)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")