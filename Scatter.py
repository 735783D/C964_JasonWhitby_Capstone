from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(style='dark', color_codes=True)


class Ui_Scatter_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setGeometry(QtCore.QRect(210, 90, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox_1.setFont(font)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(410, 90, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 601, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 230, 551, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 34))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Adding items to the boxes
        self.comboBox_1.addItem("sepal-length", ["sepal-width", "petal-length", "petal-width"])
        self.comboBox_1.addItem("sepal-width", ["sepal-length", "petal-length", "petal-width"])
        self.comboBox_1.addItem("petal-length", ["sepal-width", "sepal-length", "petal-width"])
        self.comboBox_1.addItem("petal-width", ["sepal-length", "petal-length", "sepal-width"])

        # Clicking on the first dropdown
        self.comboBox_1.activated.connect(self.clicked_box)
        self.comboBox_2.activated.connect(self.button_click_update)

    def clicked_box(self, index):
        # Clearing the second box
        self.comboBox_2.clear()
        # Cause dependency
        self.comboBox_2.addItems(self.comboBox_1.itemData(index))

    def button_click_update(self):
        # Update the label
        a = self.comboBox_1.currentText()
        b = self.comboBox_2.currentText()
        url = "Iris2.csv"
        names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'type']
        df = pd.read_csv(url, names=names)
        sns.scatterplot(x=a, y=b, hue="type", data=df)
        plt.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scatterplot Comparisons"))
        self.label.setText(_translate("MainWindow", "Use dropdowns to make selections of which variables to plot. \nYou need to select something in the left box first."))
        self.label_2.setText(_translate("MainWindow", "The scatterplot is interactive. Click on it and drag it around to see everything."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Scatter_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

