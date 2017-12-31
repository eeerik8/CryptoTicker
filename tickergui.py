import tickerdata
import tkinter

class ticker:
    def __init__(self, master):
        self.master = master
        master.title("Cryptocurrency Ticker v0.1")

        self.label = tkinter.Label(master, text="Cryptocurrency Ticker v0.1")
        self.label.pack()

        self.text = tkinter.Text(master, width=40, height = 10)
        self.text.insert('1.0', 'here is my text to insert')
        self.text.pack()


root = tkinter.Tk()
my_gui = ticker(root)
root.mainloop()