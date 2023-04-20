import sys
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtGui import QColor
from PyQt5 import uic
import threading
import can

from circularprogressbar import QRoundProgressBar
import sys

import threading , random
from time import sleep

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('Round.ui',self)

        self.ui.pushBtnStart.clicked.connect(self.startDataTake)
        self.ui.pushBtnStop.clicked.connect(self.stopDataTake)


        self.bar1 = QRoundProgressBar()
        self.bar1.setFixedSize(400, 400)
        self.bar1.setDataPenWidth(3)
        self.bar1.setOutlinePenWidth(3)
        self.bar1.setDonutThicknessRatio(0.85)
        self.bar1.setDecimals(1)
        self.bar1.setFormat('%v | %p %')
        self.bar1.setNullPosition(90)
        self.bar1.setBarStyle(QRoundProgressBar.StyleDonut)
        self.bar1.setDataColors([(0., QColor.fromRgb(0,255,0)), (0.5, QColor.fromRgb(255,255,0)), (1., QColor.fromRgb(255,0,0))])

        self.bar1.setRange(0, 200)
        self.bar1.setValue(200)
        self.horizontalLayout.addWidget(self.bar1)

        self.bar2 = QRoundProgressBar()
        self.bar2.setFixedSize(400, 400)
        self.bar2.setDataPenWidth(3)
        self.bar2.setOutlinePenWidth(3)
        self.bar2.setDonutThicknessRatio(0.85)
        self.bar2.setDecimals(1)
        self.bar2.setFormat('%v | %p %')
        self.bar2.setNullPosition(90)
        self.bar2.setBarStyle(QRoundProgressBar.StylePie)
        self.bar2.setDataColors([(0., QColor.fromRgb(0,255,0)), (0.5, QColor.fromRgb(255,255,0)), (1., QColor.fromRgb(255,0,0))])

        self.bar2.setRange(0, 200)
        self.bar2.setValue(200)
        self.horizontalLayout_2.addWidget(self.bar2)

        self.isRun = False

        self.val1 = random.randint(0,200)
        self.val2 = random.randint(0,200)

        self.UINT1 = 0
        self.U1for = 0
        self.UINT2 = 0
        self.U2for = 0
    def startDataTake(self):
        self.isRun = True
        for t in threading.enumerate():
            if t.name == "_gen_":
                print("already running")
                return
        threading.Thread(target=self.backgroundThread, name="_gen_").start()
        print("clicked Start")

    def stopDataTake(self):
        self.isRun = False
        for t in threading.enumerate():
            if t is self.backgroundThread:
                t.join()
        print("Clicked Stop")

    def backgroundThread(self):
        while(self.isRun):
            self.UINT1 = random.randint(0,200)
            self.UINT2 = random.randint(0,200)
            sleep(0.1)
            if self.UINT1 > self.U1for:
                self.val1 = self.UINT1
                self.U1for = self.UINT1
                self.bar1.setValue(self.U1for)
            else:
                if self.U1for > 10:
                    self.U1for-=10
                else:
                    self.U1for = 0
                self.bar1.setValue(self.U1for)

            if self.UINT2 > self.U2for:
                self.val2 = self.UINT2
                self.U2for = self.UINT2
                self.bar2.setValue(self.U2for)
            else:
                if self.U2for > 10:
                    self.U2for-=10
                else:
                    self.U2for = 0
                self.bar2.setValue(self.U2for)
        
        



