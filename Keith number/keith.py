from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import *
T= array([0]*10)

def keith(k):
    ch= str(k)
    n= len(ch)
    for i in range(n):
        T[i]=int(ch[i])
    s=0
    while s<int(k):
        s=0
        for i in range(n):
            s = s+T[i]
        for i in range(n-1):
            T[i]= T[i+1]
        T[n-1]= s
    return s==k

def verif():
    k= windows.nbr.text()
    if k.isdigit() :
        if keith(k):
            windows.res.setText("The number "+str(k)+ " is a Keith number")
        else:
            windows.res.setText("The number"+str(k)+ " is not a Keith number")
    else :
        windows.res.setText("Verify your number")
        
def close():
    windows.close()
def delete():
    windows.res.clear()
    windows.nbr.clear()
   
    
app = QApplication([])
windows= loadUi("keith.ui")
windows.show()
windows.bv.clicked.connect(verif)
windows.be.clicked.connect(delete)
windows.bf.clicked.connect(close)
app.exec_()

