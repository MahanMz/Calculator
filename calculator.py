
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget
from PyQt5 import uic, QtCore

class Calculator(QMainWindow):

    def __init__(self):
        super().__init__()
        dock = QDockWidget(self)
        uic.loadUi("calculator.ui", self)
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        self.tmpNums = []
        self.finNums = []

        self.btnExit.clicked.connect(self.close)
        self.btnMaximize.clicked.connect(self.showMaximized)
        self.btnMinimize.clicked.connect(self.showMinimized)

        self.btn0.clicked.connect(lambda: self.numPress("0"))
        self.btn1.clicked.connect(lambda: self.numPress("1"))
        self.btn2.clicked.connect(lambda: self.numPress("2"))
        self.btn3.clicked.connect(lambda: self.numPress("3"))
        self.btn4.clicked.connect(lambda: self.numPress("4"))
        self.btn5.clicked.connect(lambda: self.numPress("5"))
        self.btn6.clicked.connect(lambda: self.numPress("6"))
        self.btn7.clicked.connect(lambda: self.numPress("7"))
        self.btn8.clicked.connect(lambda: self.numPress("8"))
        self.btn9.clicked.connect(lambda: self.numPress("9"))
        
        self.btnClear.clicked.connect(self.clsCalc)
        self.btnPlus.clicked.connect(lambda: self.funcPress("+"))
        self.btnMinus.clicked.connect(lambda: self.funcPress("-"))
        self.btnEqual.clicked.connect(self.funcRsult)
        self.btnMultipliedBy.clicked.connect(lambda: self.funcPress("*"))
        self.btnDivision.clicked.connect(lambda: self.funcPress("/"))

        
        self.show()
    def numPress(self, number):
        self.tmpNums.append(number)
        tmpStr = "".join(self.tmpNums)
        if self.finNums:
            self.result.setText(''.join(self.finNums) + tmpStr)
        else:
            self.result.setText(tmpStr)

    def funcPress(self, operator):
        tmpStr = ''.join(self.tmpNums)
        self.finNums.append(tmpStr)
        self.finNums.append(operator)
        self.tmpNums = []
        self.result.setText(''.join(self.finNums))
    
    def funcRsult(self):
        finStr = ''.join(self.finNums) + ''.join(self.tmpNums)
        rsultStr = eval(finStr)
        finStr += '='
        finStr += str(rsultStr)
        self.result.setText(finStr)

    def clsCalc(self):
        self.result.clear()
        self.tmpNums = []
        self.finNums = []
    def resizeEvent(self, QResizeEvent):
        super(Calculator, self).resizeEvent(QResizeEvent)
        self.titleBar.setFixedWidth(self.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.width(),
                                self.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False
app = QApplication([])
win = Calculator()
app.exec_()
