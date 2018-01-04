# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tickergui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from tickerdata import refresh
from PyQt5 import QtCore, QtGui, QtWidgets\

currency = refresh()
count=0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MinimalistCryptoTracker v0.1")
        MainWindow.resize(790, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, -9, 801, 410))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        #helper function to create all columns
        def create_col(col_num):
            for x in range(10):
                item = QtWidgets.QTableWidgetItem() #need this 
                self.tableWidget.setItem(x,col_num,item)

        #create all columns to be filled in!
        def create_all_cols():
            for x in range(6):
                create_col(x)

        create_all_cols()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 26))
        self.menubar.setObjectName("menubar")
        self.menuTicker = QtWidgets.QMenu(self.menubar)
        self.menuTicker.setObjectName("menuTicker")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuTicker.addSeparator()
        self.menuTicker.addSeparator()
        self.menubar.addAction(self.menuTicker.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Rank"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Symbol"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price (USD)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "% Change (1H)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "% Change (24H)"))

        #functions for colorizing cell based on performance
        def colourizer_1h(x,y,data):
            if(float(data.percent_change_1h) > 0.00000):
                self.tableWidget.item(x, y).setBackground(QtGui.QColor(163, 255, 145))#paint green
            elif float(data.percent_change_1h) == 0.00000:
                return
            else:
                self.tableWidget.item(x, y).setBackground(QtGui.QColor(255, 104, 104))#paint red
        def colourizer_24h(x,y,data):
            if(float(data.percent_change_24h) > 0.00000):
                self.tableWidget.item(x, y).setBackground(QtGui.QColor(163, 255, 145))#paint green
            elif float(data.percent_change_24h) == 0.00000:
                return
            else:
                self.tableWidget.item(x, y).setBackground(QtGui.QColor(255, 104, 104))#paint red

        #namecolumn
        for x in range(10):
            item = self.tableWidget.item(x, 1)
            item.setText(_translate("MainWindow", currency[x].name))
        for x in range(10):
            item = self.tableWidget.item(x, 0)
            item.setText(_translate("MainWindow", currency[x].rank))
        for x in range(10):
            item = self.tableWidget.item(x, 2)
            item.setText(_translate("MainWindow", currency[x].symbol))
            self.tableWidget.item(x, 2).setBackground(QtGui.QColor(226, 250, 255))#paint blue
        for x in range(10):
            item = self.tableWidget.item(x, 3)
            item.setText(_translate("MainWindow", "$"+currency[x].price_usd))
        for x in range(10):
            item = self.tableWidget.item(x, 4)
            item.setText(_translate("MainWindow", currency[x].percent_change_1h))
            colourizer_1h(x,4,currency[x])
        for x in range(10):
            item = self.tableWidget.item(x, 5)
            item.setText(_translate("MainWindow", currency[x].percent_change_24h))
            colourizer_24h(x,5,currency[x])

        self.menuTicker.setTitle(_translate("MainWindow", "Ticker"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    def update_label():
        from tickerdata import refresh
        currency = refresh()
        for x in range(10):
            ui.tableWidget.item(x, 3).setText('$' + currency[x].price_usd)
        for x in range(10):
            ui.tableWidget.item(x, 4).setText(currency[x].percent_change_1h)
        for x in range(10):
            ui.tableWidget.item(x, 5).setText(currency[x].percent_change_24h)

    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.start(17000)  # every 10,000 milliseconds

    sys.exit(app.exec_())
