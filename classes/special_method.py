class Film:
    def __init__(self,title,duration,year):
        self.title = title
        self.duration = duration
        self.year = year
    def __str__(self):
        return self.title
    

p = Film("El Padrino",175,1985)        

print(str(p))        