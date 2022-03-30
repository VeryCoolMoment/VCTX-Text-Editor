import os
class ErrorHandler:
    def WriteToLog(text):
        if os.path.exists("log.txt") == False:
            f = open("log.txt", "x")
        else:
            f = open("log.txt", "a")
        
        f.write(text + "\n")
        f.close()


