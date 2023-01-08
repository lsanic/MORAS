def _parse_macros(self):
    self._iter_macros(self._parse_macro)

def _parse_macro(self, line, p, o):
    if line[0] != "$": #ne radi se o naredbi(jer one pocinju znakom $) pa samo vrati line
        return line
    else:
        macro = line[1:].split("(")[0] # dohvati nasu macro naredbu 
        if(len(macro)!=1): # proslijedeni su arg sto znaci da se ne radi o end naredbi
           argumenti = macro[:-1]
           a = argumenti.split(",") # podijelimo svoje argumente po el koje kasnije dohvacamo kao A, B i D preko indeksa
           A = a[0]
           B = a[1]
           D = a[2]
        else:
            argumenti = []
       
    # a) 
    if macro == "$MV":
        return ["@" + A, "D=M", "@" + B, "M=D"] 
    # izgleda ovako:
    # @A
    # D = M   
    # @B
    # M = D 
    
    #b)
    # swapa sadrzaj A i B 
    elif macro == "$SWP":
        return ["@" + A, "D=M", "@temp", "M=D", "@" + B, "D=M", "@" + A,"M=D","@temp", "D=M" , "@" + B, "M=D"]
    
    # c) sumu A i B sprema u D
    elif macro == "$SUM":
        return ["@" + A, "D=M", "@" + B,"D=M+D", "@" + D, "M = D"]
    

    else:  # u slucaju da je uneseno nesto sto ne prepoznajemo
        self._flag = False
        self.line = o
        self._errm = "Nije unesena valjana macro naredba."
        return ""