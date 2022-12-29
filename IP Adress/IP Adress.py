from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def conv_binary(n):
    ch= ""
    while n!=0:
        r= n%2
        n= n//2
        x= str(r)
        ch=x+ch
    return ch

def classe(ch):
    if (ch[0]) == "0":
        res= "A"
    elif (ch[0])== "1" and ch([1])=="0":
        res= "B" 
    elif (ch[0])== "1" and ch([1])=="1" and ch([2])=="0":
        res= "C"
    elif (ch[0])== "1" and ch([1])=="1" and ch([2])=="1" and ch([3]=="0") :
        res= "D"
    elif (ch[0])== "1" and ch([1])=="1" and ch([2])=="1" and ch([3]=="1") :
        res= "E"
    return res

def binary(ch):
    while len(ch)<8:
        ch = "0"+ ch
    return ch

def show():
    w= windows.w.text()
    x= windows.x.text()
    y= windows.y.text()
    z= windows.z.text()
    if x.isnumeric() and y.isnumeric() and w.isnumeric() and z.isnumeric() :
        x= int(x)
        y=int(y)
        z=int(z)
        w=int(w)
        if (0<=x<=255) and (0<=y<=255) and (0<=w<=255) and (0<=z<=255) :
            zx= binary(conv_binary(x))
            zy= binary(conv_binary(y))
            zw= binary(conv_binary(w))
            zz= binary(conv_binary(z))
            cl = classe(zw)
            resip= str(w)+"."+str(x)+"."+str(y)+"."+str(z)
            resb= str(zw)+"."+str(zx)+"."+str(zy)+"."+str(zz)
            resc= cl
        else:
            resip="Invalid address"
    else:
        resip="Invalid address"
    windows.resip.setText(resip)
    windows.resb.setText(resb)
    windows.resc.setText(resc)

def delete():
    windows.w.clear()
    windows.z.clear()
    windows.y.clear()
    windows.x.clear()
    windows.resip.clear()
    windows.resb.clear()
    windows.resc.clear()
    
def close():
    windows.close()

app = QApplication([])
windows= loadUi("ipadress.ui")
windows.show()
windows.be.clicked.connect(show)
windows.beff.clicked.connect(delete)
windows.bf.clicked.connect(close)
app.exec_()



