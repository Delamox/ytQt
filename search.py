import sys
import base64
import json
import os
import platform
import tempfile
from io import BytesIO
from pathlib import Path

import requests
from PIL import Image
from PyQt6 import QtCore, QtGui, QtWidgets, uic
import vlc
from pytube import YouTube

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

global title
global user
global thumbnail
global searchResponseJSON
global videoStreamURL
global vlcMediaPlayer
channelId = [None, None, None, None, None]
Id = [None, None, None, None, None]
kind = [None, None, None, None, None]
currentPage = 0


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('assets/search.ui', self)
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

        # set the thumbnail background to init style
        path = ''
        self.thumbnailButton1.setStyleSheet(
            baseThumbnailStyle + f"background-image: url({path}) 0 0 0 0 stretch stretch;" + "}")
        self.thumbnailButton2.setStyleSheet(
            baseThumbnailStyle + f"background-image: url({path}) 0 0 0 0 stretch stretch;" + "}")
        self.thumbnailButton3.setStyleSheet(
            baseThumbnailStyle + f"background-image: url({path}) 0 0 0 0 stretch stretch;" + "}")
        self.thumbnailButton4.setStyleSheet(
            baseThumbnailStyle + f"background-image: url({path}) 0 0 0 0 stretch stretch;" + "}")
        self.thumbnailButton5.setStyleSheet(
            baseThumbnailStyle + f"background-image: url({path}) 0 0 0 0 stretch stretch;" + "}")

        # link the thumbnail presses to the openVideoFunction with the index of the button
        self.thumbnailButton1.clicked.connect(lambda: self.openVideoFunction(0))
        self.thumbnailButton2.clicked.connect(lambda: self.openVideoFunction(1))
        self.thumbnailButton3.clicked.connect(lambda: self.openVideoFunction(2))
        self.thumbnailButton4.clicked.connect(lambda: self.openVideoFunction(3))
        self.thumbnailButton5.clicked.connect(lambda: self.openVideoFunction(4))

        return

    def searchYoutubeFunction(self):
        # init
        global seachResponseJSON
        global apiData
        self.searchBar.clearFocus()

        # set parameters, get json apiData from api
        userSearchQuery = self.searchBar.text()
        searchParams = {'part': 'snippet', 'key': key, "q": userSearchQuery, "maxResults": "25"}
        print('requesting search api data')
        apiData = requests.get(youtubeURLRoot + 'youtube/v3/search', params=searchParams)
        # searchResponse = requests.get('https://files.catbox.moe/7j4a26.json')

        # read json from response
        seachResponseJSON = json.loads(apiData.text)
        print('search api data loaded')

        # call function to load json into UI
        self.loadJSONFunction()

    def loadJSONFunction(self):
        # init
        global currentPage
        global seachResponseJSON
        global title
        global user
        global thumbnail
        global kind
        global Id
        print('switching to page ' + str(currentPage))

        # loop over videos and load respective JSON
        print('loading item json')
        for i in range(0 + (currentPage * 5), 5 + (currentPage * 5)):

            # 'p' is the index of the item in the JSON, for every page, 5 is added. 'i' only loops from 1-5
            p = i - (currentPage * 5)

            # extract specific items from JSON
            title = seachResponseJSON['items'][i]['snippet'].get('title')
            user = seachResponseJSON['items'][i]['snippet'].get('channelTitle')
            thumbnail = seachResponseJSON['items'][i]['snippet']['thumbnails']['medium'].get('url')
            channelId[p] = seachResponseJSON['items'][i]['snippet'].get('channelId')

            # set kind and ID of video, yt has fuzzy consistency sadly

            # playlist item
            if seachResponseJSON['items'][i].get('kind') == 'youtube#playlistItem':
                kind[p] = 'youtube#video'
                Id[p] = seachResponseJSON['items'][i]['snippet']['resourceId'].get('videoId')
            # playlist
            elif seachResponseJSON['items'][i]['id'].get('kind') == 'youtube#playlist':
                kind[p] = seachResponseJSON['items'][i]['id'].get('kind')
                Id[p] = seachResponseJSON['items'][i]['id'].get('playlistId')
            # video
            else:
                kind[p] = seachResponseJSON['items'][i]['id'].get('kind')
                Id[p] = seachResponseJSON['items'][i]['id'].get('videoId')

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

        print('item json loaded')
    
    def openVideoFunction(self, videoIndex):
        # init
        global kind
        global Id
        global seachResponseJSON
        global videoStreamURL
        mode = 'stream'

        if kind[videoIndex] == 'youtube#video':
            print('opening type ' + str(kind[videoIndex]) + ' with url ' + 'https://youtube.com/watch?v=' + str(Id[videoIndex]))
            if mode == 'stream':

                # get stream link
                videoStreamURL = str(YouTube('https://youtube.com/watch?v=' + str(Id[videoIndex])).streams.get_highest_resolution().url)

                # launch video player
                print('launching video player with video stream from url @ ' + videoStreamURL)
                player(self).show()
                print('closing video stream')

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
            seachResponseJSON = json.loads(apiData.text)
            playlistId = seachResponseJSON['items'][0]['contentDetails']['relatedPlaylists'].get('uploads')
            print('channel uploads playlist id extracted')

            # get playlist items (set parameters, get json apiData from api)
            searchParams = {'part': 'snippet', 'key': key, "playlistId": playlistId, 'maxResults': '25'}
            print('requesting uploads playlist api data')
            apiData = requests.get(youtubeURLRoot + 'youtube/v3/playlistItems', params=searchParams)

            # read JSON from response
            seachResponseJSON = json.loads(apiData.text)
            print('uploads api data loaded')
            self.loadJSONFunction()

        elif kind[videoIndex] == 'youtube#playlist':

            # get playlist items (set parameters, get json apiData from api)
            searchParams = {'part': 'snippet', 'key': key, "playlistId": Id[videoIndex], 'maxResults': '25'}
            print('requesting uploads api data')
            apiData = requests.get(youtubeURLRoot + 'youtube/v3/playlistItems', params=searchParams)

            # read JSON from response
            seachResponseJSON = json.loads(apiData.text)
            print('uploads api data loaded')
            self.loadJSONFunction()

    def nextPageFunction(self):
        global currentPage
        if currentPage < 4:
            currentPage = currentPage + 1
            self.loadJSONFunction()

    def prevPageFunction(self):
        global currentPage
        if currentPage > 0:
            currentPage = currentPage - 1
            self.loadJSONFunction()

