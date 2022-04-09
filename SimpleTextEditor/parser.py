class Parser:
    def LoadResource(line):
        f = open("en_vctx.txt", "r")
        for l in f:
            if l.startswith(line):
                if l.strip(line + "= ")[0:-1].startswith("\"") and l.strip(line + "= ")[0:-1].endswith("\""):
                    string = l.strip(line + "= ")[1:-1]
                    string = string.rstrip(string[-1])
                    return string
                else:
                    return line 
