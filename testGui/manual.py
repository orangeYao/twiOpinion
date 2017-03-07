# -*- coding: utf-8 -*-
import Tkinter as tk
import AppKit

tweet=""
count=1

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("")
        self.master.resizable(False, False)
        self.master.tk_setPalette(background='#ececec')

        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 3
        self.master.geometry("+{}+{}".format(x, y))

        self.master.config(menu=tk.Menu(self))

        tk.Message(self, text= "Choose class 1, class 2, or skip by clicking buttons Σ( ° △ °|||)︴", 
                           font='System 14 bold', justify='left', aspect=1800).pack(pady=(5, 0))
        tk.Message(self, text="Tweet No. "+str(count) +": "+tweet,
                    justify='left', aspect=800).pack(pady=(5, 0))


def manual(t, c):
    global tweet
    tweet=t
    global count
    count = c
    root = tk.Tk()
    app = App(root)
    app.mainloop()

if __name__ == '__main__':
    info = AppKit.NSBundle.mainBundle().infoDictionary()
    info['LSUIElement'] = True
    manual("This is a long long testing message hahahhaha ~~~~You can also use elegant structures like tabs and marks to locate specific sections of the text, and apply changes to those areas. Moreover, you can embed windows and images in the text because this widget was designed to handle both plain and formatted text.", 9)
