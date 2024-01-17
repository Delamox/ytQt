from PyQt6 import QtCore, QtGui, QtWidgets
from PIL import Image
import requests
from io import BytesIO
import tempfile
from pathlib import Path


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(640, 880)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color: #2a2a2a;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.thumbnail = QtWidgets.QLabel(parent=self.centralwidget)
        self.thumbnail.setGeometry(QtCore.QRect(10, 60, 256, 144))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thumbnail.sizePolicy().hasHeightForWidth())
        self.thumbnail.setSizePolicy(sizePolicy)
        self.thumbnail.setToolTip("")



        temp = tempfile.TemporaryFile()
        Image.open(BytesIO(requests.get("https://files.catbox.moe/qe6gc6.jpg").content)).save(f"{temp.name}.bmp")

        self.thumbnail.setStyleSheet(f"color: rgb(0, 0, 0);\n"
                                     f"border: 1px solid black;\n"
                                     f"border-radius: 25px;\n"
                                     f"border-color: white;\n"
                                     f"width: 144px;\n"
                                     f"height: 256px;\n"
                                     f"border-image: url({Path(f'{temp.name}.bmp').as_posix()}) 0 0 0 0 stretch stretch;")


        print(f"border-image: url({Path(f'{temp.name}.bmp').as_posix()}) 0 0 0 0 stretch stretch;")
        self.thumbnail.setText("")



        self.thumbnail.setScaledContents(True)
        self.thumbnail.setOpenExternalLinks(False)
        self.thumbnail.setObjectName("thumbnail")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setGeometry(QtCore.QRect(280, 60, 350, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setToolTip("")
        self.title.setStyleSheet("color: rgb(255, 255, 255);")
        self.title.setText("Marisad.jpg")
        self.title.setWordWrap(True)
        self.title.setObjectName("title")
        self.user = QtWidgets.QLabel(parent=self.centralwidget)
        self.user.setGeometry(QtCore.QRect(280, 100, 350, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.user.setFont(font)
        self.user.setToolTip("")
        self.user.setStyleSheet("color: #c0c0c0;")
        self.user.setText("2hu")
        self.user.setObjectName("user")
        self.meta = QtWidgets.QLabel(parent=self.centralwidget)
        self.meta.setGeometry(QtCore.QRect(280, 140, 350, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.meta.setFont(font)
        self.meta.setToolTip("")
        self.meta.setStyleSheet("color: #c0c0c0;")
        self.meta.setLineWidth(1)
        self.meta.setText("420K views / 69 weeks ago")
        self.meta.setObjectName("meta")
        self.previous = QtWidgets.QPushButton(parent=self.centralwidget)
        self.previous.setGeometry(QtCore.QRect(10, 830, 130, 40))
        self.previous.setToolTip("")
        self.previous.setStyleSheet("QPushButton {\n"
                                    "    color: #000000;\n"
                                    "    background-color: #74cbfc;\n"
                                    "    border: 1px solid black;\n"
                                    "    border-radius: 20px;\n"
                                    "    border-color: #74cbfc;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    border-radius: 5px;\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "}\n"
                                    "")
        self.previous.setText("previous")
        self.previous.setObjectName("previous")
        self.next = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next.setGeometry(QtCore.QRect(150, 830, 140, 40))
        self.next.setToolTip("")
        self.next.setStyleSheet("QPushButton {\n"
                                "    color: #000000;\n"
                                "    background-color: #74cbfc;\n"
                                "    border: 1px solid black;\n"
                                "    border-radius: 20px;\n"
                                "    border-color: #74cbfc;\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "    border-radius: 5px;\n"
                                "}\n"
                                "QPushButton:pressed {\n"
                                "}\n"
                                "")
        self.next.setText("next")
        self.next.setObjectName("next")
        self.searchbar = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.searchbar.setGeometry(QtCore.QRect(10, 10, 620, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchbar.setFont(font)
        self.searchbar.setToolTip("The searchbar dumbass.")
        self.searchbar.setToolTipDuration(-1)
        self.searchbar.setWhatsThis("")
        self.searchbar.setStyleSheet("QLineEdit {\n"
                                     "    color: #a8a8a8;\n"
                                     "    background-color: #4d4d4d;\n"
                                     "    border: 2px solid #36393e;\n"
                                     "    border-radius: 20px;\n"
                                     "    padding-right: 20px;\n"
                                     "    padding-left: 20px;\n"
                                     "}\n"
                                     "QLineEdit:hover {\n"
                                     "    border: 2px solid #74cbfc;\n"
                                     "}\n"
                                     "QLineEdit:focus {\n"
                                     "    border-radius: 5px;\n"
                                     "    border: 2px solid #74cbfc;\n"
                                     "}")
        self.searchbar.setInputMask("")
        self.searchbar.setText("")
        self.searchbar.setClearButtonEnabled(True)
        self.searchbar.setObjectName("searchbar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchbar.setPlaceholderText(_translate("MainWindow", "Search YouTube..."))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
