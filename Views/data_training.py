from .base_frame import *
from models.questions import *
from models.data import *
import matplotlib.pyplot as pyplot
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np


class TrainingFrame(BaseFrame):
    def __init__(self, parent, app):
        super().__init__(parent)

        text_styles = {"bg": "#94b4d1",
                       "font": ("Verdana", 9)}

        self.Presenter = p.SecurityPrices(view=self)

        frame_options = tk.LabelFrame(self, frame_styles, text="Choose option")
        frame_options.place(rely=0.05, relx=0.05, relheight=0.2, relwidth=0.30)

        frame_train = tk.LabelFrame(self, frame_styles, text="Training products")
        frame_train.place(rely=0.27, relx=0.05, relheight=0.3, relwidth=0.30)

        frame_all = tk.LabelFrame(self, frame_styles, text="Chart symbol")
        frame_all.place(rely=0.6, relx=0.05, relheight=0.3, relwidth=0.30)

        frame_chart = tk.LabelFrame(self, frame_styles, text="Chart")
        frame_chart.place(rely=0.05, relx=0.4, relheight=0.86, relwidth=0.55)

        self.canvas_chart = tk.Canvas(frame_chart, bg="blue")
        self.canvas_chart.pack(expand=True, fill="both")

        self.entry_color = ttk.Entry(frame_options, width=30, cursor="xterm")
        self.entry_color.place(relx=0.25, rely=0.1)
        label_color = tk.Label(frame_options, text_styles, text="Set color")
        label_color.place(relx=0.05, rely=0.1)
        btn_add_chart = ttk.Button(frame_options, text="Add chart", command=lambda: self.add_to_chart())
        btn_add_chart.place(relx=0.66, rely=0.1)
        btn_del_chart = ttk.Button(frame_options, text="Clear chart", command=lambda: self.clear_chart_table())
        btn_del_chart.place(relx=0.83, rely=0.1)

        list_question = ['', ]
        self.list_answer = ['', ]
        try:
            self.question_data = get_all_questions()
            for question in self.question_data:
                list_question.append(question.get('content'))

            for answer in self.question_data[0].get('answers'):
                self.list_answer.append(answer.get('content'))

        except:
            pass

        self.question = tk.StringVar(frame_options)
        self.answer = tk.StringVar(frame_options)

        self.option_menu_question = ttk.OptionMenu(frame_options, self.question, list_question[0], *list_question,
                                                   command=self.load_answer)
        self.option_menu_question.place(relx=0.25, rely=0.3)
        label_question = tk.Label(frame_options, text_styles, text="Question")
        label_question.place(relx=0.05, rely=0.3)

        self.option_menu_answer = ttk.OptionMenu(frame_options, self.answer, self.list_answer[0], *self.list_answer)
        self.option_menu_answer.place(relx=0.25, rely=0.55)
        label_answer = tk.Label(frame_options, text_styles, text="Answer")
        label_answer.place(relx=0.05, rely=0.55)

        btn_draw = ttk.Button(frame_options, text="Draw Chart", command=lambda: self.initiate_chart())
        btn_draw.place(relx=0.8, rely=0.75)
        btn_reset = ttk.Button(frame_options, text="Clear train", command=lambda: self.clear_train_products())
        btn_reset.place(relx=0.2, rely=0.75)
        btn_fetch = ttk.Button(frame_options, text="Get train data", command=lambda: self.get_train_data())
        btn_fetch.place(relx=0.6, rely=0.75)

        self.tv_train = ttk.Treeview(frame_train)
        self.tv_train.place(relheight=1, relwidth=0.995)
        self.ts_train = tk.Scrollbar(frame_train)
        self.ts_train.configure(command=self.tv_train.yview)
        self.tv_train.configure(yscrollcommand=self.ts_train.set)
        self.ts_train.pack(side="right", fill="y")
        self.product_headers = ("Id", "Product Name")

        self.tv_all = ttk.Treeview(frame_all)
        self.tv_all.place(relheight=1, relwidth=0.995)
        self.ts_all = tk.Scrollbar(frame_all)
        self.ts_all.configure(command=self.tv_all.yview)
        self.tv_all.configure(yscrollcommand=self.ts_all.set)
        self.ts_all.pack(side="right", fill="y")
        self.all_headers = ("Answer", "Color")

        self.canvas1 = None
        self.toolbar = None

        self.train_products = []
        self.chart_list = dict()
        self.list_scores = []

        self.x_arr = []
        self.y_arr = []

        self.load_headers()

    def load_headers(self):

        self.tv_train['columns'] = self.product_headers
        self.tv_train["show"] = "headings"
        self.tv_all['columns'] = self.all_headers
        self.tv_all["show"] = "headings"

        for header in self.product_headers:
            self.tv_train.heading(header, text=header)
            self.tv_train.column(header, width=50)
        for header in self.all_headers:
            self.tv_all.heading(header, text=header)
            self.tv_all.column(header, width=50)

        self.tv_train.bind('<Double-1>', self.remove_product)

    def remove_product(self, event):
        curItem = self.tv_train.focus()
        product_id = self.tv_train.item(curItem).get('values')[0]
        for row in self.train_products:
            if row[0] == product_id:
                self.train_products.remove(row)
                break

        selected_item = self.tv_train.selection()[0]  ## get selected item
        self.tv_train.delete(selected_item)

    def clear_chart_table(self):
        for i in self.tv_all.get_children():
            self.tv_all.delete(i)
        self.chart_list = {}

    def clear_train_products(self):
        for i in self.tv_train.get_children():
            self.tv_train.delete(i)
        self.train_products = []

    def get_train_data(self):
        self.clear_train_products()
        answer = self.answer.get()
        data = get_train_products(answer)
        self.train_products = data
        for row in self.train_products:
            self.tv_train.insert('', 'end', values=(row.get('id'), row.get('laptop_name')))

    def add_to_chart(self):
        for i in self.tv_all.get_children():
            self.tv_all.delete(i)
        self.chart_list[self.entry_color.get()] = self.train_products
        for key in self.chart_list.keys():
            self.tv_all.insert('', 'end', values=(key, self.chart_list[key][0].get('answer_name')))

    def load_answer(self, value):
        print(self.chart_list.keys())
        question = {}
        for question in self.question_data:
            if question.get('content') == value:
                question = question
                break
        self.list_answer = []
        for answer in question.get('answers'):
            self.list_answer.append(answer.get('content'))
        menu = self.option_menu_answer["menu"]
        menu.delete(0, "end")
        for answer in self.list_answer:
            menu.add_command(label=answer, command=lambda value=answer: self.answer.set(value))

    def initiate_chart(self):
        self.remove_existing_chart()

        print(self.chart_list.keys())

        figure = plt.Figure(figsize=(4, 5), facecolor="#f0f6f7", dpi=80)

        axis = figure.add_subplot(111)

        axis.set_xlim(0, 20001)
        axis.set_ylim(0, 20001)
        major_ticks = np.arange(0, 20001, 1000)
        minor_ticks = np.arange(0, 20001, 1000)

        axis.set_xticks(major_ticks)
        axis.set_xticks(minor_ticks, minor = True)
        axis.set_yticks(major_ticks)
        axis.set_yticks(minor_ticks, minor = True)

        for key in self.chart_list.keys():
            train_data = self.chart_list[key]
            list_scores = []
            for arr in train_data:
                product_id = arr.get('laptop')
                score = get_clustering_data(product_id)
                list_scores.append(score)

            x_arr = []
            y_arr = []
            for score in list_scores:
                x_arr.append(int(score.get('detected_cpu_score')))
                y_arr.append(int(score.get('detected_gpu_score')))

            axis.scatter(x_arr, y_arr, s=100, c=key, marker='o', label='benchmark')

        axis.set_xlabel('Cpu benchmark')
        axis.set_ylabel('Gpu benchmark')
        axis.set_title('Activities Scatter Graph')

        canvas = FigureCanvasTkAgg(figure, self.canvas_chart)
        self.canvas1 = canvas.get_tk_widget()
        self.canvas1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        canvas._tkcanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def remove_existing_chart(self):
        if self.canvas1 is not None:
            self.canvas1.destroy()
        if self.toolbar is not None:
            self.toolbar.destroy()
