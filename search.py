#    ytQt, an alternative youtube frontend desktop application using python and Qt.
#    Copyright (C) 2024  D.L. ten Bosch
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import base64
import json
import os
import platform
import sys
import tempfile
from io import BytesIO
from pathlib import Path

import requests
import vlc
from PIL import Image
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtGui import QKeyEvent
from pytube import YouTube


class Search(QtWidgets.QMainWindow):
    def __init__(self):

        # initialize search ui
        global appPath
        super(Search, self).__init__()
        try:
            appPath = sys._MEIPASS
        except Exception:
            appPath = os.path.abspath('./assets')
        print(appPath)

        uic.loadUi(os.path.join(appPath, 'search.ui'), self)
        self.setWindowIcon(QtGui.QIcon('assets/ytQt.ico'))
        self.initPythonCode()
        self.show()

    def initPythonCode(self):

        # create object list for easier lookup
        self.thumbnailObjectList = [
            self.thumbnailButton1, self.thumbnailButton2, self.thumbnailButton3, self.thumbnailButton4,
            self.thumbnailButton5]
        self.titleObjectList = [
            self.titleLabel1, self.titleLabel2, self.titleLabel3, self.titleLabel4, self.titleLabel5]
        self.userObjectList = [
            self.userLabel1, self.userLabel2, self.userLabel3, self.userLabel4, self.userLabel5]

        # set up links
        self.searchButton.clicked.connect(self.searchYoutubeFunction)
        self.searchBar.returnPressed.connect(self.searchYoutubeFunction)
        self.nextPageButton.clicked.connect(self.nextPageFunction)
        self.prevPageButton.clicked.connect(self.prevPageFunction)
        self.resolutionButton.clicked.connect(self.switchResolution)
        self.prevResultButton.clicked.connect(self.prevResult)
        self.nextResultButton.clicked.connect(self.nextResult)

        # set the thumbnail background to init style
        self.thumbnailButton1.setStyleSheet('background-color: #1E2126; border: 1px solid #1E2126')
        self.thumbnailButton2.setStyleSheet('background-color: #1E2126; border: 1px solid #1E2126')
        self.thumbnailButton3.setStyleSheet('background-color: #1E2126; border: 1px solid #1E2126')
        self.thumbnailButton4.setStyleSheet('background-color: #1E2126; border: 1px solid #1E2126')
        self.thumbnailButton5.setStyleSheet('background-color: #1E2126; border: 1px solid #1E2126')

        # link the thumbnail presses to the openVideoFunction with the index of the button
        self.thumbnailButton1.clicked.connect(lambda: self.openVideoFunction(0))
        self.thumbnailButton2.clicked.connect(lambda: self.openVideoFunction(1))
        self.thumbnailButton3.clicked.connect(lambda: self.openVideoFunction(2))
        self.thumbnailButton4.clicked.connect(lambda: self.openVideoFunction(3))
        self.thumbnailButton5.clicked.connect(lambda: self.openVideoFunction(4))
        return

    def switchResolution(self):
        global resolution

        # switch resolution
        if resolution == 'HD':
            resolution = 'SD'
            self.resolutionButton.setText('SD')
        else:
            resolution = 'HD'
            self.resolutionButton.setText('HD')

    def searchYoutubeFunction(self):
        global searchResponseJSON
        global apiData
        global currentPage
        self.searchBar.clearFocus()
        currentPage = 0
        self.prevPageButton.setStyleSheet(baseButtonStyle + "color: #404040};})\n")
        self.nextPageButton.setStyleSheet(baseButtonStyle + "color: #ffffff};})\n")

        # set parameters, get json apiData from api
        userSearchQuery = self.searchBar.text()
        searchParams = {'part': 'snippet', 'key': key, "q": userSearchQuery, "maxResults": "25"}
        print('requesting search api data')
        apiData = requests.get(youtubeURLRoot + 'youtube/v3/search', params=searchParams)
        # searchResponse = requests.get('https://files.catbox.moe/7j4a26.json')

        # read json from response
        searchResponseJSON = json.loads(apiData.text)
        print('search api data loaded')

        # call function to load json into UI
        self.loadJSONFunction(True)

    def prevResult(self):
        global searchResponseJSON
        global history
        global historyIndex
        if historyIndex < 1:
            return
        historyIndex = historyIndex - 1
        searchResponseJSON = history[historyIndex]
        self.loadJSONFunction(False)

    def nextResult(self):
        global searchResponseJSON
        global history
        global historyIndex
        if historyIndex >= len(history) - 1:
            return
        historyIndex = historyIndex + 1
        searchResponseJSON = history[historyIndex]
        self.loadJSONFunction(False)

    def loadJSONFunction(self, append):
        global currentPage
        global searchResponseJSON
        global title
        global user
        global thumbnail
        global kind
        global Id
        global history
        global historyIndex
        print('history ' + str(historyIndex + 1) + ' / ' + str(len(history)))
        print('switching to page ' + str(currentPage))

        if append:
            # remove all array items after current item in history
            del history[historyIndex + 1: len(history)]

            # append json to history array
            history.append(searchResponseJSON)
            historyIndex = historyIndex + 1

        # change navigation button style
        if historyIndex < 1:
            self.prevResultButton.setStyleSheet(baseButtonStyle + "color: #404040};})\n")
        else:
            self.prevResultButton.setStyleSheet(baseButtonStyle + "color: #ffffff};})\n")

        if historyIndex > len(history) - 2:
            self.nextResultButton.setStyleSheet(baseButtonStyle + "color: #404040};})\n")
        else:
            self.nextResultButton.setStyleSheet(baseButtonStyle + "color: #ffffff};})\n")

        # loop over videos and load respective JSON
        print('loading item json')
        for i in range(0 + (currentPage * 5), 5 + (currentPage * 5)):

            if i >= len(searchResponseJSON['items']):
                print('no more items')
                return
            # 'p' is the index of the item in the JSON, for every page, 5 is added. 'i' only loops from 1-5
            p = i - (currentPage * 5)

            # extract specific items from JSON
            title = searchResponseJSON['items'][i]['snippet'].get('title')
            user = searchResponseJSON['items'][i]['snippet'].get('channelTitle')
            thumbnail = searchResponseJSON['items'][i]['snippet']['thumbnails']['medium'].get('url')
            channelId[p] = searchResponseJSON['items'][i]['snippet'].get('channelId')

            # set kind and ID of video, yt has fuzzy consistency sadly

            # playlist item
            if searchResponseJSON['items'][i].get('kind') == 'youtube#playlistItem':
                kind[p] = 'youtube#video'
                Id[p] = searchResponseJSON['items'][i]['snippet']['resourceId'].get('videoId')
            # playlist
            elif searchResponseJSON['items'][i]['id'].get('kind') == 'youtube#playlist':
                kind[p] = searchResponseJSON['items'][i]['id'].get('kind')
                Id[p] = searchResponseJSON['items'][i]['id'].get('playlistId')
            # video
            else:
                kind[p] = searchResponseJSON['items'][i]['id'].get('kind')
                Id[p] = searchResponseJSON['items'][i]['id'].get('videoId')

            # create temp file and inject sized image for storing thumbnail 'i'
            temp = tempfile.NamedTemporaryFile(prefix='ytQtthumbnail')
            if kind[p] == 'youtube#channel':
                self.thumbnailObjectList[p].setFixedWidth(144)
                (Image.open(BytesIO(requests.get(thumbnail).content))).resize((144, 144)).save(f"{temp.name}.bmp")
            else:
                self.thumbnailObjectList[p].setFixedWidth(256)
                (Image.open(BytesIO(requests.get(thumbnail).content))).resize((256, 144)).save(f"{temp.name}.bmp")

            # write extracted items to respective objects
            path = Path(f'{temp.name}.bmp').as_posix()
            self.thumbnailObjectList[p].setStyleSheet(
                baseThumbnailStyle + f"background-image: url({path}) 0 0 0 0 stretch stretch;" + "}")
            self.titleObjectList[p].setText(title)
            self.userObjectList[p].setText(user)
            self.titleObjectList[p].setToolTip(title)
            self.titleObjectList[p].setToolTipDuration(-1)
            print('item json ' + str(p) + ' loaded')

    def openVideoFunction(self, videoIndex):
        global kind
        global Id
        global searchResponseJSON
        global videoStreamURL
        global resolution
        mode = 'stream'

        # extract video and launch player
        if kind[videoIndex] == 'youtube#video':
            print('opening type ' + str(kind[videoIndex]) + ' with url ' + 'https://youtube.com/watch?v=' + str(
                Id[videoIndex]))
            if mode == 'stream':

                # get stream link
                if resolution == 'HD':
                    videoStreamURL = str(YouTube(
                        'https://youtube.com/watch?v=' + str(Id[videoIndex])).streams.get_highest_resolution().url)
                else:
                    try:
                        videoStreamURL = str(YouTube(
                            'https://youtube.com/watch?v=' + str(Id[videoIndex])).streams.get_lowest_resolution().url)
                    except Exception as e:
                        print(e)
                        return

                # launch video player
                print('launching video player with video stream from url @ ' + videoStreamURL)
                player(self).show()

            # DOWNLOAD FEATURE IS DEPRECATED AND ARCHIVED
            elif mode == 'download':
                print('creating temp file')
                temp = tempfile.NamedTemporaryFile(prefix='ytQtvideo', suffix='.mp4', delete=False)
                print('temp file created @ ' + Path(temp.name).as_posix())
                print('writing video steam to temp file')
                YouTube('https://youtube.com/watch?v=' + str(Id[videoIndex])).streams.get_highest_resolution().download(
                    filename=Path(temp.name).as_posix())
                print('launching video player with video file @ ' + Path(temp.name).as_posix())
                temp.close()
                self.hide()
                os.system('python player.py ' + base64.b64encode(Path(temp.name).as_posix().encode()).decode())
                self.show()
                os.remove(temp.name)
                print('removed temp file @ ' + Path(temp.name).as_posix())

        elif kind[videoIndex] == 'youtube#channel':

            # get upload playlist id (set parameters, get json apiData from api)
            searchParams = {'part': 'contentDetails', 'key': key, "id": channelId[videoIndex]}
            print('requesting channel api data')
            apiData = requests.get(youtubeURLRoot + 'youtube/v3/channels', params=searchParams)
            searchResponseJSON = json.loads(apiData.text)
            playlistId = searchResponseJSON['items'][0]['contentDetails']['relatedPlaylists'].get('uploads')
            print('channel uploads playlist id extracted')

            # get playlist items (set parameters, get json apiData from api)
            searchParams = {'part': 'snippet', 'key': key, "playlistId": playlistId, 'maxResults': '25'}
            print('requesting uploads playlist api data')
            apiData = requests.get(youtubeURLRoot + 'youtube/v3/playlistItems', params=searchParams)

            # read JSON from response
            searchResponseJSON = json.loads(apiData.text)
            print('uploads api data loaded')
            self.loadJSONFunction(True)

        elif kind[videoIndex] == 'youtube#playlist':

            # get playlist items (set parameters, get json apiData from api)
            searchParams = {'part': 'snippet', 'key': key, "playlistId": Id[videoIndex], 'maxResults': '25'}
            print('requesting uploads api data')
            apiData = requests.get(youtubeURLRoot + 'youtube/v3/playlistItems', params=searchParams)

            # read JSON from response
            searchResponseJSON = json.loads(apiData.text)
            print('uploads api data loaded')
            self.loadJSONFunction(True)

    def nextPageFunction(self):
        global currentPage
        global searchResponseJSON
        if searchResponseJSON == None:
            return

        # switch to next page
        if currentPage < 4:
            currentPage = currentPage + 1
            if currentPage == 4:
                self.nextPageButton.setStyleSheet(baseButtonStyle + "color: #404040};})\n")
            else:
                self.prevPageButton.setStyleSheet(baseButtonStyle + "color: #ffffff};})\n")
            self.loadJSONFunction(False)

    def prevPageFunction(self):
        global currentPage
        global searchResponseJSON

        # return to prevent crash if there are no items
        if searchResponseJSON == None:
            return

        # switch to previous page
        if currentPage > 0:
            currentPage = currentPage - 1
            if currentPage == 0:
                self.prevPageButton.setStyleSheet(baseButtonStyle + "color: #404040};})\n")
            else:
                self.nextPageButton.setStyleSheet(baseButtonStyle + "color: #ffffff};})\n")
            self.loadJSONFunction(False)


