# coding:utf-8  
#!env/usr/bin/python  
  
from Tkinter import *  
  
class App(object):  
    def __init__(self,master):  
        self.com = Button(master,text = '打招呼', command = self.say_hello)      
        self.com.pack(side = BOTTOM)  
         
    def say_hello(self):  
        print '你好，Gui!'  
  
root = Tk()  
root.title('window with command')  
root.geometry('400x200')  
  
app = App(root)  
root.mainloop()
