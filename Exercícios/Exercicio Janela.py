from tkinter import *
from tkinter import messagebox

def onBtonPressed():
    messagebox.showinfo('Info?',"Button Pressed!");

Main = Tk();
Main.title('Mta Wiki Scraper v2.0');

bton = Button(Main,text='Olá!',command=onBtonPressed);
bton.grid(row=0,column=1,padx=10,pady=10);
#
text = Entry(Main);
text.grid(row=0,column=0,padx=10,pady=10);


Main.mainloop();