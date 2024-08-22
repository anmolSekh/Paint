# from tkinter import *
from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor

class paint:
    def __init__(self, master):
        self.master = master
        self.color_fg = "black"
        self.color_bg = "white"
        self.x = None
        self.y = None
        self.pen_width = 1
        self.drawWidgets()
        self.C.bind('<B1-Motion>', self.draw)
        self.C.bind('<ButtonRelease-1>', self.reset)

    def draw(self, m):
        if self.x and self.y:
            # self.C.create_line(self.x, self.y, m.x, m.y, width = self.pen_width, fill = self.color_fg, capstyle = 'round', smooth = 'true')
            self.C.create_line(self.x, self.y, m.x, m.y, width = self.pen_width, fill = self.color_fg)
        self.x = m.x
        self.y = m.y

    def reset(self):
        self.x = None
        self.y = None

    def changeWidth(self, W):
        self.pen_width = W
    
    def clearCanvas(self):
        self.C.delete(ALL)

    def change_fg(self):
        self.color_fg = askcolor()
    
    def change_bg(self):
        self.color_bg = askcolor()
        self.C['bg'] = self.color_bg

    def drawWidgets(self):
        self.controls = Frame(self.master, padx=5, pady=5)
        textpw = Label(self.controls, text='Pen Width', font='Georgia 16')
        textpw.grid(row=0, column=0)
        self.slider = ttk.Scale(self.controls, from_=5, to=100, command=self.changeWidth, orient='vertical')
        self.slider.set(self.pen_width)
        self.slider.grid(row=0, column=1)
        self.controls.pack(side='left')
        self.C = Canvas(self.master, bg = self.color_bg, width = 500, height=400)
        self.C.pack(fill=BOTH, expand=True)
    
        menu = Menu(self.master)
        self.master.config(menu=menu)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Menu', menu=optionmenu)
        optionmenu.add_command(label='Brush Color', command=self.change_fg)
        optionmenu.add_command(label='Background Color', command=self.change_bg)
        optionmenu.add_command(label='Clear Canvas', command=self.clearCanvas)
        optionmenu.add_command(label='Exit', command=self.master.destroy)
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column = 0, row = 0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1,row=0)

def key(event):
    print("Click")

def choose_color():
    colorcode = askcolor()
    print(colorcode)

root = Tk()
# C = Canvas(root, bd = 5, bg = "white", width = 700)
# B = Button(root, text = "Select color", command = choose_color)
# C.bind("<Button-1>", key)
# C.pack()
# B.pack()
# root.geometry("300x300")
paint(root)
root.mainloop()