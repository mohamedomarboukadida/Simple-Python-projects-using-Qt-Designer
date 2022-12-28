from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def prime(k):
    test =True
    for i in range(2,k):
        if k%i==0:
            test = False
    return test

def mersenne(k):
    m= k+1
    n=0
    while m%2==0:
        n=n+1
        m=m//2
    return prime(n) and m==1

def verif():
    k= windows.nbr.text()
    if k.isdigit():
        k= int(k)
        if mersenne(k):
            msg=str(k)+ " : is a Mersenne number"
        else:
            msg=str(k)+ " : is not a Mersenne number"
    else:
        msg=" Error!"
    windows.res.setText(msg)


def close():
    windows.close()
def delete():
    windows.res.clear()
    windows.nbr.clear()


    
app = QApplication([])
windows= loadUi("mersenne.ui")
windows.show()
windows.bv.clicked.connect(verif)
windows.be.clicked.connect(delete)
windows.bf.clicked.connect(close)
app.exec_()
