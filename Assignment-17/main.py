import math
from functools import partial
from re import A
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

# functions
first_num = 0
memory = 0
opr = ''

def show_result(num):
    window.temp.setText(num)

def setNum(nums):
    c = window.temp.text()
    if c == "0":
        window.temp.setText(nums)
    else:
        window.temp.setText(window.temp.text() + nums)

def opr_(operator):
    global first_num,opr
    first_num = window.temp.text()
    opr = operator
    window.temp.setText("")

def equal():
    global first_num,opr
    b = window.temp.text()
    match opr:
        case '+':
            c = round(float(first_num) + float(b),10)
        case '-':
            c = round(float(first_num) - float(b),10)
        case '*':
            c = round(float(first_num) * float(b),10)
        case '/':
            c = round(float(first_num) / float(b),10)
    
    window.temp.setText(str(c))

def clean():
    global first_num 
    first_num = ''
    window.temp.setText('')

def MR():
    global memory 
    window.label.setText('')
    window.temp.setText(str(memory))
    memory = ''

def MP():
    global memory
    memory += float(window.temp.text())
    window.label.setText('M = ' + str(memory))
    window.temp.setText('')

def MM():
    global memory
    memory -= float(window.temp.text())
    window.label.setText('M = ' + str(memory))
    window.temp.setText('')

def triangle_(func):
    temp = int(window.temp.text())
    x = 0
    match (func):
        case 'sin':
            x = math.sin(math.radians(temp))
        case 'cos':
            x = math.cos(math.radians(temp))
        case 'tan':
            x = math.tan(math.radians(temp))
        case 'cot':
            x = 1 / math.tan(math.radians(temp))
        case 'log':
            x = math.log10(temp)
    
    window.temp.setText(str(x))

def rond():
    c = float(window.temp.text())
    x = round(c, 10)
    window.temp.setText(str(x))

def sqrt():
    x = float(window.temp.text())
    window.temp.setText(str(math.sqrt(x)))

# Load and Execute program
loader = QUiLoader()
app = QApplication([])
window = loader.load("ui.ui")

window.b1.clicked.connect(partial(setNum, "1"))
window.b2.clicked.connect(partial(setNum, "2"))
window.b3.clicked.connect(partial(setNum, "3"))
window.b4.clicked.connect(partial(setNum, "4"))
window.b5.clicked.connect(partial(setNum, "5"))
window.b6.clicked.connect(partial(setNum, "6"))
window.b7.clicked.connect(partial(setNum, "7"))
window.b8.clicked.connect(partial(setNum, "8"))
window.b9.clicked.connect(partial(setNum, "9"))
window.point.clicked.connect(partial(setNum, "."))
window.z.clicked.connect(partial(setNum, "0"))
window.zz.clicked.connect(partial(setNum, "00"))

window.plus.clicked.connect(partial(opr_,'+'))
window.neg.clicked.connect(partial(opr_,'-'))
window.mul.clicked.connect(partial(opr_,'*'))
window.div.clicked.connect(partial(opr_,'/'))

window.equal.clicked.connect(equal)
window.sqrt.clicked.connect(sqrt)

window.MP.clicked.connect(MP)
window.MM.clicked.connect(MM)
window.MR.clicked.connect(MR)

window.sin.clicked.connect(partial(triangle_,'sin'))
window.cos.clicked.connect(partial(triangle_,'cos'))
window.tan.clicked.connect(partial(triangle_,'tan'))
window.cot.clicked.connect(partial(triangle_,'cot'))
window.log.clicked.connect(partial(triangle_,'log'))

window.c.clicked.connect(clean)
window.round.clicked.connect(rond)
window.show()

app.exec()
