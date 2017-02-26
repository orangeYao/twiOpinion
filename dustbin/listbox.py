#coding:utf-8 
from Tkinter import *

class App(object):
    """
    建立左右两个列表，两个列表中的内容可以通过左右按钮交换
    """
    def __init__(self,root):
        self.language = 'Python','Perl','C','Ruby','PHP','Java' 
        self.leftbox = StringVar()
        self.leftbox.set(self.language)
        self.rightbox = StringVar()
        self.rightbox.set('')
           
        self.list_left = Listbox(root, listvariable = self.leftbox, width = 16)
        self.list_left.pack(side = LEFT)

        self.frame = Frame(root)
        self.frame.pack(side = LEFT)
        Button(self.frame, text = '->', command = self.move_to_right, width = 7).pack(side = TOP)
        Button(self.frame, text = '<-', command = self.move_to_left, width = 7).pack(side = TOP)

        self.list_right = Listbox(root, listvariable = self.rightbox)
        self.list_right.pack(side = RIGHT)

    def move_to_right(self):
        """
        将左列表中的内容移动到右列表中，用Listbox中的curselection()方法来捕捉鼠标选中的条目
        用delete()方法删除选中条目，用insert(END，)方法来向列表尾插入条目
        """
        self.list_right.insert(END,self.list_left.get(self.list_left.curselection()))
        self.list_left.delete(self.list_left.curselection())

    def move_to_left(self):
        self.list_left.insert(END,self.list_right.get(self.list_right.curselection()))
        self.list_right.delete(self.list_right.curselection())

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
        

