import time
class Frase:
    def __init__(self,author,frase,desc,id_member,date):
        self.author = author
        self.frase = frase
        self.desc = desc
        self.id = id_member
        self.date = date
    # Set
    def setAuthor(self):
        self.author
    def setFrase(self):
        self.frase
    def setDesc(self):
        self.desc
    def setDate(self):
        self.date
    def setID(self):
        self.id

    #Get
    def getAuthor(self):
        return self.author
    def getFrase(self):
        return self.frase
    def getDesc(self):
        return self.desc
    def getDate(self):
        return self.date
    def getID(self):
        return self.id