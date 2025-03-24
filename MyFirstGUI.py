from tkinter import *

class MyFirstGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        
        self.label1 = Label(master, text="Enter your Firstname")
        self.label1.pack()
        self.entry1 = Entry()
        self.entry1.pack()

        self.label2 = Label(master, text="Enter your Date of Birth")
        self.label2.pack()
        self.entry2 = Entry()
        self.entry2.pack()

        self.label3 = Label(master, text="Enter your Firstname")
        self.label3.pack()
        self.entry3 = Entry()
        self.entry3.pack()

        self.label4 = Label(master, text="Enter your Member Type")
        self.label4.pack()
        self.entry4 = Entry()
        self.entry4.pack()
        
        self.insertintodbButton = Button(master, text="Insert Into DB", command=self.sayhello)
        self.insertintodbButton.pack()

        self.printallmembersButton = Button(master, text="Print All Members", command=self.sayhello)
        self.printallmembersButton.pack()

        self.closeButton = Button(master, text="Close", command=self.close)
        self.closeButton.pack()

    def sayhello(self):    
        print("Hello " + self.entry1.get())

    def close(self):
        root.destroy()

root = Tk()
my_gui = MyFirstGUI(root)
root.dooneevent()
