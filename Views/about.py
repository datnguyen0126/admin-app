from .base_frame import *


class AboutPageWindow(tk.Toplevel):

    def __init__(self):
        super().__init__()

        main_frame = tk.Frame(self)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        self.geometry("500x500")
        self.resizable(0, 0)

        self.title("About")
        bio = """Welcome to training app"""
        frame1 = tk.LabelFrame(main_frame, frame_styles,
                               text="Thank you for viewing")
        frame1.pack(expand=True, fill="both")

        label = tk.Label(frame1, text=bio,
                         font=("Trebuchet MS", 9), bg="#94b4d1")
        label.pack(expand=True)
