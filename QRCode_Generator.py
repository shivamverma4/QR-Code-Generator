import pyqrcode

st=""
def qrcode():
    q=pyqrcode.create(st)
    q.png('myQR.png',scale=6)
    print('QR Code Generated..')

if __name__=='__main__':
    st=input()
    qrcode()
