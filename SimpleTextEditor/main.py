import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from errorhandle import ErrorHandler as error
from parser import Parser as lang_parser
from tkinter.filedialog import asksaveasfile
import os
import tkinter
import platform
import tkinter.scrolledtext as scrolledtext



class TextEditor(object):
    global textbox
    global CurrentOpenFile
    global filename
    global root
    def Main():
        global CurrentOpenFile
        CurrentOpenFile = None
        global root
        root = tk.Tk()
        root.title("Untitled - VCTX")
        root.geometry("800x600")
        global currentbuild
        currentbuild = lang_parser.LoadResource("VCTX_VERSION")
        global textbox 
        textbox =scrolledtext.ScrolledText(root, undo=True)

        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        helpmenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=TextEditor.New)
        filemenu.add_command(label="Save", command=TextEditor.Save)
        filemenu.add_command(label="Save As", command=TextEditor.SaveAs)
        filemenu.add_command(label="Open", command=TextEditor.Open)
        helpmenu.add_command(label="About", command=TextEditor.About)
        root.bind('<Control-s>', TextEditor.CTRLS_SAVE)
        root.protocol("WM_DELETE_WINDOW",  TextEditor.on_close)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Help", menu=helpmenu)
        root.config(menu=menubar)
        textbox.pack(expand=True, fill=BOTH)
        root.mainloop()

    def Open():
        filename = fd.askopenfilename()
        if filename != "":
            try:
                f = open(filename)
                textbox.delete("1.0", END)
                textbox.insert("1.0", f.read())
                global CurrentOpenFile
                CurrentOpenFile = filename
                root.title(os.path.basename(CurrentOpenFile) + " - VCTX")
            except:
                error.DisplayError("Cannot open file!", "The file you have tried to open isn't supported or is corrupted in some way", True)
                TextEditor.New()
    def About():
        tkinter.messagebox.showinfo(title="About VCTX", message=f"Current Build:{currentbuild}\nCurrent Operating System:{platform.platform()}")
        

    def New():
        textbox.delete("1.0", END)
        TextEditor.CurrentOpenFile = None
        root.title("Untitled - VCTX")

    def CTRLS_SAVE(self):
        TextEditor.Save() 

    def Save():
        if CurrentOpenFile == None:
            TextEditor.SaveAs()
            
        else:
            f = open(CurrentOpenFile, "w")
            f.write(textbox.get("1.0", "end"))
            f.close()

    def on_close(): 
        if CurrentOpenFile == None:
            MsgBox = tk.messagebox.askyesnocancel ('Exiting VCTX','Would you like to save your untitled project?',icon = 'warning')
            if MsgBox == True:
                TextEditor.SaveAs()
                root.destroy()
            elif MsgBox == False:
                root.destroy()
            elif MsgBox == None:
                return
        else:
            root.destroy()

    def SaveAs():
        files = [('All Files', '*.*'), 
                ('Python Files', '*.py'),
                ('Text Document', '*.txt')]
        file = asksaveasfile(filetypes = files, defaultextension = ".py")
        textboxcontent = textbox.get("1.0", "end")
        if file:
            with open(file.name, "w") as f:
                f.write(textboxcontent)
                global CurrentOpenFile
                CurrentOpenFile = file.name
                root.title(os.path.basename(CurrentOpenFile) +" - VCTX")



TextEditor.Main()