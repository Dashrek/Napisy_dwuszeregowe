class napis:
    def __init__(self,numer,typ,kolor):
        self.numer=numer
        self.kolor=kolor
        self.lines=[]
        self.typ=typ
    def add_time(self,time):
        self.time=time
    def add_line(self,line):
        self.lines.append(line)
    def __lt__(self,other):
        kla=lambda a:"".join([(i if i!="," else ".")for i in a])
        t=self.time.split("-->")[0].split(":")
        t=float(kla(t[2]))+int(t[1])*60+int(t[0])*3600
        t1 = other.time.split("-->")[0].split(":")

        t1 = float(kla(t1[2])) + int(t1[1]) * 60 + int(t1[0]) * 3600
        return t<t1
    def __str__(self):
        return str(self.numer)+"\n"+str(self.time)+"\n"+"<font color=\""+self.kolor+"\">"+"\n"+str(("{\\an2}" if self.typ=="pl" else "{\\an8}"))+("\n"+str(("{\\an2}" if self.typ=="pl" else "{\\an8}"))).join(self.lines)+"\n</font>\n"
class napisy:
    def __init__(self,file,kolor,typ):
        self.klasy=[]
        self.kolor=kolor
        nr_napisu=1
        znacznik_czasu=False
        for i in file:
            if i.split("\n")[0]==str(nr_napisu):
                self.klasy.append(napis(i.split("\n")[0],typ,self.kolor))
                nr_napisu+=1
                znacznik_czasu=True
                continue
            elif znacznik_czasu==True:
                znacznik_czasu=False
                self.klasy[-1].add_time(i.split("\n")[0])
                continue
            elif i!="\n":
                self.klasy[-1].add_line(i.split("\n")[0])
                continue
    def zapis(self):
        for i in self.klasy:
            print(i)
f=open("Obi-Wan Kenobi - S1E2.srt","r",encoding="UTF-8")
f1=open("Obi-Wan.Kenobi.S01E02.srt","r",encoding="UTF-8")
t=napisy(f.readlines(),"#ffbf1f","ger")
t1=napisy(f1.readlines(),"#ff7200","pl")

class listas:
    def __init__(self,lista,lista1):
        self.lista=[]
        self.dl=0
        for i in lista:
            self.add(i)
        for i in lista1:
            self.add(i)
    def add(self,x):
        lewy=0
        prawy=self.dl

        while(lewy<prawy):
            sr = (lewy + prawy) // 2
            if self.lista[sr]<x:
                lewy=sr+1
            else:
                prawy=sr
        self.lista.insert(lewy,x)
        self.dl+=1
    def wypisz(self):
        for count,i in enumerate(self.lista):
            i.numer=count+1
            print(i)
listas(t.klasy,t1.klasy).wypisz()
f.close()
f1.close()