from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
root=Tk()
root.geometry("1200x720")
root.title("Notepad")

def newfile():
    global file
    root.title("Untitled - Notepad")
    file=None
    textarea.delete(1.0,END)
def openfile():
    global file
    file=askopenfilename(defaultextension="*.txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file)+' - Notepad')
        textarea.delete(1.0,END)
        f=open(file,'r')
        textarea.insert(1.0,f.read())
def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='untitled.txt', defaultextension="*.txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=='':
            file=None
        else:
            f=open(file,'w')
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+' - Notepad')
    else:
        f=open(file,'w')
        f.write(textarea.get(1.0,END))
        f.close()
def cut():
    textarea.event_generate(("<<Cut>>"))
def copy():
    textarea.event_generate(("<<Copy>>"))
def paste():
    textarea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","Notepad by hiten")

file=None
textarea=Text(root,font="lucida 13")
textarea.pack(fill=BOTH,expand=True)
mainmenu=Menu(root)
filemenu=Menu(mainmenu,tearoff=0)
filemenu.add_command(label="New",command=newfile)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save",command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=filemenu)
editmenu=Menu(mainmenu,tearoff=0)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=editmenu)
helpmenu=Menu(mainmenu,tearoff=0)
helpmenu.add_command(label="About",command=about)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=helpmenu)
scroll=Scrollbar(textarea)
scroll.pack(fill=Y,side=RIGHT)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)
root.mainloop()