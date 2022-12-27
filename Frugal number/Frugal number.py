from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication


def frugal(k):
    l = len(str(k))
    f=2
    nc=0
    while k!=0:
        nb=0
        while k%f==0 :
            nb+=1
            k=k//f
        if nb ==1 :
            nc+=1
        elif nb>1:
            nc+=2
        f+=1
    return l>nc

def verif():
    k= windows.nbr.text()
    if k.isdigit() and int(k)>100 :
        k= int(k)
        if frugal(k):
            windows.res.setText(str(k)+ " Is Frugal")
        else:
            windows.res.setText(str(k)+ " Is not Frugal")
    else:
        windows.res.setText(" Type an integer >=100 ")

def effacer():
    windows.res.clear()
    windows.nbr.clear()
    
def fermer():
    windows.close()

app = QApplication([])
windows = loadUi("frugal.ui")
windows.show()
windows.bv.clicked.connect(verif)
windows.bf.clicked.connect(fermer)
windows.be.clicked.connect(effacer)
