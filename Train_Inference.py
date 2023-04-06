from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics, model_selection, svm
from sklearn.metrics import confusion_matrix

import seaborn as sns
sns.set(style='dark', color_codes=True)


class Ui_Train_Inference(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font1 = QtGui.QFont()
        font1.setPointSize(18)

        font2 = QtGui.QFont()
        font2.setPointSize(12)

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(165, 10, 500, 81))
        self.label1.setFont(font1)
        self.label1.setObjectName("label1")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(100, 300, 650, 81))
        self.label2.setFont(font2)
        self.label2.setObjectName("label2")

        self.label2_5 = QtWidgets.QLabel(self.centralwidget)
        self.label2_5.setGeometry(QtCore.QRect(100, 70, 650, 81))
        self.label2_5.setFont(font2)
        self.label2_5.setObjectName("label3")

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(500, 605, 500, 81))
        self.label3.setFont(font2)
        self.label3.setObjectName("label3")

        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(100, 605, 500, 81))
        self.label4.setFont(font2)
        self.label4.setObjectName("label4")


# This button is for training
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 500, 200, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setFont(font2)
        self.pushButton_4.clicked.connect(self.trainer)

        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(230, 400, 50, 31))
        self.lineEdit1.setFont(font1)
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit1.textEdited['QString'].connect(self.label1.update)

        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(330, 400, 50, 31))
        self.lineEdit2.setFont(font1)
        self.lineEdit2.setObjectName("lineEdit1")

        self.lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit3.setGeometry(QtCore.QRect(430, 400, 50, 31))
        self.lineEdit3.setFont(font1)
        self.lineEdit3.setObjectName("lineEdit2")

        self.lineEdit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit4.setGeometry(QtCore.QRect(530, 400, 50, 31))
        self.lineEdit4.setFont(font1)
        self.lineEdit4.setObjectName("lineEdit3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def trainer(self):
        iris = "Iris2.csv"
        names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'type']
        df = pd.read_csv(iris, names=names)
        print(df.head())
        mysvm_model = svm.SVC(max_iter=1000)
        y = df.values[:, 4]
        X = df.values[:, 0:4]
        X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.33)
        mysvm_model.fit(X_train, y_train)
        y_pred_svm = mysvm_model.predict(X_test)

        # Convert accuracy score to percentage
        acc = 100*(metrics.accuracy_score(y_test, y_pred_svm))
        accStr = str(acc)
        self.label3.setText("Accuracy Score: " + accStr + "%")
        print(acc)

        xlabels = ["Iris-Setosa", "Iris-Versicolor", "Iris-Virginica"]
        ylabels = ["Iris-Setosa", "Iris-Versicolor", "Iris-Virginica"]
        cm = confusion_matrix(y_test, y_pred_svm, labels=mysvm_model.classes_)
        sns.heatmap(cm, cmap="Greys", annot=True, xticklabels=xlabels,yticklabels=ylabels)
        plt.title("Species Predictions Confusion Matrix")
        plt.show()
        num1 = self.lineEdit1.text()
        num2 = self.lineEdit2.text()
        num3 = self.lineEdit3.text()
        num4 = self.lineEdit4.text()
        try:
            value = (num1 + ' '+ num2 + ' '+ num3 + ' ' + num4)
            valueList = list(value.split(" "))
            print(mysvm_model.predict([valueList]))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error! Application will restart \nand you will need to \nfill out all values with numbers.")
            msg.setInformativeText("The model cannot predict accurately otherwise.")
            msg.setWindowTitle("Error")
            msg.exec_()
            pass
        self.label4.setText("Predicted Species: " + str(mysvm_model.predict([valueList])))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Training and Inference"))
        self.label1.setText(_translate("MainWindow", "Welcome to the training and inference page!"))
        self.label2.setText(_translate("MainWindow", "SVM Algorithm will be trained using 33% of the dataset using a randomly selected set.\nThe algorithm is retrained every time you push the button."))
        self.label2_5.setText(_translate("MainWindow", "In this window, you will train the SVM algorithm using a randomly selected portion of\nthe Iris dataset. Which you will then use the measurements you have taken from the Iris\nthat you currently have and put those in following boxes. The algorithm will make a \nprediction based off of the measurements you have given it with an accuracy score."))
        self.label3.setText(_translate("MainWindow", "Accuracy Score: "))
        self.label4.setText(_translate("MainWindow", "Predicted Species: "))
        self.pushButton_4.setText(_translate("MainWindow", "Make Prediction"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Train_Inference()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
#test commit