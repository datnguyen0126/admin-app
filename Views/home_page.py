from .base_frame import *
from models.data import *
from models.questions import *


class HomePageFrame(BaseFrame):
    def __init__(self, parent, app):
        super().__init__(parent)

        self.form_data = {
            'id': '',
            'name': '',
            'brand': '',
            'price': '',
            'cpu': '',
            'vga': '',
            'ram': '',
            'disk': '',
            'battery': '',
            'dimension': '',
            'display': '',
            'screen_size': '',
            'weight': '',
            'description': ''
        }

        text_styles = {"justify": "left",
                       "bg": "#94b4d1",
                       "font": ("Verdana", 9)}

        self.Presenter = p.HomePage(view=self)

        frame_prices = tk.LabelFrame(self, frame_styles,
                                     text="Product table")
        frame_prices.place(rely=0.05, relx=0.02, height=550, width=500)

        frame_train = tk.LabelFrame(self, frame_styles, text="Train products")
        frame_train.place(rely=0.63, relx=0.02, height=300, width=500)

        frame_filter = tk.LabelFrame(self, frame_styles, text="Filter")
        frame_filter.place(rely=0.05, relx=0.35, height=55, width=1000)

        frame_order = tk.LabelFrame(self, frame_styles, text="Product detail")
        frame_order.place(rely=0.12, relx=0.35, height=440, width=1000)

        frame_score = tk.LabelFrame(self, frame_styles, text="Product Benchmark")
        frame_score.place(rely=0.63, relx=0.35, height=95, width=1000)

        frame_set_train = tk.LabelFrame(self, frame_styles, text="Set train product")
        frame_set_train.place(rely=0.75, relx=0.35, height=110, width=1000)

        frame_classify = tk.LabelFrame(self, frame_styles, text="Classification")
        frame_classify.place(rely=0.87, relx=0.35, height=82, width=1000)

        list_find = ['name', 'cpu']
        self.find_option = tk.StringVar(frame_filter)
        label_find = tk.Label(frame_filter, text_styles, text="Find ")
        label_find.place(relx=0.05, rely=0.06)
        self.option_menu_find = ttk.OptionMenu(frame_filter, self.find_option, list_find[0], *list_find)
        self.option_menu_find.place(relx=0.1, rely=0.06)
        self.entry_find = ttk.Entry(frame_filter, width=50, cursor="xterm")
        self.entry_find.place(relx=0.17, rely=0.06)

        get_btn = ttk.Button(frame_filter, text="Get data", command=lambda: self.load_data())
        get_btn.place(rely=0.06, relx=0.5)

        # row 1
        label_id = tk.Label(frame_order, text_styles, text="id")
        label_id.place(relx=0.02, rely=0.02)
        label_id.place(relx=0.02, rely=0.02)
        self.entry_id = ttk.Entry(frame_order, width=20, cursor="xterm")
        self.entry_id.place(relx=0.05, rely=0.02)

        label_name = tk.Label(frame_order, text_styles, text="name")
        label_name.place(relx=0.2, rely=0.02)
        self.entry_name = ttk.Entry(frame_order, width=40, cursor="xterm")
        self.entry_name.place(relx=0.25, rely=0.02)

        label_brand = tk.Label(frame_order, text_styles, text="brand")
        label_brand.place(relx=0.55, rely=0.02)
        self.entry_brand = ttk.Entry(frame_order, width=20, cursor="xterm")
        self.entry_brand.place(relx=0.6, rely=0.02)

        label_price = tk.Label(frame_order, text_styles, text="price")
        label_price.place(relx=0.75, rely=0.02)
        self.entry_price = ttk.Entry(frame_order, width=20, cursor="xterm")
        self.entry_price.place(relx=0.8, rely=0.02)

        # row 2
        label_cpu = tk.Label(frame_order, text_styles, text="cpu")
        label_cpu.place(relx=0.02, rely=0.1)
        self.entry_cpu = ttk.Entry(frame_order, width=30, cursor="xterm")
        self.entry_cpu.place(relx=0.05, rely=0.1)

        label_vga = tk.Label(frame_order, text_styles, text="vga")
        label_vga.place(relx=0.3, rely=0.1)
        self.entry_vga = ttk.Entry(frame_order, width=50, cursor="xterm")
        self.entry_vga.place(relx=0.35, rely=0.1)

        label_ram = tk.Label(frame_order, text_styles, text="ram")
        label_ram.place(relx=0.7, rely=0.1)
        self.entry_ram = ttk.Entry(frame_order, width=30, cursor="xterm")
        self.entry_ram.place(relx=0.75, rely=0.1)

        # row 3
        label_disk = tk.Label(frame_order, text_styles, text="disk")
        label_disk.place(relx=0.02, rely=0.18)
        self.entry_disk = ttk.Entry(frame_order, width=30, cursor="xterm")
        self.entry_disk.place(relx=0.07, rely=0.18)

        label_dimension = tk.Label(frame_order, text_styles, text="dimension")
        label_dimension.place(relx=0.32, rely=0.18)
        self.entry_dimension = ttk.Entry(frame_order, width=40, cursor="xterm")
        self.entry_dimension.place(relx=0.4, rely=0.18)

        label_battery = tk.Label(frame_order, text_styles, text="battery")
        label_battery.place(relx=0.67, rely=0.18)
        self.entry_battery = ttk.Entry(frame_order, width=30, cursor="xterm")
        self.entry_battery.place(relx=0.75, rely=0.18)

        # row 4
        label_screen_size = tk.Label(frame_order, text_styles, text="screen size")
        label_screen_size.place(relx=0.02, rely=0.26)
        self.entry_screen_size = ttk.Entry(frame_order, width=30, cursor="xterm")
        self.entry_screen_size.place(relx=0.12, rely=0.26)

        label_display = tk.Label(frame_order, text_styles, text="display")
        label_display.place(relx=0.33, rely=0.26)
        self.entry_display = ttk.Entry(frame_order, width=40, cursor="xterm")
        self.entry_display.place(relx=0.4, rely=0.26)

        label_weight = tk.Label(frame_order, text_styles, text="weight")
        label_weight.place(relx=0.67, rely=0.26)
        self.entry_weight = ttk.Entry(frame_order, width=30, cursor="xterm")
        self.entry_weight.place(relx=0.75, rely=0.26)

        # row 5
        label_description = tk.Label(frame_order, text_styles, text="Description")
        label_description.place(relx=0.05, rely=0.34)
        self.entry_description = tk.Text(frame_order, width=110, height=12, cursor="xterm")
        self.entry_description.place(relx=0.05, rely=0.42)

        update_btn = ttk.Button(frame_order, text="Update product", command=lambda: self.update_item())
        update_btn.place(rely=0.91, relx=0.83)

        self.tv_train = ttk.Treeview(frame_train)
        self.tv_train.place(relheight=1, relwidth=0.995)
        self.ts_train = tk.Scrollbar(frame_train)
        self.ts_train.configure(command=self.tv_train.yview)
        self.tv_train.configure(yscrollcommand=self.ts_train.set)
        self.ts_train.pack(side="right", fill="y")
        self.product_headers = ("Id", "Product Name")

        self.tv_all = ttk.Treeview(frame_prices)
        self.tv_all.place(relheight=1, relwidth=0.995)
        self.ts_prices = tk.Scrollbar(frame_prices)
        self.ts_prices.configure(command=self.tv_all.yview)
        self.tv_all.configure(yscrollcommand=self.ts_prices.set)
        self.ts_prices.pack(side="right", fill="y")
        self.price_headers = ("Id", "Product Name", "Price")
        self.load_headers()

        # benchmark frame
        # row 1
        label_detected_cpu = tk.Label(frame_score, text_styles, text="detected cpu")
        label_detected_cpu.place(relx=0.02, rely=0.05)
        self.entry_detected_cpu = ttk.Entry(frame_score, width=20, cursor="xterm")
        self.entry_detected_cpu.place(relx=0.12, rely=0.05)

        label_cpu_score = tk.Label(frame_score, text_styles, text="cpu score")
        label_cpu_score.place(relx=0.27, rely=0.05)
        self.entry_cpu_score = ttk.Entry(frame_score, width=20, cursor="xterm")
        self.entry_cpu_score.place(relx=0.34, rely=0.05)

        label_detected_gpu = tk.Label(frame_score, text_styles, text="detected gpu")
        label_detected_gpu.place(relx=0.5, rely=0.05)
        self.entry_detected_gpu = ttk.Entry(frame_score, width=20, cursor="xterm")
        self.entry_detected_gpu.place(relx=0.6, rely=0.05)

        label_gpu_score = tk.Label(frame_score, text_styles, text="gpu score")
        label_gpu_score.place(relx=0.75, rely=0.05)
        self.entry_gpu_score = ttk.Entry(frame_score, width=20, cursor="xterm")
        self.entry_gpu_score.place(relx=0.85, rely=0.05)


        list_question = ['', ]
        self.list_answer = ['', ]
        try:
            self.question_data = get_all_questions()
            for question in self.question_data:
                if question.get('train'):
                    list_question.append(question.get('content'))

            for answer in self.question_data[0].get('answers'):
                self.list_answer.append(answer.get('content'))

        except:
            list_question = ['', ]

        list_check = ['yes', 'no']

        self.question = tk.StringVar(frame_set_train)
        self.answer = tk.StringVar(frame_set_train)
        self.check = tk.StringVar(frame_set_train)

        self.option_menu_question = ttk.OptionMenu(frame_set_train, self.question, list_question[0], *list_question,
                                                   command=self.load_answer)
        self.option_menu_question.place(relx=0.12, rely=0.1)
        label_question = tk.Label(frame_set_train, text_styles, text="Question")
        label_question.place(relx=0.03, rely=0.1)

        self.option_menu_answer = ttk.OptionMenu(frame_set_train, self.answer,
                                                 self.list_answer[0],
                                                 *self.list_answer)
        self.option_menu_answer.place(relx=0.54, rely=0.1)
        label_answer = tk.Label(frame_set_train, text_styles, text="Answer")
        label_answer.place(relx=0.47, rely=0.1)

        self.option_menu_check = ttk.OptionMenu(frame_set_train, self.check, list_check[0], *list_check)
        self.option_menu_check.place(relx=0.9, rely=0.1)
        label_question = tk.Label(frame_set_train, text_styles, text="Check")
        label_question.place(relx=0.85, rely=0.1)

        self.train_products = []
        self.list_scores = []

        btn_set_train = ttk.Button(frame_set_train, text="Set train products", command=lambda: self.set_train_products())
        btn_set_train.place(relx=0.87, rely=0.52)
        btn_clear = ttk.Button(frame_set_train, text="Clear train products", command=lambda: self.clear_train_products())
        btn_clear.place(relx=0.74, rely=0.52)
        btn_clear = ttk.Button(frame_score, text="Reload score", command=lambda: self.reload_score())
        btn_clear.place(relx=0.9, rely=0.52)

        label_weight = tk.Label(frame_classify, text_styles, text="Classify")
        label_weight.place(relx=0.03, rely=0.2)
        self.entry_class = ttk.Entry(frame_classify, width=20, cursor="xterm")
        self.entry_class.place(relx=0.11, rely=0.2)
        btn_classify = ttk.Button(frame_classify, text="Classify", command=lambda: self.check_item())
        btn_classify.place(relx=0.87, rely=0.2)

    def load_answer(self, value):
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

    def check_item(self):
        response = check_product(self.entry_id.get(), self.answer.get())
        self.entry_class.delete(0,"end")
        self.entry_class.insert(0, response)
        print(response)

    def load_headers(self):

        self.tv_all['columns'] = self.price_headers
        self.tv_all["show"] = "headings"

        for header in self.price_headers:
            self.tv_all.heading(header, text=header)
            self.tv_all.column(header, width=50)

        self.tv_train['columns'] = self.product_headers
        self.tv_train["show"] = "headings"

        for header in self.product_headers:
            self.tv_train.heading(header, text=header)
            self.tv_train.column(header, width=50)

        self.tv_all.bind('<ButtonRelease-1>', self.selected_product)

        self.tv_all.bind('<Double-1>', self.add_product)
        self.tv_train.bind('<Double-1>', self.remove_product)

    def reload_score(self):
        score = reload_score(self.entry_id.get())

        self.entry_detected_cpu.delete(0,"end")
        self.entry_detected_cpu.insert(0, score.get('detected_cpu'))

        self.entry_cpu_score.delete(0,"end")
        self.entry_cpu_score.insert(0, score.get('detected_cpu_score'))

        self.entry_detected_gpu.delete(0,"end")
        self.entry_detected_gpu.insert(0, score.get('detected_gpu'))

        self.entry_gpu_score.delete(0,"end")
        self.entry_gpu_score.insert(0, score.get('detected_gpu_score'))

    def load_data(self):
        self.tv_all.delete(*self.tv_all.get_children())
        data = get_all_product(name=self.entry_find.get(), option=self.find_option.get())
        for row in data:
            self.tv_all.insert('', 'end', values=(row.get('id'), row.get('name'), row.get('price')))

    def set_product_form(self, data, score):
        self.form_data = data.copy()

        self.entry_cpu.delete(0, tk.END)
        self.entry_cpu.insert(0, self.form_data.get('cpu'))

        self.entry_vga.delete(0, tk.END)
        self.entry_vga.insert(0, self.form_data.get('vga'))

        self.entry_ram.delete(0, tk.END)
        self.entry_ram.insert(0, self.form_data.get('ram'))

        self.entry_id.delete(0, tk.END)
        self.entry_id.insert(0, self.form_data.get('id'))

        self.entry_name.delete(0, tk.END)
        self.entry_name.insert(0, self.form_data.get('name'))

        self.entry_brand.delete(0, tk.END)
        self.entry_brand.insert(0, self.form_data.get('brand'))

        self.entry_price.delete(0, tk.END)
        self.entry_price.insert(0, self.form_data.get('price'))

        self.entry_disk.delete(0, tk.END)
        self.entry_disk.insert(0, self.form_data.get('disk'))

        self.entry_battery.delete(0, tk.END)
        self.entry_battery.insert(0, self.form_data.get('battery'))

        self.entry_dimension.delete(0, tk.END)
        self.entry_dimension.insert(0, self.form_data.get('dimension'))

        self.entry_display.delete(0, tk.END)
        self.entry_display.insert(0, self.form_data.get('display'))

        self.entry_screen_size.delete(0, tk.END)
        self.entry_screen_size.insert(0, self.form_data.get('screen_size'))

        self.entry_weight.delete(0, tk.END)
        self.entry_weight.insert(0, self.form_data.get('weight'))

        self.entry_description.delete(1.0,"end")
        self.entry_description.insert(1.0, self.form_data.get('description'))

        self.entry_detected_cpu.delete(0,"end")
        self.entry_detected_cpu.insert(0, score.get('detected_cpu'))

        self.entry_cpu_score.delete(0,"end")
        self.entry_cpu_score.insert(0, score.get('detected_cpu_score'))

        self.entry_detected_gpu.delete(0,"end")
        self.entry_detected_gpu.insert(0, score.get('detected_gpu'))

        self.entry_gpu_score.delete(0,"end")
        self.entry_gpu_score.insert(0, score.get('detected_gpu_score'))
        return

    def selected_product(self, event):
        curItem = self.tv_all.focus()
        product_id = self.tv_all.item(curItem).get('values')[0]
        # print(self.tv_all.item(curItem).get('values')[0])
        item = get_product(product_id)
        score = get_clustering_data(product_id)
        self.set_product_form(item, score)
    
    def add_product(self, event):
        curItem = self.tv_all.focus()
        product = self.tv_all.item(curItem).get('values')
        if product not in self.train_products:
            self.train_products.append(product)
            self.tv_train.insert('', 'end', values=(product[0], product[1], product[2]))

    def remove_product(self, event):
        curItem = self.tv_train.focus()
        product_id = self.tv_train.item(curItem).get('values')[0]
        for row in self.train_products:
            if row[0] == product_id:
                self.train_products.remove(row)
                break

        selected_item = self.tv_train.selection()[0]  ## get selected item
        self.tv_train.delete(selected_item)

    def clear_train_products(self):
        for i in self.tv_train.get_children():
            self.tv_train.delete(i)
        self.train_products = []

    def set_train_products(self):
        laptop_ids = [product[0] for product in self.train_products]
        answer = self.answer.get()
        check = self.check.get()
        set_train_products(laptop_ids, answer, check)

    def update_item(self):
        form_data = {
            'id': '',
            'name': self.entry_name.get(),
            'brand': self.entry_brand.get(),
            'price': self.entry_price.get(),
            'cpu': self.entry_cpu.get(),
            'vga': self.entry_vga.get(),
            'ram': self.entry_ram.get(),
            'disk': self.entry_disk.get(),
            'battery': self.entry_battery.get(),
            'dimension': self.entry_dimension.get(),
            'display': self.entry_display.get(),
            'screen_size': self.entry_screen_size.get(),
            'weight': self.entry_weight.get(),
            'description': self.entry_description.get("1.0",tk.END)
        }
        update_product(self.entry_id.get(), form_data=form_data)

