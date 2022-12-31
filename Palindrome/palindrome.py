from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def verif(ch):
    test= True
    i=0
    for i in range(len(ch)):
        if not("a"<=ch[i]<="z" ):
            test=False
    return test

def palaind(ch):
    l=len(ch)
    i=0
    while (i<l//2) and ch[i]==ch[l-i-1]:
        i=i+1
    return i>=l//2

def palindrome():
    ch= windows.chn.text()
    if verif(ch) and (1<len(ch)<=30):
        msg=""
        for i in range(len(ch)-1):
            for j in range(i+1,len(ch)):
                if palaind(ch[i:j+1]):
                    msg = msg+ ch[i:j+1]+" | "
                    
    else:
        msg="Error!"
        
    windows.res.setText(msg)
        
def close():
    windows.close()
def delete():
    windows.res.clear()
    windows.chn.clear()


app = QApplication([])
windows= loadUi("palindrome.ui")
windows.show()
windows.bv.clicked.connect(palindrome)
windows.be.clicked.connect(delete)
windows.bf.clicked.connect(close)
app.exec_()


    
