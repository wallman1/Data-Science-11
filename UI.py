from logging import debug
import tkinter as tk
from tkinter import ttk
from Functions import search_spell, add_spell_to_spellbook, view_spellbook, list_spells
update = False
LARGEFONT =("Verdana", 35)
smallfont =("Verdana", 11)
class tkinterApp(tk.Tk):
    
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True) 

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {} 

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        # label of frame Layout 2
        label = ttk.Label(self, text ="Start page", font = LARGEFONT)

        myframe = ttk.Label(self, text = "", font=smallfont)
        myscroll = ttk.Scrollbar(myframe, orient='vertical')

        myframe.grid(row = 2, column = 3, padx = 10, pady = 10)
        myscroll.grid(row=2, sticky='ew')
        myscroll.config( command = list_spells())
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 

        button1 = ttk.Button(self, text ="Page 1",
        command = lambda : controller.show_frame(Page1))
    
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Page 2",
        command = lambda : controller.show_frame(Page2))
    
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.text = None
        def listing():
            self.text = ttk.Label(self, text = list_spells(), font = smallfont)
            self.text.grid(row = 2, column = 2, padx = 10, pady = 10)

        button3 = ttk.Button(self, text = "List (Some) Spells", command = listing)
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)
     


# second window frame page1 
class Page1(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Search Spell", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10, sticky = "e")

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))

        # putting the button in its place 
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        name_entry = tk.Entry(self, font=('calibre',10,'normal'))
        name_entry.grid(row = 1, column = 2, padx = 10, pady = 10)
        # button to show frame 2 with text
        # layout2
        self.spell_label=None
        def getandmove():
            name_entry.get()
            print(name_entry.get())
            entry1 = name_entry.get()
            txt = search_spell(entry1)
            txt = str(f"{txt[0:80]}\n{txt[80:160]}\n{txt[160:240]}...")
            if not self.spell_label:
                self.spell_label = ttk.Label(self, text ="Not set yet", font = smallfont)
                self.spell_label.grid(row = 2, column = 2, padx = 10, pady = 10)
            self.spell_label['text']=txt
            if txt == "Spell not found":
                pass
            else:
                add_spell_button = ttk.Button(self, text= "Add Spell", command = lambda: add_spell_to_spellbook(entry1))
                add_spell_button.grid(row = 2, column = 3, padx = 10, pady = 10)
            
        button3 = ttk.Button(self, text="Get text", command=lambda: getandmove())
        button3.grid(row = 1, column = 3, padx =10 , pady =10)
        button2 = ttk.Button(self, text ="View Spellbook",
                            command = lambda : controller.show_frame(Page2))
    
        # putting the button in its place by 
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

# third window frame page2
class Page2(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Spellbook", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Search Spells",
                            command = lambda : controller.show_frame(Page1))
    
        # putting the button in its place by 
        # using grid
        self.label2 = None
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        txt = str(view_spellbook())
        label2 = ttk.Label(self, text =txt, font = smallfont)
        label2.grid(row = 2, column = 2, padx = 10, pady = 10)

        def updatespellbook():
            label2
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage))
        button3 = ttk.Button(self, text = "List Spells", command = lambda: controller.show_frame(Page3))
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)
    
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

class Page3(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(Page1))
    
        # putting the button in its place by 
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage))
    
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

# Driver Code
app = tkinterApp()
app.mainloop()