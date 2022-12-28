from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def verif(ch):
    i= 0
    while i<len(ch) and ("A"<=ch[i]<="Z" or ch[i]== " "):
        i = i+1
    return i ==len(ch)
    
def rotation13(ch):
    chc=""
    for i in range(len(ch)):
        if ch[i] == " ":
            chc = chc + " "
        elif "A"<=ch[i]<="M":
            chc= chc+ chr(ord(ch[i])+13)
        else:
            chc = chc+chr(ord(ch[i])-13)
    return chc
    
def cesar():
    ch = windows.chn.text()
    if len(ch) ==0 :
        msg = "You must enter a message"
    elif not verif(ch):
        msg = "the message must contain only capital letters and spaces"
    else:
        msg = rotation13(ch)
    windows.res.setText(msg)
        

def close():
    windows.close()
def delete():
    windows.res.clear()
    windows.chn.clear()


app = QApplication([])
windows= loadUi("cesar.ui")
windows.show()
windows.bc.clicked.connect(cesar)
windows.bdc.clicked.connect(cesar)
windows.be.clicked.connect(delete)
windows.bf.clicked.connect(close)
app.exec_()

