from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication


def verif(ch):
    test = True
    for i in range(len(ch)):
        if not ("A"<=ch[i]<="Z" or ch[i]==" "):
            test =False
    return test and ch.find(" ")!=-1 and ch[i]!=" "


def coco(ch):
    ch=ch+" "
    test =True
    x= ch[0]
    ch= ch[(ch.find(" "))+1:]
    while test and ch!="":
        p= ch.find(" ")
        mot=ch[:p]
        test= mot.find(x)!=-1
        ch=ch[p+1:]
    return test

def trait():
    ch= windows.nl.text()
    if verif(ch) :
        if coco(ch):
            msg= ch+ " : is a Cocogram"
        else:
            msg= ch+ " : is not a Cocogram "
    else:
        msg= "Error ! "    
    windows.res.setText(msg)
    
def delete():
    windows.res.clear()
    windows.nl.clear()
    
def close():
    windows.close()

app = QApplication([])
windows= loadUi("cocogram.ui")
windows.show()
windows.bv.clicked.connect(trait)
windows.be.clicked.connect(delete)
windows.bf.clicked.connect(close)
app.exec_()
        