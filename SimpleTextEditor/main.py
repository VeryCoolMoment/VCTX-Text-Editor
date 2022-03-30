import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from errorhandle import ErrorHandler as error
from tkinter.filedialog import asksaveasfile



class TextEditor:
    global textbox
    global isFileSaved
    global CurrentOpenFile
    isFileSaved = False
    global filename
    global root
    def Main():
        CurrentOpenFile = "null"
        global root
        root = tk.Tk()
        root.title("Text Editor")
        root.geometry("800x600")
        global textbox 
        textbox = tk.Text(root)
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=TextEditor.New)
        filemenu.add_command(label="Save", command=TextEditor.Save)
        filemenu.add_command(label="Save As", command=TextEditor.SaveAs)
        filemenu.add_command(label="Open", command=TextEditor.Open)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)
        textbox.pack(expand=True, fill=BOTH)
        
        root.mainloop()
    def Open():
        filename = fd.askopenfilename()
        print(filename)
        if filename != "":

            f = open(filename)
            textbox.delete("1.0", END)
            textbox.insert("1.0", f.read())
            TextEditor.isFileSaved = True 
            TextEditor.CurrentOpenFile = filename
            #global root
            root.title("Current Open File - VCM's Editor")
        


    def New():
        textbox.delete("1.0", END)
        global isFileSaved
        TextEditor.isFileSaved = False
        TextEditor.CurrentOpenFile = "null"
    def Save():
        if TextEditor.CurrentOpenFile == "null":
            TextEditor.SaveAs()
            TextEditor.isFileSaved = True
        else:
            f = open(TextEditor.CurrentOpenFile, "w")
            f.write(textbox.get("1.0", "end"))
            f.close()
    def SaveAs():
        files = [('All Files', '*.*'), 
                ('Python Files', '*.py'),
                ('Text Document', '*.txt')]
        file = asksaveasfile(filetypes = files, defaultextension = ".py")
        textboxcontent = textbox.get("1.0", "end")
        if file:
            with open(file.name, "w") as f:
                f.write(textboxcontent)
                CurrentOpenFile = filename
                root.title("Current Open File - VCM's Editor")



TextEditor.Main()