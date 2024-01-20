#    ytQt, an alternative youtube frontend desktop application using python and Qt.
#    Copyright (C) 2024  D.L. ten Bosch
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import platform

import vlc
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ytQt(object):
    def setupUi(self, ytQt):
        ytQt.setObjectName("ytQt video playback")
        ytQt.setWindowTitle('ytQt video playback')
        ytQt.resize(1280, 810)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ytQt.sizePolicy().hasHeightForWidth())
        ytQt.setSizePolicy(sizePolicy)
        ytQt.setStyleSheet("background-color: #2a2a2a;")
        ytQt.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(parent=ytQt)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.pause = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(600, 760, 80, 40))
        self.pause.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pause.setToolTip("")
        self.pause.setStyleSheet("QPushButton {\n"
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
        self.pause.setText("pause")
        self.pause.setObjectName("pause")
        self.rewind = QtWidgets.QPushButton(parent=self.centralwidget)
        self.rewind.setGeometry(QtCore.QRect(550, 760, 40, 40))
        self.rewind.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.rewind.setToolTip("")
        self.rewind.setStyleSheet("QPushButton {\n"
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
        self.rewind.setText("-10")
        self.rewind.setObjectName("rewind")
        self.wind = QtWidgets.QPushButton(parent=self.centralwidget)
        self.wind.setGeometry(QtCore.QRect(690, 760, 40, 40))
        self.wind.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.wind.setToolTip("")
        self.wind.setStyleSheet("QPushButton {\n"
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
        self.wind.setText("+10")
        self.wind.setObjectName("wind")
        self.volumeslider = QtWidgets.QSlider(parent=self.centralwidget)
        self.volumeslider.setGeometry(QtCore.QRect(1090, 759, 90, 40))
        self.volumeslider.setStyleSheet("QSlider::groove:horizontal {\n"
                                        "border: 1px solid #74cbfc;\n"
                                        "background: #2b2b2b;\n"
                                        "height: 20px;\n"
                                        "border-radius: 4px;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::sub-page:horizontal {\n"
                                        "background: #2b2b2b;\n"
                                        "border: 1px solid red;\n"
                                        "height: 20px;\n"
                                        "border-radius: 4px;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::add-page:horizontal {\n"
                                        "background: #2b2b2b;\n"
                                        "border: 1px solid green;\n"
                                        "height: 20px;\n"
                                        "border-radius: 4px;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::handle:horizontal {\n"
                                        "background: #4d4d4d;\n"
                                        "border: 1px solid #4d4d4d;\n"
                                        "width: 20px;\n"
                                        "margin-top: -2px;\n"
                                        "margin-bottom: -2px;\n"
                                        "border-radius: 4px;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::handle:horizontal:hover {\n"
                                        "background: #a8a8a8;\n"
                                        "border: 1px solid #a8a8a8;\n"
                                        "border-radius: 4px;\n"
                                        "}\n"
                                        "")
        self.volumeslider.setMinimum(1)
        self.volumeslider.setMaximum(100)
        self.volumeslider.setSingleStep(10)
        self.volumeslider.setPageStep(10)
        self.volumeslider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volumeslider.setInvertedControls(False)
        self.volumeslider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.volumeslider.setTickInterval(1)
        self.volumeslider.setObjectName("volumeslider")
        self.fullscreen = QtWidgets.QPushButton(parent=self.centralwidget)
        self.fullscreen.setGeometry(QtCore.QRect(1190, 760, 80, 40))
        self.fullscreen.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.fullscreen.setToolTip("")
        self.fullscreen.setStyleSheet("QPushButton {\n"
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
        self.fullscreen.setText("fullscreen")
        self.fullscreen.setObjectName("fullscreen")
        self.wind_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.wind_2.setGeometry(QtCore.QRect(100, 760, 40, 40))
        self.wind_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.wind_2.setToolTip("")
        self.wind_2.setStyleSheet("QPushButton {\n"
                                  "color: #000000;\n"
                                  "background-color: #74cbfc;\n"
                                  "border-width: 1px;\n"
                                  "border-style: solid black;\n"
                                  "border-radius: 20px;\n"
                                  "border-color: #74cbfc;\n"
                                  "}\n"
                                  "QPushButton:hover {\n"
                                  "border-radius: 5px;\n"
                                  "background-color: #EE9090;\n"
                                  "}\n"
                                  "QPushButton:pressed {\n"
                                  "border-color: #e974fc;\n"
                                  "border-width: 3px\n"
                                  "}")
        self.wind_2.setText("dislike")
        self.wind_2.setObjectName("wind_2")
        self.like = QtWidgets.QPushButton(parent=self.centralwidget)
        self.like.setGeometry(QtCore.QRect(150, 760, 40, 40))
        self.like.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.like.setToolTip("")
        self.like.setStyleSheet("QPushButton {\n"
                                "color: #000000;\n"
                                "background-color: #74cbfc;\n"
                                "border-width: 1px;\n"
                                "border-style: solid black;\n"
                                "border-radius: 20px;\n"
                                "border-color: #74cbfc;\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "border-radius: 5px;\n"
                                "background-color: lightgreen;\n"
                                "}\n"
                                "QPushButton:pressed {\n"
                                "border-color: #e974fc;\n"
                                "border-width: 3px\n"
                                "}")
        self.like.setText("like")
        self.like.setObjectName("like")
        self.wind_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.wind_4.setGeometry(QtCore.QRect(10, 760, 80, 40))
        self.wind_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.wind_4.setToolTip("")
        self.wind_4.setStyleSheet("QPushButton {\n"
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
        self.wind_4.setText("comments")
        self.wind_4.setObjectName("wind_4")
        self.videoslider = QtWidgets.QSlider(parent=self.centralwidget)
        self.videoslider.setGeometry(QtCore.QRect(10, 730, 1260, 20))
        self.videoslider.setStyleSheet("QSlider::groove:horizontal {\n"
                                       "border: 1px solid #74cbfc;\n"
                                       "background: #2b2b2b;\n"
                                       "height: 10px;\n"
                                       "border-radius: 4px;\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::sub-page:horizontal {\n"
                                       "background: #2b2b2b;\n"
                                       "border: 1px solid #e974fc;\n"
                                       "height: 10px;\n"
                                       "border-radius: 4px;\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::add-page:horizontal {\n"
                                       "background: #2b2b2b;\n"
                                       "border: 1px solid #74cbfc;\n"
                                       "height: 10px;\n"
                                       "border-radius: 4px;\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::handle:horizontal {\n"
                                       "background: #4d4d4d;\n"
                                       "border: 1px solid #4d4d4d;\n"
                                       "width: 13px;\n"
                                       "border-radius: 4px;\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::handle:horizontal:hover {\n"
                                       "background: #a8a8a8;\n"
                                       "border: 1px solid #a8a8a8;\n"
                                       "border-radius: 4px;\n"
                                       "}\n"
                                       "")
        self.videoslider.setMinimum(1)
        self.videoslider.setMaximum(1000)
        self.videoslider.setSingleStep(10)
        self.videoslider.setPageStep(1)
        self.videoslider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.videoslider.setInvertedControls(False)
        self.videoslider.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        self.videoslider.setTickInterval(1)
        self.videoslider.setObjectName("videoslider")
        #self.videoslider.setFocusPolicy(Qt.NoFocus)
        ytQt.setCentralWidget(self.centralwidget)
        self.retranslateUi(ytQt)
        QtCore.QMetaObject.connectSlotsByName(ytQt)
        #
        print(sys.argv[1])
        self.vlc_instance = vlc.Instance()
        self.mediaplayer = self.vlc_instance.media_player_new()
        if platform.system() == "Linux":
            self.mediaplayer.set_xwindow(int(self.frame.winId()))
        elif platform.system() == "Windows":
            self.mediaplayer.set_hwnd(int(self.frame.winId()))
        self.media_path = sys.argv[1]
        self.media = self.vlc_instance.media_new(self.media_path)
        self.media.get_mrl()
        self.mediaplayer.set_media(self.media)
        self.mediaplayer.play()
        self.fullscreen.clicked.connect(self.fullscreentoggle)
        self.wind.clicked.connect(self.skip)
        self.rewind.clicked.connect(self.reskip)
        self.pause.clicked.connect(self.playpause)
        self.videoslider.sliderMoved.connect(self.videoprogress)
        self.volumeslider.setValue(self.mediaplayer.audio_get_volume())
        self.volumeslider.valueChanged.connect(self.audiolevel)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.updateslider)
        self.timer.start()

    def skip(self):
        self.mediaplayer.set_time(self.mediaplayer.get_time() + 5000)

    def reskip(self):
        self.mediaplayer.set_time(self.mediaplayer.get_time() - 5000)

    def fullscreentoggle(self):
        print('noinplementation')

    def playpause(self):
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            self.pause.setText('play')
            self.is_paused = True
        else:
            if self.mediaplayer.play() == -1:
                self.media_path = sys.argv[1]
                self.media = self.vlc_instance.media_new(self.media_path)
                self.media.get_mrl()
                self.mediaplayer.set_media(self.media)
                return
            self.mediaplayer.play()
            self.pause.setText('pause')
            self.is_paused = False

    def videoprogress(self):
        self.mediaplayer.set_position(self.videoslider.value() / 1000)

    def updateslider(self):
        self.videoslider.setValue(int(self.mediaplayer.get_position() * 1000))

    def retranslateUi(self, ytQt):
        _translate = QtCore.QCoreApplication.translate
        ytQt.setWindowTitle(_translate("ytQt", "ytQt"))

    def audiolevel(self):
        self.mediaplayer.audio_set_volume(self.volumeslider.value())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ytQt = QtWidgets.QMainWindow()
    ui = Ui_ytQt()
    ui.setupUi(ytQt)
    ytQt.show()
    sys.exit(app.exec())