class player(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        global appPath
        super(player, self).__init__(parent)
        uic.loadUi(os.path.join(appPath, 'player.ui'), self)
        self.setWindowIcon(QtGui.QIcon('assets/ytQt.ico'))
        global videoStreamURL
        self.startVideoStream()

    def startVideoStream(self):
        global vlcMediaPlayer

        # start vlc instance
        self.vlcInstance = vlc.Instance(['--video-on-top', '--verbose=-1', '--repeat'])
        self.vlcMediaPlayer = self.vlcInstance.media_player_new()
        if platform.system() == "Linux":
            self.vlcMediaPlayer.set_xwindow(int(self.vlcContainerFrame.winId()))
        elif platform.system() == "Windows":
            self.vlcMediaPlayer.set_hwnd(int(self.vlcContainerFrame.winId()))
        self.media_path = videoStreamURL
        self.media = self.vlcInstance.media_new(self.media_path)
        self.vlcMediaPlayer.set_media(self.media)
        self.vlcMediaPlayer.play()

        # connect buttons
        self.fastforwardButton.clicked.connect(self.fastforward)
        self.rewindButton.clicked.connect(self.rewind)
        self.pauseButton.clicked.connect(self.pausePlay)
        self.fullscreenButton.clicked.connect(self.fullscreenToggle)

        # connect sliders
        self.volumeSlider.setValue(int(self.vlcMediaPlayer.audio_get_volume() / 10))
        self.videoSlider.sliderMoved.connect(self.setVideoProgress)
        self.volumeSlider.valueChanged.connect(self.setAudioLevel)

        # start ui update timer
        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.updateVideoSlider)
        self.timer.start()

    def pausePlay(self):
        if self.vlcMediaPlayer.is_playing():

            # pause player
            self.vlcMediaPlayer.pause()
            self.pauseButton.setText('⏵')
            self.is_paused = True
        else:

            # start player
            self.vlcMediaPlayer.play()
            self.pauseButton.setText('⏸︎')
            self.is_paused = False
        self.updateVideoSlider()

    def fullscreenToggle(self):
        if self.isFullScreen():

            # show normal
            self.showNormal()
            self.setStyleSheet("background-color: #1e2126;")
        else:

            # show fullscreen
            self.showFullScreen()
            self.setStyleSheet("background-color: #000000;")

    def closeEvent(self, event):

        # stop video player when player closes, temporary solution
        self.close()
        self.vlcMediaPlayer.stop()
        event.accept()

    def fastforward(self):

        # fast-forward 5s
        self.vlcMediaPlayer.set_time(self.vlcMediaPlayer.get_time() + 5000)
        self.updateVideoSlider()

    def rewind(self):

        # rewind 5s
        self.vlcMediaPlayer.set_time(self.vlcMediaPlayer.get_time() - 5000)
        self.updateVideoSlider()

    def setVideoProgress(self):

        # update the progress of the slider to the video
        self.vlcMediaPlayer.set_position(self.videoSlider.value() / 1000)

    def setAudioLevel(self):

        # update vlc volume to slider value
        self.vlcMediaPlayer.audio_set_volume(self.volumeSlider.value() * 10)

    def updateVideoSlider(self):
        # update vlc video progress to slider value
        self.videoSlider.setValue(int(self.vlcMediaPlayer.get_position() * 1000))

    def keyPressEvent(self, event: QKeyEvent):

        # ignore if held down
        if event.isAutoRepeat():
            return

        # pause 'spacebar'
        if event.key() == QtCore.Qt.Key.Key_Space or event.key() == QtCore.Qt.Key.Key_MediaTogglePlayPause:
            self.pausePlay()

        # fullscreen 'f'
        elif event.key() == QtCore.Qt.Key.Key_F or event.key() == QtCore.Qt.Key.Key_F11:
            self.fullscreenToggle()

        # volume + 'arrow_up'
        elif event.key() == QtCore.Qt.Key.Key_Up:
            if self.volumeSlider.value() <= 9:
                self.volumeSlider.setValue(self.volumeSlider.value() + 1)
            else:
                self.volumeSlider.setValue(10)
            self.vlcMediaPlayer.audio_set_volume(self.volumeSlider.value())

        # volume - 'arrow_down'
        elif event.key() == QtCore.Qt.Key.Key_Down:
            if self.volumeSlider.value() >= 1:
                self.volumeSlider.setValue(self.volumeSlider.value() - 1)
            else:
                self.volumeSlider.setValue(0)
            self.vlcMediaPlayer.audio_set_volume(self.volumeSlider.value())

        # fastforward 'arrow_right'
        elif event.key() == QtCore.Qt.Key.Key_Right:
            self.fastforward()

        # rewind 'arrow_left'
        elif event.key() == QtCore.Qt.Key.Key_Left:
            self.rewind()


