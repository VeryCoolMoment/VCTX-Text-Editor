import os
from tkinter import messagebox
class ErrorHandler:
    def WriteToLog(text):
        if os.path.exists("log.txt") == False:
            f = open("log.txt", "x")
        else:
            f = open("log.txt", "a")
        
        f.write(text + "\n")
        f.close()
    def DisplayError(errortitle,errortext,shouldwritetolog):
        messagebox.showerror(errortitle, errortext)
        if shouldwritetolog == True:
            ErrorHandler.WriteToLog("ERROR: " + errortext)


