import sys
import base64
import json
import os
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

        self.searchButton.clicked.connect(self.searchYoutubeFunction)
        self.searchBar.returnPressed.connect(self.searchYoutubeFunction)

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
        global Ida
        global seachResponseJSON
        mode = 'stream'

        if kind[videoIndex] == 'youtube#video':
            print('opening type ' + str(kind[videoIndex]) + ' with url ' + 'https://youtube.com/watch?v=' + str(Id[videoIndex]))
            if mode == 'stream':

                # get stream link
                videoStreamLink = str(YouTube('https://youtube.com/watch?v=' + str(Id[videoIndex])).streams.get_highest_resolution().url)

                # launch video player
                print('launching video player with video stream from url @ ' + videoStreamLink)
                self.hide()
                os.system('python deprecated/player.py ' + base64.b64encode(videoStreamLink.encode()).decode())
                self.show()
                print('closing video stream')

            # DOWNLOAD FEATURE DEPRECATED AND ARCHIVED
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


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()