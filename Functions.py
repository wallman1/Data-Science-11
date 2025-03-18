import customtkinter
#from testing import *

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.button_1 = customtkinter.CTkButton(self, text="Button 1")
        self.button_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.button_2 = customtkinter.CTkButton(self, text="Button 2")
        self.button_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        def button_callback(self):
           scene2.mainloop()


class Scene2(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.button_1 = customtkinter.CTkButton(self, text="Button 1", command=self)
        self.button_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.button_2 = customtkinter.CTkButton(self, text="Button 2")
        self.button_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        def button_callback(self):
           app.mainloop() 

scene2 = Scene2()
app = App()
app.mainloop()