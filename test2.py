import customtkinter
from PIL import Image
import getdata

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
return_data = None


class Apps(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("testing")
        self.resizable(False, False)
        self.data = None
        self.index_id = None
        self.index_name = None
        self.value: str = ""
        self.my_font = customtkinter.CTkFont(family="fantasy", size=20, weight='bold')
        self.frame_main = customtkinter.CTkFrame(master=self)
        self.label_image = customtkinter.CTkImage(light_image=Image.open("D:/Downloads/test.png"),
                                                  size=(400, 400))
        self.label_image = customtkinter.CTkLabel(self.frame_main, image=self.label_image, text="")
        self.label_image.pack()

        self.frame_main.pack(side='left', fill='both', expand=True)
        self.theme_mode = customtkinter.CTkLabel(self.frame_main, text="Theme Mode:", anchor="w")
        self.theme_mode.pack()
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.frame_main, values=["Light", "Dark",
                                                                                                "System"],
                                                                       command=self.theme_window)
        self.appearance_mode_optionemenu.pack(anchor='center')
        self.frame_content = customtkinter.CTkFrame(master=self)
        self.frame_content.pack(side='right', expand=True, fill='both')

        # content
        self.tabview = customtkinter.CTkTabview(self.frame_content, width=200)
        self.tabview.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.frame_kiri = self.tabview.add("LOGIN")
        self.options = self.tabview.add("OPTIONS")

        self.label_font = customtkinter.CTkLabel(self.options, text="Text-Family")
        self.font = customtkinter.CTkOptionMenu(self.options, values=["Segoe UI", "Arial", "Calibri", "Tahoma"],
                                                command=self.change_font)
        self.label_weight_font = customtkinter.CTkLabel(self.options, text="Text-Weight")
        self.weight_font = customtkinter.CTkOptionMenu(self.options, values=["italic", "normal", "bold"],
                                                       command=self.change_weigth)
        self.label_scaling = customtkinter.CTkLabel(self.options, text="Scaling-Window")
        self.scaling_window = customtkinter.CTkOptionMenu(self.options, values=["80%", "100%", "120%"],
                                                          command=self.change_window)
        self.label_font.grid(column=0, row=0, pady=(10, 0))
        self.font.grid(column=1, row=0, padx=(0, 30), pady=(10, 0))
        self.label_weight_font.grid(column=0, row=1, pady=(10, 0))
        self.weight_font.grid(column=1, row=1, padx=(0, 30), pady=(10, 0))
        self.label_scaling.grid(column=0, row=2, pady=(10, 0))
        self.scaling_window.grid(column=1, row=2, padx=(0, 30), pady=(10, 0))

        self.tabview.add("Tab 3")
        self.tabview.tab("LOGIN").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("OPTIONS").grid_columnconfigure(0, weight=1)

        # slidebar
        self.scroll_frame_kiri = customtkinter.CTkScrollableFrame(master=self.frame_kiri, orientation="vertical",
                                                                  width=400,
                                                                  height=200)
        self.scroll_frame_kiri.grid(row=1, column=0, padx=(5, 5), pady=(5, 0))
        self.textbox = customtkinter.CTkTextbox(master=self.scroll_frame_kiri, height=140)
        self.textbox.pack(expand=True, fill="both", pady=(5, 50))
        self.textbox.insert("0.0",
                            "Habbit Tracker\n\n" + "Pixela is a tool or service that has various aspects depending on "
                                                   "how you use it.As a recording tool, as a visualization tool. "
                                                   "Sometimes, as a full-managed day-series database.Use Pixela "
                                                   "freely without being bound by stereotypes."
                                                   "\n\n")
        self.frame_sliders = customtkinter.CTkFrame(master=self.scroll_frame_kiri)
        self.frame_sliders.pack(expand=True, fill="both", pady=(0, 60))
        self.slider_1 = customtkinter.CTkSlider(self.frame_sliders, from_=0, to=24, orientation="vertical",
                                                width=20,
                                                command=self.count_slider)
        self.slider_1.place(relx=0.1, rely=0)

        # as
        self.label_title = customtkinter.CTkLabel(master=self.frame_sliders, text="Habit Tracker",
                                                  font=self.my_font)
        self.entry_label = customtkinter.CTkEntry(master=self.frame_sliders, placeholder_text='username',
                                                  corner_radius=50, width=200, height=35)
        self.entry_quantity = customtkinter.CTkEntry(master=self.frame_sliders, placeholder_text="quantity",
                                                     corner_radius=50,
                                                     width=200, height=35)

        self.button_checmark = customtkinter.CTkCheckBox(master=self.frame_sliders, text="", fg_color="green",
                                                         checkbox_width=15,
                                                         checkbox_height=15, state='disabled', border_width=3)
        self.button_checmark_2 = customtkinter.CTkCheckBox(master=self.frame_sliders, text="", fg_color="green",
                                                           checkbox_width=15,
                                                           checkbox_height=15, state='disabled', border_width=3)
        # left bar
        self.left_bar = customtkinter.CTkTabview(master=self.frame_content, width=250)
        self.left_bar.grid(row=0, column=1, padx=(5, 5), pady=(5, 5), sticky="nsew", rowspan=2)
        # self.image_retina = customtkinter.CTkImage(light_image=Image.open('image/retina.png'),size=(200,200))
        # self.image_Das = customtkinter.CTkLabel(master=self.tab_info,image=self.image_retina,text="")
        # self.image_Das.pack()

        self.tab_info = self.left_bar.add("INFO")
        self.tab_info.configure(width=300)

        self.tab_akun = self.left_bar.add("Personal")
        self.input_akun = customtkinter.CTkEntry(master=self.tab_akun, placeholder_text="[a-z][a-z0-9-]{1,32}",
                                                 corner_radius=50, width=180)
        self.linput_akun_ = customtkinter.CTkLabel(master=self.tab_akun, text="Name")
        self.linput_akun_.grid(column=0, row=0, padx=(10, 30))
        self.input_akun.grid(column=1, row=0)

        self.input_graphs = customtkinter.CTkEntry(master=self.tab_akun, placeholder_text="[a-z][1-9] ",
                                                   corner_radius=50, width=180)
        self.graphs_new = customtkinter.CTkLabel(master=self.tab_akun, text="Name Graphs")
        self.input_graphs.grid(column=1, row=1)
        self.graphs_new.grid(column=0, row=1, padx=(10, 30), pady=(8, 8))

        self.input_colour = customtkinter.CTkEntry(master=self.tab_akun, placeholder_text="[shibafu,momiji,sora,etc]",
                                                   corner_radius=50, width=180)
        self.colour_new = customtkinter.CTkLabel(master=self.tab_akun, text="Color Graphs")
        self.input_colour.grid(column=1, row=2)
        self.colour_new.grid(column=0, row=2, padx=(10, 30), pady=(8, 8))

        self.input_type_data = customtkinter.CTkEntry(master=self.tab_akun, placeholder_text="[int or float]",
                                                      corner_radius=50, width=180)
        self.type_new = customtkinter.CTkLabel(master=self.tab_akun, text="Type")
        self.input_type_data.grid(column=1, row=3)
        self.type_new.grid(column=0, row=3, padx=(10, 30), pady=(8, 8))

        self.input_unit = customtkinter.CTkEntry(master=self.tab_akun,
                                                 placeholder_text="[commit,kilogram,calory]",
                                                 corner_radius=50, width=180)
        self.unit_new = customtkinter.CTkLabel(master=self.tab_akun, text="Unit")
        self.input_unit.grid(column=1, row=4)
        self.unit_new.grid(column=0, row=4, padx=(10, 30), pady=(8, 8))

        self.graphs_id = customtkinter.CTkEntry(master=self.tab_akun,
                                                placeholder_text="[secret number]",
                                                corner_radius=50, width=180)
        self.graphs_id_new = customtkinter.CTkLabel(master=self.tab_akun, text="Graphs Password")
        self.graphs_id.grid(column=1, row=5)
        self.graphs_id_new.grid(column=0, row=5, padx=(10, 30), pady=(8, 8))

        self._image_button = customtkinter.CTkImage(light_image=Image.open("D:/Downloads/user-plus-solid (1).png"),
                                                    size=(34, 24))

        self.button_create_user = customtkinter.CTkButton(master=self.tab_akun, image=self._image_button,
                                                          text="Creat User"
                                                          , corner_radius=20, anchor="w")
        self.button_create_user.grid(column=0, row=6, columnspan=2, pady=(40, 0))
        self.or_ = customtkinter.CTkLabel(master=self.tab_akun, text="or", font=('arial', 14, 'bold'))
        self.or_.grid(column=0, row=7, pady=(5, 5), columnspan=2)

        self.superuser = customtkinter.CTkImage(light_image=Image.open("D:/Downloads/icons8-profile-50.png"),
                                                size=(30, 30))
        self.button_superuser = customtkinter.CTkButton(master=self.tab_akun, image=self.superuser, text="Login Admin",
                                                        corner_radius=20, anchor='w')
        self.button_superuser.grid(column=0, row=8, columnspan=2)

        if self.entry_label.get() == "":
            self.button_checmark.deselect()
        self.entry_graphid = customtkinter.CTkEntry(master=self.frame_sliders, placeholder_text="graphid",
                                                    height=35,
                                                    width=200,
                                                    corner_radius=50)

        self.button = customtkinter.CTkButton(master=self.frame_sliders, text="Click", hover=True, height=35,
                                              width=200,
                                              font=self.my_font,
                                              border_spacing=2, corner_radius=30, command=self.click)
        self.label_title.place(relx=0.48, rely=0.1, anchor='center')
        self.entry_label.place(relx=0.5, rely=0.5, anchor='center')
        self.button_checmark.place(relx=0.9, rely=0.35)
        self.button_checmark_2.place(relx=0.9, rely=0.2)
        self.entry_graphid.place(relx=0.5, rely=0.3, anchor='center')
        self.entry_quantity.place(relx=0.5, rely=0.7, anchor='center')
        self.button.place(relx=0.5, rely=0.9, anchor='center')

        self.scrollable_frame = customtkinter.CTkScrollableFrame(master=self.frame_content, label_text="Tabel",
                                                                 orientation="horizontal", width=400)

        self.scrollable_frame.grid(row=1, column=0, padx=(5, 5), pady=(5, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=2)
        self.image = customtkinter.CTkImage(light_image=Image.open("image/python.png"), size=(720, 135))
        self.label_image = customtkinter.CTkLabel(self.scrollable_frame, image=self.image, text="")
        self.label_image.pack()

    def click(self):
        self.entry_label.insert(0, "alihusain")
        self.entry_graphid.insert(0, "asd12es")
        self.index_name = self.entry_label.get()
        self.index_id = self.entry_graphid.get()
        print(self.value)
        self.data = getdata.Data(self.index_name, self.index_id, self.entry_quantity.get())
        self.data.data_return_checkmark(self.button_checmark)
        self.data.data_return_checkmark_id(self.button_checmark_2)
        if self.data.execus():
            self.data.add_pixel()
            # self.data.get_retina()
            global return_data
            return_data = self.data.openweb()
            self.entry_graphid.delete(0, customtkinter.END)
            self.entry_label.delete(0, customtkinter.END)
            self.data.dwonload_pixel()
            self.data.get_data_all()
            self.frame_data()
            self.data.website()

    def create_akun(self):
        self.data = getdata.CData(username=str(self.input_akun), name_graphs=self.graphs_new, type_data=self.type_new,
                                  color=self.colour_new, unit=self.unit_new, graphid=self.graphs_id)
        self.data.creat_user()
        self.data.creat_graphs()
        self.data.save_data()

    @staticmethod
    def theme_window(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def frame_data(self):
        self.image.configure(light_image=Image.open("image/python.png"))

    def count_slider(self, value):
        self.entry_quantity.delete(0, customtkinter.END)
        self.value = int(round(value))
        self.entry_quantity.insert(0, self.value)

    def change_font(self, new_scaling: str):
        font = new_scaling
        self.my_font.configure(family=new_scaling)

    def change_weigth(self, font: str):
        font = font
        self.my_font.configure(weight=font)

    def change_window(self, new_scaling: str):
        self.resizable(True, True)
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
        self.resizable(False, False)


if __name__ == "__main__":
    run = Apps()
    run.mainloop()
