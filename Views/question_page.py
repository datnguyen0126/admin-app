from .base_frame import *
from models.data import *


class QuestionPageFrame(BaseFrame):
    def __init__(self, parent, app):
        super().__init__(parent)

        text_styles = {"justify": "left",
                       "bg": "#94b4d1",
                       "font": ("Verdana", 9)}

        self.Presenter = p.HomePage(view=self)

        frame_questions = tk.LabelFrame(self, frame_styles,
                                        text="Question table")
        frame_questions.place(rely=0.05, relx=0.02, height=400, width=700)

        frame_answer = tk.LabelFrame(self, frame_styles,
                                     text="Answer table")
        frame_answer.place(rely=0.05, relx=0.47, height=400, width=800)

        self.tv_questions = ttk.Treeview(frame_questions)
        self.tv_questions.place(relheight=1, relwidth=0.995)
        self.ts_questions = tk.Scrollbar(frame_questions)
        self.ts_questions.configure(command=self.tv_questions.yview)
        self.tv_questions.configure(yscrollcommand=self.ts_questions.set)
        self.ts_questions.pack(side="right", fill="y")

        self.tv_answer = ttk.Treeview(frame_answer)
        self.tv_answer.place(relheight=1, relwidth=0.995)
        self.ts_answer = tk.Scrollbar(frame_answer)
        self.ts_answer.configure(command=self.tv_answer.yview)
        self.tv_answer.configure(yscrollcommand=self.ts_answer.set)
        self.ts_answer.pack(side="right", fill="y")
        self.load_headers()

    def load_headers(self):
        self.tv_questions['columns'] = ('Id', 'Content')
        self.tv_questions["show"] = "headings"

        self.tv_questions.heading('Id', text='Id')
        self.tv_questions.column('Id', width=10)
        self.tv_questions.heading('Content', text='Content')
        self.tv_questions.column('Content', width=70)

        self.tv_answer['columns'] = ('Content', )
        self.tv_answer["show"] = "headings"
        self.tv_answer.heading('Content', text='Content')
        self.tv_answer.column('Content', width=100)

        # self.tv_questions.bind('<ButtonRelease-1>', self.selected_product)
