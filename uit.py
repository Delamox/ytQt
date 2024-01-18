from PyQt6 import QtCore, QtGui, QtWidgets
from PIL import Image
import requests
from io import BytesIO
import tempfile
from pathlib import Path
import os

class Ui_ytQt(object):
    def setupUi(self, ytQt):
        ytQt.setObjectName("ytQt")
        ytQt.setEnabled(True)
        ytQt.resize(1040, 880)
        ytQt.setWindowTitle("ytQt")
        ytQt.setWindowOpacity(1.0)
        ytQt.setStyleSheet("background-color: #2a2a2a;")
        self.centralwidget = QtWidgets.QWidget(parent=ytQt)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setGeometry(QtCore.QRect(280, 60, 750, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setToolTip(
            "This title is too long to be displayed properly on yt, look at tooltip! Hello tooltip user!")
        self.title.setStyleSheet("color: rgb(255, 255, 255);")
        self.title.setText(
            "This title is too long to be displayed properly on yt, look at tooltip... Hello tooltip user!")
        self.title.setScaledContents(False)
        self.title.setWordWrap(False)
        self.title.setObjectName("title")
        self.user = QtWidgets.QLabel(parent=self.centralwidget)
        self.user.setGeometry(QtCore.QRect(280, 100, 750, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.user.setFont(font)
        self.user.setToolTip("")
        self.user.setStyleSheet("color: #c0c0c0;")
        self.user.setText("Username")
        self.user.setObjectName("user")
        self.meta = QtWidgets.QLabel(parent=self.centralwidget)
        self.meta.setGeometry(QtCore.QRect(280, 140, 750, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.meta.setFont(font)
        self.meta.setToolTip("")
        self.meta.setStyleSheet("color: #c0c0c0;")
        self.meta.setLineWidth(1)
        self.meta.setText("K views /  weeks ago")
        self.meta.setObjectName("meta")
        self.previous = QtWidgets.QPushButton(parent=self.centralwidget)
        self.previous.setGeometry(QtCore.QRect(10, 830, 130, 40))
        self.previous.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.previous.setToolTip("")
        self.previous.setStyleSheet("QPushButton {\n"
                                    "color: #000000;\n"
                                    "background-color: #74cbfc;\n"
                                    "border-width: 1px;\n"
                                    "border-style: solid black;\n"
                                    "border-radius: 20px;\n"
                                    "border-color: #74cbfc;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "border-radius: 5px;\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "border-color: #e974fc;\n"
                                    "border-width: 3px\n"
                                    "}")
        self.previous.setText("previous")
        self.previous.setObjectName("previous")
        self.next = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next.setGeometry(QtCore.QRect(150, 830, 140, 40))
        self.next.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.next.setToolTip("")
        self.next.setStyleSheet("QPushButton {\n"
                                "color: #000000;\n"
                                "background-color: #74cbfc;\n"
                                "border-width: 1px;\n"
                                "border-style: solid black;\n"
                                "border-radius: 20px;\n"
                                "border-color: #74cbfc;\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "border-radius: 5px;\n"
                                "}\n"
                                "QPushButton:pressed {\n"
                                "border-color: #e974fc;\n"
                                "border-width: 3px\n"
                                "}")
        self.next.setText("next")
        self.next.setObjectName("next")
        self.searchbar = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.searchbar.setGeometry(QtCore.QRect(10, 10, 970, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchbar.setFont(font)
        self.searchbar.setToolTip("The searchbar dumbass.")
        self.searchbar.setToolTipDuration(-1)
        self.searchbar.setWhatsThis("")
        self.searchbar.setStyleSheet("QLineEdit {\n"
                                     "color: #a8a8a8;\n"
                                     "background-color: #4d4d4d;\n"
                                     "border: 2px solid #36393e;\n"
                                     "border-radius: 20px;\n"
                                     "padding-right: 20px;\n"
                                     "padding-left: 20px;}\n"
                                     "QLineEdit:hover {\n"
                                     "border-color: #74cbfc;}\n"
                                     "QLineEdit:focus {\n"
                                     "border-radius: 5px;\n"
                                     "border-color: #e974fc;}")
        self.searchbar.setInputMask("")
        self.searchbar.setText("")
        self.searchbar.setClearButtonEnabled(True)
        self.searchbar.setObjectName("searchbar")
        self.meta_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.meta_3.setGeometry(QtCore.QRect(280, 440, 350, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.meta_3.setFont(font)
        self.meta_3.setToolTip("")
        self.meta_3.setStyleSheet("color: #c0c0c0;")
        self.meta_3.setLineWidth(1)
        self.meta_3.setText("K views /  weeks ago")
        self.meta_3.setObjectName("meta_3")
        self.user_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.user_3.setGeometry(QtCore.QRect(280, 400, 350, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.user_3.setFont(font)
        self.user_3.setToolTip("")
        self.user_3.setStyleSheet("color: #c0c0c0;")
        self.user_3.setText("Username")
        self.user_3.setObjectName("user_3")
        self.title_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_3.setGeometry(QtCore.QRect(280, 360, 350, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.title_3.setFont(font)
        self.title_3.setToolTip("")
        self.title_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_3.setText("Video Title")
        self.title_3.setWordWrap(True)
        self.title_3.setObjectName("title_3")
        self.meta_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.meta_2.setGeometry(QtCore.QRect(280, 290, 350, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.meta_2.setFont(font)
        self.meta_2.setToolTip("")
        self.meta_2.setStyleSheet("color: #c0c0c0;")
        self.meta_2.setLineWidth(1)
        self.meta_2.setText("K views /  weeks ago")
        self.meta_2.setObjectName("meta_2")
        self.user_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.user_2.setGeometry(QtCore.QRect(280, 250, 350, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.user_2.setFont(font)
        self.user_2.setToolTip("")
        self.user_2.setStyleSheet("color: #c0c0c0;")
        self.user_2.setText("Username")
        self.user_2.setObjectName("user_2")
        self.title_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_2.setGeometry(QtCore.QRect(280, 210, 350, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.title_2.setFont(font)
        self.title_2.setToolTip("")
        self.title_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_2.setText("Video Title")
        self.title_2.setWordWrap(True)
        self.title_2.setObjectName("title_2")
        self.meta_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.meta_4.setGeometry(QtCore.QRect(280, 590, 350, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.meta_4.setFont(font)
        self.meta_4.setToolTip("")
        self.meta_4.setStyleSheet("color: #c0c0c0;")
        self.meta_4.setLineWidth(1)
        self.meta_4.setText("K views /  weeks ago")
        self.meta_4.setObjectName("meta_4")
        self.user_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.user_4.setGeometry(QtCore.QRect(280, 550, 350, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.user_4.setFont(font)
        self.user_4.setToolTip("")
        self.user_4.setStyleSheet("color: #c0c0c0;")
        self.user_4.setText("Username")
        self.user_4.setObjectName("user_4")
        self.title_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_4.setGeometry(QtCore.QRect(280, 510, 350, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.title_4.setFont(font)
        self.title_4.setToolTip("")
        self.title_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_4.setText("Video Title")
        self.title_4.setWordWrap(True)
        self.title_4.setObjectName("title_4")
        self.meta_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.meta_5.setGeometry(QtCore.QRect(280, 740, 350, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.meta_5.setFont(font)
        self.meta_5.setToolTip("")
        self.meta_5.setStyleSheet("color: #c0c0c0;")
        self.meta_5.setLineWidth(1)
        self.meta_5.setText("K views /  weeks ago")
        self.meta_5.setObjectName("meta_5")
        self.user_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.user_5.setGeometry(QtCore.QRect(280, 700, 350, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.user_5.setFont(font)
        self.user_5.setToolTip("")
        self.user_5.setStyleSheet("color: #c0c0c0;")
        self.user_5.setText("Username")
        self.user_5.setObjectName("user_5")
        self.title_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_5.setGeometry(QtCore.QRect(280, 660, 350, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.title_5.setFont(font)
        self.title_5.setToolTip("")
        self.title_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_5.setText("Video Title")
        self.title_5.setWordWrap(True)
        self.title_5.setObjectName("title_5")
        self.next_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_2.setGeometry(QtCore.QRect(990, 10, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.next_2.setFont(font)
        self.next_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.next_2.setToolTip("")
        self.next_2.setStyleSheet("QPushButton {\n"
                                  "color: #000000;\n"
                                  "background-color: #74cbfc;\n"
                                  "border: 1px solid black;\n"
                                  "border-radius: 20px;\n"
                                  "border-color: #74cbfc;\n"
                                  "text-align: center;\n"
                                  "padding-bottom: 4px;}\n"
                                  "QPushButton:hover {\n"
                                  "border-radius: 5px;}\n"
                                  "QPushButton:pressed {\n"
                                  "border-color: #e974fc;\n"
                                  "border-width: 3px}")
        self.next_2.setText("⌕")
        self.next_2.setObjectName("next_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 256, 144))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.pushButton.setFont(font)

        url = 'https://img.youtube.com/vi/Y2gTSjoEExc/mqdefault.jpg'
        temp = tempfile.TemporaryFile()
        (Image.open(BytesIO(requests.get(url).content))).resize((256, 144)).save(f"{temp.name}.bmp")

        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "border-width: 1px;\n"
                                      "border-style: solid;\n"
                                      "border-radius: 25px;\n"
                                      "border-color: #2b2b2b;\n"
                                      "width: 144px;\n"
                                      "height: 256px;\n"
                                      f"background-image: url({Path(f'{temp.name}.bmp').as_posix()}) 0 0 0 0 stretch stretch;"
                                      "background-position: center;}\n"
                                      "QPushButton:hover{\n"
                                      "border-radius: 12px;\n"
                                      "border-width: 3px;\n"
                                      "border-color: #74cbfc}\n"
                                      "QPushButton:pressed{\n"
                                      "border-width: 3px;\n"
                                      "border-color: #e974fc;}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 256, 144))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "border-width: 1px;\n"
                                        "border-style: solid;\n"
                                        "border-radius: 25px;\n"
                                        "border-color: #2b2b2b;\n"
                                        "width: 144px;\n"
                                        "height: 256px;\n"
                                        f"background-image: url({Path(f'{temp.name}.bmp').as_posix()}) 0 0 0 0 stretch stretch;"
                                        "background-position: center;}\n"
                                        "QPushButton:hover{\n"
                                        "border-radius: 12px;\n"
                                        "border-width: 3px;\n"
                                        "border-color: #74cbfc}\n"
                                        "QPushButton:pressed{\n"
                                        "border-width: 3px;\n"
                                        "border-color: #e974fc;}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 360, 256, 144))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "border-width: 1px;\n"
                                        "border-style: solid;\n"
                                        "border-radius: 25px;\n"
                                        "border-color: #2b2b2b;\n"
                                        "width: 144px;\n"
                                        "height: 256px;\n"
                                        f"background-image: url({Path(f'{temp.name}.bmp').as_posix()}) 0 0 0 0 stretch stretch;"
                                        "background-position: center;}\n"
                                        "QPushButton:hover{\n"
                                        "border-radius: 12px;\n"
                                        "border-width: 3px;\n"
                                        "border-color: #74cbfc}\n"
                                        "QPushButton:pressed{\n"
                                        "border-width: 3px;\n"
                                        "border-color: #e974fc;}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 510, 256, 144))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "border-width: 1px;\n"
                                        "border-style: solid;\n"
                                        "border-radius: 25px;\n"
                                        "border-color: #2b2b2b;\n"
                                        "width: 144px;\n"
                                        "height: 256px;\n"
                                        f"background-image: url({Path(f'{temp.name}.bmp').as_posix()}) 0 0 0 0 stretch stretch;"
                                        "background-position: center;}\n"
                                        "QPushButton:hover{\n"
                                        "border-radius: 12px;\n"
                                        "border-width: 3px;\n"
                                        "border-color: #74cbfc}\n"
                                        "QPushButton:pressed{\n"
                                        "border-width: 3px;\n"
                                        "border-color: #e974fc;}")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 660, 256, 144))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "border-width: 1px;\n"
                                        "border-style: solid;\n"
                                        "border-radius: 25px;\n"
                                        "border-color: #2b2b2b;\n"
                                        "width: 144px;\n"
                                        "height: 256px;\n"
                                        f"background-image: url({Path(f'{temp.name}.bmp').as_posix()}) 0 0 0 0 stretch stretch;"
                                        "background-position: center;}\n"
                                        "QPushButton:hover{\n"
                                        "border-radius: 12px;\n"
                                        "border-width: 3px;\n"
                                        "border-color: #74cbfc}\n"
                                        "QPushButton:pressed{\n"
                                        "border-width: 3px;\n"
                                        "border-color: #e974fc;}")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        ytQt.setCentralWidget(self.centralwidget)

        self.retranslateUi(ytQt)
        QtCore.QMetaObject.connectSlotsByName(ytQt)

    def retranslateUi(self, ytQt):
        _translate = QtCore.QCoreApplication.translate
        self.searchbar.setPlaceholderText(_translate("ytQt", "Search YouTube..."))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ytQt = QtWidgets.QMainWindow()
    ui = Ui_ytQt()
    ui.setupUi(ytQt)
    ytQt.show()
    sys.exit(app.exec())
