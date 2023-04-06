from PyQt5 import QtCore, QtGui, QtWidgets
import csv
from PyQt5.QtWidgets import QMessageBox
import seaborn as sns
sns.set(style='dark', color_codes=True)
from Train_Inference import Ui_Train_Inference
from Scatter import Ui_Scatter_MainWindow


class Ui_MainWindow_Main(QtWidgets.QWidget):

    def __init__(self, fileName, parent=None):
        super(Ui_MainWindow_Main, self).__init__(parent)
        self.fileNameEmployee = "Iris.csv"
        self.model = QtGui.QStandardItemModel(self)

        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setFixedSize(675, 600)

        self.load_employee_data_button = QtWidgets.QPushButton(self)
        self.load_employee_data_button.setText("Click here to view the Iris dataset")
        try:
            self.load_employee_data_button.clicked.connect(self.on_pushButtonLoad_clicked_iris_dataset)
        except EnvironmentError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error! Please close existing window.")
            msg.setInformativeText('You can only have one window open at a time. Please close the existing window to continue!')
            msg.setWindowTitle("Error")
            msg.exec_()
            pass

        self.trainingWindow = QtWidgets.QPushButton(self)
        self.trainingWindow.setText("Go to the training and inference page")
        self.trainingWindow.clicked.connect(self.inference_page_show)

# Should be the interactive scatter plot
        self.irisScatterPlot = QtWidgets.QPushButton(self)
        self.irisScatterPlot.setText("Go to scatter plot setup page for Iris comparisons")
        self.irisScatterPlot.clicked.connect(self.scatter_plot_setup_page_show)

        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(20)

        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.tableView)
        self.layoutVertical.addWidget(self.load_employee_data_button)
        self.layoutVertical.addWidget(self.trainingWindow)
        self.layoutVertical.addWidget(self.irisScatterPlot)
        self.layoutVertical.addSpacing(220)
        self.welcomeLabel = QtWidgets.QLabel(self)
        self.welcomeLabel.setGeometry(QtCore.QRect(125, 735, 500, 50))
        self.navigationLabel = QtWidgets.QLabel(self)
        self.navigationLabel.setGeometry(QtCore.QRect(100, 800, 700, 30))
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setText("Welcome to the Iris Prediction Engine!")
        self.navigationLabel.setFont(font)
        self.navigationLabel.setText("To begin, please view dataset and proceed.")

    def loadCsv(self, fileName):
        self.model.clear()
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

    @QtCore.pyqtSlot()
    def on_pushButtonLoad_clicked_iris_dataset(self):
        self.loadCsv(self.fileNameEmployee)

    def scatter_plot_setup_page_show(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Scatter_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def inference_page_show(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Train_Inference()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('Iris Prediction Engine')

    main = Ui_MainWindow_Main("data.csv")
    main.show()

    sys.exit(app.exec_())