class player(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(player, self).__init__(parent)
        uic.loadUi('assets/player.ui', self)
        global videoStreamURL
        self.startVideoStream()

    def startVideoStream(self):
        global vlcMediaPlayer
        self.vlcInstance = vlc.Instance(['--video-on-top', '--verbose=-1'])
        self.vlcMediaPlayer = self.vlcInstance.media_player_new()
        if platform.system() == "Linux":
            self.vlcMediaPlayer.set_xwindow(int(self.vlcContainerFrame.winId()))
        elif platform.system() == "Windows":
            self.vlcMediaPlayer.set_hwnd(int(self.vlcContainerFrame.winId()))
        self.media_path = videoStreamURL
        self.media = self.vlcInstance.media_new(self.media_path)
        self.vlcMediaPlayer.set_media(self.media)
        self.vlcMediaPlayer.play()

        self.fastforwardButton.clicked.connect(self.fastforward)
        self.rewindButton.clicked.connect(self.rewind)
        self.pauseButton.clicked.connect(self.pausePlay)
        self.fullscreenButton.clicked.connect(self.fullscreenToggle)

        self.volumeSlider.setValue(int(self.vlcMediaPlayer.audio_get_volume()/10))
        self.videoSlider.sliderMoved.connect(self.setVideoProgress)
        self.volumeSlider.valueChanged.connect(self.setAudioLevel)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.updateVideoSlider)
        self.timer.start()

    def pausePlay(self):
        if self.vlcMediaPlayer.is_playing():
            self.vlcMediaPlayer.pause()
            self.pauseButton.setText('⏵')
            self.is_paused = True
        else:
            self.vlcMediaPlayer.play()
            self.pauseButton.setText('⏸︎')
            self.is_paused = False
        self.updateVideoSlider()

    def fullscreenToggle(self):
        if self.isFullScreen() == True:
            self.showNormal()
            self.setStyleSheet("background-color: #1e2126;")
        else:
            self.showFullScreen()
            self.setStyleSheet("background-color: #000000;")

    def closeEvent(self, event):
        self.close()
        self.vlcMediaPlayer.stop()
        event.accept()

    def fastforward(self):
        self.vlcMediaPlayer.set_time(self.vlcMediaPlayer.get_time() + 5000)
        self.updateVideoSlider()

    def rewind(self):
        self.vlcMediaPlayer.set_time(self.vlcMediaPlayer.get_time() - 5000)
        self.updateVideoSlider()

    def setVideoProgress(self):
        self.vlcMediaPlayer.set_position(self.videoSlider.value() / 1000)

    def setAudioLevel(self):
        self.vlcMediaPlayer.audio_set_volume(self.volumeSlider.value() * 10)

    def updateVideoSlider(self):
        self.videoSlider.setValue(int(self.vlcMediaPlayer.get_position() * 1000))

    def keyPressEvent(self, e):
        if e.isAutoRepeat():
            return
        if str(e.key()) == '32':
            self.pausePlay()
            # self.fullscreentoggle()
        elif str(e.key()) == '16777235':
            if self.volumeSlider.value() <= 9:
                self.volumeSlider.setValue(self.volumeSlider.value() + 1)
            else:
                self.volumeSlider.setValue(10)
            self.vlcMediaPlayer.audio_set_volume(self.volumeSlider.value())
        elif str(e.key()) == '16777237':
            if self.volumeSlider.value() >= 10:
                self.volumeSlider.setValue(self.volumeSlider.value() - 1)
            else:
                self.volumeSlider.setValue(0)
            self.vlcMediaPlayer.audio_set_volume(self.volumeSlider.value())
        elif str(e.key()) == '16777236':
            self.fastforward()
        elif str(e.key()) == '16777234':
            self.rewind()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec()
