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


import json
import os
import tempfile
from io import BytesIO
from pathlib import Path

import requests
from PIL import Image
from PyQt6 import QtCore, QtGui, QtWidgets
from pytube import YouTube

key = 'AIzaSyDuWZalLquMoISDybPsuOYs75cAeAEtEzo'
# key = 'AIzaSyCDqJTmI3gkjv7-KfWQzo1jqad1HoUqOQc'
baseurl = "https://youtube.googleapis.com/"
basethumbstyle = ("QPushButton:hover{\n"
                  "border-radius: 12px;\n"
                  "border-width: 3px;\n"
                  "border-color: #74cbfc}\n"
                  "QPushButton:pressed{\n"
                  "border-width: 3px;\n"
                  "border-color: #e974fc;}\n"
                  "QPushButton{\n"
                  "color: rgb(0, 0, 0);\n"
                  "border-width: 1px;\n"
                  "border-style: solid;\n"
                  "border-radius: 25px;\n"
                  "border-color: #2b2b2b;\n"
                  "width: 144px;\n"
                  "height: 256px;\n"
                  "background-position: center;\n")
global title
global user
global thumbnail
global kind
global id
global videostreamlink
global channelid
channelid = [None, None, None, None, None]
id = [None, None, None, None, None]
kind = [None, None, None, None, None]


