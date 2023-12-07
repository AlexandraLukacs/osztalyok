import datetime
class Szemely:
    def __init__(self,nev:str,szuldatum:int,szszam:int):
        self.nev=nev
        self.szuldatum=szuldatum
        self.szszam=szszam

    def kor(self):
        """ tagfüggvény, osztálymetódus
        Az osztály adttagjai végeznek műveleteket"""
        x = datetime.datetime.now()
        return x.year-self.szuldatum