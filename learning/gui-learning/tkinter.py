from Tkinter import *


class Application(Frame):
    """A GUI application with three button"""

    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        #"""Create three buttons"""
        #Create first buttom
        btn1 = Button(self.master, text="I do nothing")
        btn1.pack()

        #Create second button
        btn2 = Button(self.master, text="T do nothing as well")
        btn2.pack()

        #Create third button
        btn3 = Button(self.master, text="I do nothing as well as well")
        btn3.pack()


root = Tk()
root.title("Lazy Button 2")
root.geometry("500x500")
app = Application(root)
root.mainloop()