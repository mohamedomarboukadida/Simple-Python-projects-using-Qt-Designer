from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def sum(k):
    s= 0
    while k>1:
        s+= k%10
        k= k//10
    return s

def verif():
    k = windows.nbr.text()
    if k.isdigit() and int(k)>1:
        if int(k)% sum(int(k)) ==0 :
            windows.res.setText(k+ "is number Harshads")
        else:
            windows.res.setText(k+ "is not a Harshads number")
    else:
        windows.res.setText( "Type a number >1")

def close():
    windows.close()
def delete():
    windows.res.clear()
    windows.nbr.clear()
    
    
app = QApplication([])
windows= loadUi("harshad.ui")
windows.show()
windows.bv.clicked.connect(verif)
windows.be.clicked.connect(delete)
windows.bf.clicked.connect(close)