# key = 'AIzaSyDuWZalLquMoISDybPsuOYs75cAeAEtEzo'
key = 'AIzaSyCDqJTmI3gkjv7-KfWQzo1jqad1HoUqOQc'
youtubeURLRoot = "https://youtube.googleapis.com/"
baseThumbnailStyle = ("QPushButton:hover{\n"
                      "border-radius: 12px;\n"
                      "border-width: 2px;\n"
                      "border-color: #74cbfc}\n"
                      "QPushButton:pressed{\n"
                      "border-width: 3px;\n"
                      "border-color: #e974fc;}\n"
                      "QPushButton{\n"
                      "color: rgb(0, 0, 0);\n"
                      "border-width: 1px;\n"
                      "border-style: solid;\n"
                      "border-radius: 25px;\n"
                      "border-color: #1E2126;\n"
                      "width: 144px;\n"
                      "height: 256px;\n"
                      "background-position: center;\n")
baseButtonStyle = ("QPushButton:hover{\n"
                   "border-radius: 5px;\n}"
                   "QPushButton:pressed {\n"
                   "border-color: #e974fc;\n"
                   "border-width: 3px}\n"
                   "QPushButton {\n"
                   "background-color: 4d4d4d;\n"
                   "border: 2px solid black;\n"
                   "border-color: #74cbfc;\n"
                   "border-radius: 20px;\n"
                   "text-align: center;\n"
                   "padding-bottom: 0px;\n")

global title
global user
global thumbnail
global searchResponseJSON
global videoStreamURL
global vlcMediaPlayer
global appPath
global resolution
global history
global historyIndex
history = []
historyIndex = -1
resolution = 'HD'
channelId = [None, None, None, None, None]
Id = [None, None, None, None, None]
kind = [None, None, None, None, None]
currentPage = 0
searchResponseJSON = None

if __name__ == '__main__':
    # initialization of the script
    app = QtWidgets.QApplication(sys.argv)
    window = Search()
    app.exec()
