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
import base64
import platform

import base64
import vlc
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget


class Ui_ytQt(QWidget):

    def setupUi(self):
        self.setObjectName("ytQt video playback")
        self.setWindowTitle('ytQt video playback')
        self.resize(1280, 810)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet("background-color: #2a2a2a;")
        # self.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(parent=self)
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
        self.rewind.setText("-5")
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
        self.wind.setText("+5")
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
        self.dislike = QtWidgets.QPushButton(parent=self.centralwidget)
        self.dislike.setGeometry(QtCore.QRect(100, 760, 40, 40))
        self.dislike.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.dislike.setToolTip("")
        self.dislike.setStyleSheet("QPushButton {\n"
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
        self.dislike.setText("dislike")
        self.dislike.setObjectName("dislike")
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
        self.comments = QtWidgets.QPushButton(parent=self.centralwidget)
        self.comments.setGeometry(QtCore.QRect(10, 760, 80, 40))
        self.comments.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.comments.setToolTip("")
        self.comments.setStyleSheet("QPushButton {\n"
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
        self.comments.setText("comments")
        self.comments.setObjectName("comments")
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
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        #
        sys.argv[1] = base64.b64decode(sys.argv[1]).decode()
        self.vlc_instance = vlc.Instance(['--video-on-top', '--verbose=-1'])
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
        # self.fullscreen.clicked.connect(self.fullscreentoggle)
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
        self.videoslider.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.volumeslider.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.frame.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.fullscreen.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pause.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.like.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.dislike.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.comments.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.wind.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.rewind.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)

    def __init__(self):
        super().__init__()
        self.setupUi()

    def keyPressEvent(self, e):
        print(str(e.key()))
        if e.isAutoRepeat():
            return
        if str(e.key()) == '32':
            # self.playpause()
            self.fullscreentoggle()
        elif str(e.key()) == '16777235':
            if self.volumeslider.value() <= 90:
                self.volumeslider.setValue(self.volumeslider.value() + 10)
            else:
                self.volumeslider.setValue(100)
            self.mediaplayer.audio_set_volume(self.volumeslider.value())
        elif str(e.key()) == '16777237':
            if self.volumeslider.value() >= 10:
                self.volumeslider.setValue(self.volumeslider.value() - 10)
            else:
                self.volumeslider.setValue(0)
            self.mediaplayer.audio_set_volume(self.volumeslider.value())
        elif str(e.key()) == '16777236':
            self.skip()
        elif str(e.key()) == '16777234':
            self.reskip()

    def skip(self):
        self.mediaplayer.set_time(self.mediaplayer.get_time() + 5000)
        self.updateslider()

    def reskip(self):
        self.mediaplayer.set_time(self.mediaplayer.get_time() - 5000)
        self.updateslider()

    # @QtCore.pyqtSlot("QWebEngineFullScreenRequest")
    def fullscreentoggle(self):
        print('a')
    #     if str(self.frame.parent()) == str(self.centralwidget):
    #         print('setting frame to fullscreen view')
    #         self.frame.setParent(None)
    #         self.frame.showFullScreen()
    #         # self.hide()
    #         # self.setFocus()
    #         # self.frame.show()
    #     else:
    #         print('setting frame to regular view')
    #         #self.show()
    #         self.frame.setParent(self.centralwidget)
    #         self.frame.showNormal()


        # if request.toggleOn():
        #     self.browser.setParent(None)
        #     self.browser.showFullScreen()
        # else:
        #     self.setCentralWidget(self.browser)
        #     self.browser.showNormal()

    def playpause(self):
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            self.pause.setText('play')
            self.is_paused = True
        else:
            if self.mediaplayer.play() == -1:
                print('calamiteit')
                self.media_path = sys.argv[1]
                self.media = self.vlc_instance.media_new(self.media_path)
                self.media.get_mrl()
                self.mediaplayer.set_media(self.media)
                return
            self.mediaplayer.play()
            self.pause.setText('pause')
            self.is_paused = False
        self.updateslider()

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
    # ytQt = QtWidgets.QMainWindow()
    # ui = Ui_ytQt()
    # ui.setupUi(ytQt)
    # ytQt.show()
    ex = Ui_ytQt()
    ex.show()
    sys.exit(app.exec())
