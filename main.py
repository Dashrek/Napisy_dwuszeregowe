class napis:
    def __init__(self,numer):
        self.numer=numer
        self.lines=[]
    def add_time(self,time):
        self.time=time
    def add_line(self,line):
        self.lines.append(line)
class napisy:
    def __init__(self,file,kolor):
        self.klasy=[]
        self.kolor=kolor
        nr_napisu=1
        znacznik_czasu=False
        for i in file:
            if i.split("\n")[0]==str(nr_napisu):
                self.klasy.append(napis(i.split("\n")[0]))
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
            print(i.numer)
            print(i.time)
            print("<font color=\""+self.kolor+"\">")
            for j in i.lines:
                print("{\\an8}"+j)
            print("</font>")
            print("")
f=open("Obi-Wan Kenobi - S1E2.srt","r",encoding="UTF-8")
t=napisy(f.readlines(),"#ffbf1f")
t.zapis()