class Ui_ytQt(object):
    def setupUi(self, ytQt):
        ytQt.setObjectName("ytQt")
        ytQt.setEnabled(True)
        ytQt.resize(1040, 864)
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
        self.title.setToolTip("")
        self.title.setStyleSheet("color: rgb(255, 255, 255);")
        self.title.setText("")
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
        self.user.setText("")
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
        self.meta.setText("")
        self.meta.setObjectName("meta")
        self.previous = QtWidgets.QPushButton(parent=self.centralwidget)
        self.previous.setGeometry(QtCore.QRect(10, 814, 130, 40))
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
        self.next.setGeometry(QtCore.QRect(150, 814, 140, 40))
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
        self.search = QtWidgets.QPushButton(parent=self.centralwidget)
        self.search.setGeometry(QtCore.QRect(990, 10, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.search.setFont(font)
        self.search.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.search.setToolTip("")
        self.search.setStyleSheet("QPushButton {\n"
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
        self.search.setText("⌕")
        self.search.setObjectName("search")
        self.thumbnail = QtWidgets.QPushButton(parent=self.centralwidget)
        self.thumbnail.setGeometry(QtCore.QRect(10, 60, 256, 144))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.thumbnail.setFont(font)
        self.thumbnail.setText("")
        self.thumbnail.setObjectName("thumbnail")
        self.meta_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.meta_2.setGeometry(QtCore.QRect(280, 290, 750, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.meta_2.setFont(font)
        self.meta_2.setToolTip("")
        self.meta_2.setStyleSheet("color: #c0c0c0;")
        self.meta_2.setLineWidth(1)
        self.meta_2.setText("")
        self.meta_2.setObjectName("meta_2")
        self.user_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.user_2.setGeometry(QtCore.QRect(280, 250, 750, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.user_2.setFont(font)
        self.user_2.setToolTip("")
        self.user_2.setStyleSheet("color: #c0c0c0;")
        self.user_2.setText("")
        self.user_2.setObjectName("user_2")
        self.title_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_2.setGeometry(QtCore.QRect(280, 210, 750, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.title_2.setFont(font)
        self.title_2.setToolTip(
            "This title is too long to be displayed properly on yt, look at tooltip! Hello tooltip user!")
        self.title_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_2.setText("")
        self.title_2.setScaledContents(False)
        self.title_2.setWordWrap(False)
        self.title_2.setObjectName("title_2")
        self.meta_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.meta_3.setGeometry(QtCore.QRect(280, 440, 750, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.meta_3.setFont(font)
        self.meta_3.setToolTip("")
        self.meta_3.setStyleSheet("color: #c0c0c0;")
        self.meta_3.setLineWidth(1)
        self.meta_3.setText("")
        self.meta_3.setObjectName("meta_3")
        self.user_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.user_3.setGeometry(QtCore.QRect(280, 400, 750, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.user_3.setFont(font)
        self.user_3.setToolTip("")
        self.user_3.setStyleSheet("color: #c0c0c0;")
        self.user_3.setText("")
        self.user_3.setObjectName("user_3")
        self.title_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_3.setGeometry(QtCore.QRect(280, 360, 750, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.title_3.setFont(font)
        self.title_3.setToolTip(
            "This title is too long to be displayed properly on yt, look at tooltip! Hello tooltip user!")
        self.title_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_3.setText("")
        self.title_3.setScaledContents(False)
        self.title_3.setWordWrap(False)
        self.title_3.setObjectName("title_3")
        self.meta_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.meta_4.setGeometry(QtCore.QRect(280, 590, 750, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.meta_4.setFont(font)
        self.meta_4.setToolTip("")
        self.meta_4.setStyleSheet("color: #c0c0c0;")
        self.meta_4.setLineWidth(1)
        self.meta_4.setText("")
        self.meta_4.setObjectName("meta_4")
        self.user_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.user_4.setGeometry(QtCore.QRect(280, 550, 750, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.user_4.setFont(font)
        self.user_4.setToolTip("")
        self.user_4.setStyleSheet("color: #c0c0c0;")
        self.user_4.setText("")
        self.user_4.setObjectName("user_4")
        self.title_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_4.setGeometry(QtCore.QRect(280, 510, 750, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.title_4.setFont(font)
        self.title_4.setToolTip(
            "This title is too long to be displayed properly on yt, look at tooltip! Hello tooltip user!")
        self.title_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_4.setText("")
        self.title_4.setScaledContents(False)
        self.title_4.setWordWrap(False)
        self.title_4.setObjectName("title_4")
        self.meta_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.meta_5.setGeometry(QtCore.QRect(280, 740, 750, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.meta_5.setFont(font)
        self.meta_5.setToolTip("")
        self.meta_5.setStyleSheet("color: #c0c0c0;")
        self.meta_5.setLineWidth(1)
        self.meta_5.setText("")
        self.meta_5.setObjectName("meta_5")
        self.user_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.user_5.setGeometry(QtCore.QRect(280, 700, 750, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.user_5.setFont(font)
        self.user_5.setToolTip("")
        self.user_5.setStyleSheet("color: #c0c0c0;")
        self.user_5.setText("")
        self.user_5.setObjectName("user_5")
        self.title_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_5.setGeometry(QtCore.QRect(280, 660, 750, 36))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.title_5.setFont(font)
        self.title_5.setToolTip(
            "This title is too long to be displayed properly on yt, look at tooltip! Hello tooltip user!")
        self.title_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_5.setText("")
        self.title_5.setScaledContents(False)
        self.title_5.setWordWrap(False)
        self.title_5.setObjectName("title_5")
        self.thumbnail_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.thumbnail_2.setGeometry(QtCore.QRect(10, 210, 256, 144))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.thumbnail_2.setFont(font)
        self.thumbnail_2.setText("")
        self.thumbnail_2.setObjectName("thumbnail_2")
        self.thumbnail_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.thumbnail_3.setGeometry(QtCore.QRect(10, 360, 256, 144))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.thumbnail_3.setFont(font)
        self.thumbnail_3.setText("")
        self.thumbnail_3.setObjectName("thumbnail_3")
        self.thumbnail_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.thumbnail_4.setGeometry(QtCore.QRect(10, 510, 256, 144))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.thumbnail_4.setFont(font)
        self.thumbnail_4.setText("")
        self.thumbnail_4.setObjectName("thumbnail_4")
        self.thumbnail_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.thumbnail_5.setGeometry(QtCore.QRect(10, 660, 256, 144))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.thumbnail_5.setFont(font)
        self.thumbnail_5.setText("")
        self.thumbnail_5.setObjectName("thumbnail_5")
        ytQt.setCentralWidget(self.centralwidget)
        self.retranslateUi(ytQt)
        QtCore.QMetaObject.connectSlotsByName(ytQt)
        #
        self.searchbar.returnPressed.connect(self.searchyt)
        self.thumbnaillist = [self.thumbnail, self.thumbnail_2, self.thumbnail_3, self.thumbnail_4, self.thumbnail_5, ]
        self.titlelist = [self.title, self.title_2, self.title_3, self.title_4, self.title_5, ]
        self.userlist = [self.user, self.user_2, self.user_3, self.user_4, self.user_5, ]
        self.metalist = [self.meta, self.meta_2, self.meta_3, self.meta_4, self.meta_5]
        self.search.clicked.connect(self.searchyt)
        # url = 'https://img.youtube.com/vi/Y2gTSjoEExc/mqdefault.jpg'
        # temp = tempfile.TemporaryFile(prefix='ytQtthumbnail')
        # (Image.open(BytesIO(requests.get(url).content))).resize((256, 144)).save(f"{temp.name}.bmp")
        # path = Path(f'{temp.name}.bmp').as_posix()
        path = None
        self.thumbnail_5.setStyleSheet(basethumbstyle + f"background-image: url({path}) 0 0 0 0 stretch stretch;" + "}")
        self.thumbnail_5.clicked.connect(lambda: self.openbutton(4))
        self.thumbnail_4.setStyleSheet(basethumbstyle + f"background-image: url({path}) 0 0 0 0 stretch stretch;" + "}")
        self.thumbnail_4.clicked.connect(lambda: self.openbutton(3))
        self.thumbnail_3.setStyleSheet(basethumbstyle + f"background-image: url({path}) 0 0 0 0 stretch stretch;" + "}")
        self.thumbnail_3.clicked.connect(lambda: self.openbutton(2))
        self.thumbnail_2.setStyleSheet(basethumbstyle + f"background-image: url({path}) 0 0 0 0 stretch stretch;" + "}")
        self.thumbnail_2.clicked.connect(lambda: self.openbutton(1))
        self.thumbnail.setStyleSheet(basethumbstyle + f"background-image: url({path}) 0 0 0 0 stretch stretch;" + "}")
        self.thumbnail.clicked.connect(lambda: self.openbutton(0))
        # self.next.clicked.connect(self.next)
        # self.previous.clicked.connect(self.previous)

    def next(self):
        print("Next clicked")

    def previous(self):
        print("Previous clicked")

    def searchyt(self):
        self.searchbar.clearFocus()
        ytquery = self.searchbar.text()
        params = {'part': 'snippet', 'key': key, "q": ytquery, "maxResults": "5"}
        print('requesting search api data')
        searchResponse = requests.get(baseurl + 'youtube/v3/search', params=params)
        #searchResponse = requests.get('https://files.catbox.moe/7j4a26.json')
        obj = json.loads(searchResponse.text)
        print('search api data loaded')
        self.loadvideos(obj)


    def openbutton(self, index):
        global kind
        global id
        if kind[index] == 'youtube#video':
            print('opening type ' + str(kind[index]) + ' with url ' + 'https://youtube.com/watch?v=' + str(id[index]))
            print('creating temp file')
            temp = tempfile.TemporaryFile(prefix='ytQtvideo', suffix='.mp4', delete=False)
            print('temp file created @ ' + Path(temp.name).as_posix())
            print('downloading video steam to temp file')
            YouTube('https://youtube.com/watch?v=' + str(id[index])).streams.get_highest_resolution().download(
                filename=Path(temp.name).as_posix())
            print('launching video player with video file @ ' + Path(temp.name).as_posix())
            temp.close()
            os.system('python player.py ' + Path(temp.name).as_posix())
            os.remove(temp.name)
            print('removed temp file @ ' + Path(temp.name).as_posix())
        elif kind[index] == 'youtube#channel':
            params = {'part': 'contentDetails', 'key': key, "id": channelid[index]}
            print('requesting channel api data')
            searchResponse = requests.get(baseurl + 'youtube/v3/channels', params=params)
            obj = json.loads(searchResponse.text)
            print('channel api data loaded')
            plid = obj['items'][0]['contentDetails']['relatedPlaylists'].get('uploads')
            params = {'part': 'snippet', 'key': key, "playlistId": plid, 'maxResults': '5'}
            print('requesting uploads api data')
            searchResponse = requests.get(baseurl + 'youtube/v3/playlistItems', params=params)
            obj = json.loads(searchResponse.text)
            print('uploads api data loaded')
            print(searchResponse.text)
            self.loadvideos(obj)
    def loadvideos(self, obj):
        print('loading item json')
        for i in range(0, 5):
            global title
            global user
            global thumbnail
            global kind
            global id
            global videostreamlink
            title = obj['items'][i]['snippet'].get('title')
            user = obj['items'][i]['snippet'].get('channelTitle')
            channelid[i] = obj['items'][i]['snippet'].get('channelId')
            thumbnail = obj['items'][i]['snippet']['thumbnails']['medium'].get('url')
            if not obj['items'][i].get('kind') == 'youtube#playlistItem':
                kind[i] = obj['items'][i]['id'].get('kind')
                id[i] = obj['items'][i]['id'].get('videoId')
            else:
                kind[i] = 'youtube#video'
                id[i] = obj['items'][i]['snippet']['resourceId'].get('videoId')

            temp = tempfile.TemporaryFile(prefix='ytQtthumbnail')
            if kind[i] == 'youtube#channel':
                self.thumbnaillist[i].setFixedWidth(144)
                (Image.open(BytesIO(requests.get(thumbnail).content))).resize((144, 144)).save(f"{temp.name}.bmp")
            elif kind[i] == 'youtube#video':
                self.thumbnaillist[i].setFixedWidth(256)
                (Image.open(BytesIO(requests.get(thumbnail).content))).resize((256, 144)).save(f"{temp.name}.bmp")
            path = Path(f'{temp.name}.bmp').as_posix()
            self.thumbnaillist[i].setStyleSheet(
                basethumbstyle + f"background-image: url({path}) 0 0 0 0 stretch stretch;" + "}")
            self.titlelist[i].setText(title)
            self.userlist[i].setText(user)
        print('item json loaded')

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
