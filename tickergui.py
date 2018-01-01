# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tickergui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from tickerdata import currency
from PyQt5 import QtCore, QtGui, QtWidgets\


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
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
        for x in range(10):
            item = self.tableWidget.item(x, 3)
            item.setText(_translate("MainWindow", "$"+currency[x].price_usd))
        for x in range(10):
            item = self.tableWidget.item(x, 4)
            item.setText(_translate("MainWindow", currency[x].percent_change_1h))
        for x in range(10):
            item = self.tableWidget.item(x, 5)
            item.setText(_translate("MainWindow", currency[x].percent_change_24h))


        self.menuTicker.setTitle(_translate("MainWindow", "Ticker"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
