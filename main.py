from email.mime import application
import os.path, sys
from PyQt5 import QtWidgets, QtCore, QtGui
from db_worker import create_datebase, output_all_playlists
from playlist import playlist_output_form_letter
from cover_art_music_author import author_photo_name_music
from window import Ui_MainWindow
from loguru import logger
from functools import partial


logger.add('logs/player.log', format='{time} {level} {message}', rotation="10MB")


if os.path.exists('db.bin') != True: #Якщо файлу бази данних немає у папці
    create_datebase() #Запустить функцію, що створить його.


class Window(QtWidgets.QMainWindow):
    @logger.catch
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.music_button.clicked.connect(self.music_button_cliked)
        self.ui.playlist_button.clicked.connect(self.playlist_button_cliked)
        self.ui.playlist_frame.setVisible(False)
        self.past_playlist = None
        self.past_music = None
        self.list_playlist_musics = []
        self.list_musics = []
        Window.get_musics(self, 1, self.ui.music_frame_layout, 'music')
        Window.get_playlists(self)
        logger.info('start window')

    def music_button_cliked(self):
        self.ui.music_frame.setVisible(True)
        self.ui.playlist_frame.setVisible(False)

        music_icon = QtGui.QIcon()
        music_icon.addPixmap(QtGui.QPixmap("button_image/active_button_musics.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui.music_button.setIcon(music_icon)
        self.ui.music_button.setIconSize(QtCore.QSize(100, 30))

        playlist_icon = QtGui.QIcon()
        playlist_icon.addPixmap(QtGui.QPixmap("button_image/deactive_button_playlists.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui.playlist_button.setIcon(playlist_icon)
        self.ui.playlist_button.setIconSize(QtCore.QSize(100, 30))

        logger.info('music button cliked')

    def playlist_button_cliked(self):
        self.ui.music_frame.setVisible(False)
        self.ui.playlist_frame.setVisible(True)

        music_icon = QtGui.QIcon()
        music_icon.addPixmap(QtGui.QPixmap("button_image/deactive_button_musics.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui.music_button.setIcon(music_icon)
        self.ui.music_button.setIconSize(QtCore.QSize(100, 30))

        playlist_icon = QtGui.QIcon()
        playlist_icon.addPixmap(QtGui.QPixmap("button_image/active_button_playlists.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.ui.playlist_button.setIcon(playlist_icon)
        self.ui.playlist_button.setIconSize(QtCore.QSize(100, 30))

        logger.info('playlist button cliked')
    
    def playlist_label_cliked(self, playlist_id, QMouseEvent):
        if self.past_playlist == None:
            self.past_playlist = playlist_id
            for i in range(len(self.list_playlists)):
                if playlist_id == self.list_playlists[i][0]:
                    self.list_playlists[i][1].setStyleSheet('color:#FF0000;')
        else:
            for i in range(len(self.list_playlists)):
                if self.past_playlist == self.list_playlists[i][0]:
                    self.list_playlists[i][1].setStyleSheet('color:#FFFFFF;')
            self.past_playlist = playlist_id
            for i in range(len(self.list_playlists)):
                if playlist_id == self.list_playlists[i][0]:
                    self.list_playlists[i][1].setStyleSheet('color:#FF0000;')

        Window.get_musics(self, playlist_id, self.ui.playlist_frame_layout, 'playlist')

        logger.info('change playlist')

    def playlist_music_label_cliked(self, music_id, QMouseEvent):
        if self.past_music == None:
            self.past_music = music_id
            for i in range(len(self.list_playlist_musics)):
                if self.list_playlist_musics[i][0] == music_id:
                    self.list_playlist_musics[i][1].setStyleSheet('color:#FF0000;')
                    self.list_musics[i][2].setStyleSheet('color:#FF0000;')
        else:
            for i in range(len(self.list_playlist_musics)):
                if self.list_playlist_musics[i][0] == self.past_music:
                    self.list_playlist_musics[i][1].setStyleSheet('color:#FFFFFF;')
                    self.list_playlist_musics[i][2].setStyleSheet('color:#7D7373;')
            for i in range(len(self.list_musics)):
                if self.list_musics[i][0] == self.past_music:
                    self.list_musics[i][1].setStyleSheet('color:#FFFFFF;')
                    self.list_musics[i][2].setStyleSheet('color:#7D7373;')
            self.past_music = music_id
            for i in range(len(self.list_playlist_musics)):
                if self.list_playlist_musics[i][0] == music_id:
                    self.list_playlist_musics[i][1].setStyleSheet('color:#FF0000;')
                    self.list_playlist_musics[i][2].setStyleSheet('color:#FF0000;')

    def music_label_cliked(self, music_id, QMouseEvent):
        if self.past_music == None:
            self.past_music = music_id
            for i in range(len(self.list_musics)):
                if self.list_musics[i][0] == music_id:
                    self.list_musics[i][1].setStyleSheet('color:#FF0000;')
                    self.list_musics[i][2].setStyleSheet('color:#FF0000;')
        else:
            for i in range(len(self.list_musics)):
                if self.list_musics[i][0] == self.past_music:
                    self.list_musics[i][1].setStyleSheet('color:#FFFFFF;')
                    self.list_musics[i][2].setStyleSheet('color:#7D7373;')
            for i in range(len(self.list_playlist_musics)):
                if self.list_playlist_musics[i][0] == self.past_music:
                    self.list_playlist_musics[i][1].setStyleSheet('color:#FFFFFF;')
                    self.list_playlist_musics[i][2].setStyleSheet('color:#7D7373;')
            self.past_music = music_id
            for i in range(len(self.list_musics)):
                if self.list_musics[i][0] == music_id:
                    self.list_musics[i][1].setStyleSheet('color:#FF0000;')
                    self.list_musics[i][2].setStyleSheet('color:#FF0000;')

    def get_playlists(self):
        for i in reversed(range(self.ui.playlist_frame_layout.count())): 
            self.ui.playlist_frame_layout.itemAt(i).widget().setParent(None)

        playlists = output_all_playlists()[1:]
        self.list_playlists = []

        for i in range(len(playlists)):
            playlist_id = playlists[i][0]

            frame = QtWidgets.QFrame(self.ui.playlist_widget)
            frame.setMaximumSize(QtCore.QSize(16777215, 40))
            frame.setMinimumSize(QtCore.QSize(0, 40))
            frame.setFrameShape(QtWidgets.QFrame.Box)
            frame.setLineWidth(0)
            frame.setObjectName("frame_in_playlist")

            label = QtWidgets.QLabel(playlists[i][1], frame)
            label.setGeometry(QtCore.QRect(10,2,264,36))
            label.setStyleSheet('color: #FFFFFF')
            label.setFont(QtGui.QFont('Arial', 15))
            label.mousePressEvent = partial(Window.playlist_label_cliked, self, playlist_id)
            self.list_playlists.append([playlist_id, label])

            self.ui.playlist_frame_layout.addWidget(frame)
            
        space_frame = QtWidgets.QFrame(self.ui.playlist_widget)
        space_frame.setFrameShape(QtWidgets.QFrame.Box)
        space_frame.setLineWidth(0)
        space_frame.setObjectName("space_frame_in_playlist")
        self.ui.playlist_frame_layout.addWidget(space_frame)
    
    def get_musics(self, playlist_id, layout, frame_for_music):
        for i in reversed(range(layout.count())): 
            layout.itemAt(i).widget().setParent(None)

        musics_way = playlist_output_form_letter(playlist_id)[1:][0]
        musics = []
        for i in range(len(musics_way)):
            music = author_photo_name_music(musics_way[i][1])
            musics.append([musics_way[i][0], music[0], music[1]])
        if frame_for_music == 'playlist':
            self.list_playlist_musics = []
        else:
            self.list_musics = []

        for i in range(len(musics)):
            frame = QtWidgets.QFrame(self.ui.music_widget)
            frame.setMaximumSize(QtCore.QSize(16777215, 50))
            frame.setMinimumSize(QtCore.QSize(0, 50))
            frame.setFrameShape(QtWidgets.QFrame.Box)
            frame.setLineWidth(0)
            frame.setObjectName("frame_in_musics")

            label = QtWidgets.QLabel(musics[i][2], frame)
            label.setGeometry(QtCore.QRect(10,2,264,28))
            label.setStyleSheet('color: #FFFFFF')
            label.setFont(QtGui.QFont('Arial', 15))
            if frame_for_music == 'playlist':
                label.mousePressEvent = partial(Window.playlist_music_label_cliked, self, musics[i][0])
            else:
                label.mousePressEvent = partial(Window.music_label_cliked, self, musics[i][0])

            label_author = QtWidgets.QLabel(musics[i][1], frame)
            label_author.setGeometry(QtCore.QRect(10,30,264,20))
            label_author.setStyleSheet('color: #7D7373')
            label_author.setFont(QtGui.QFont('Arial', 12))
            label_author.setAlignment(QtCore.Qt.AlignTop)
            if frame_for_music == 'playlist':
                label.mousePressEvent = partial(Window.playlist_music_label_cliked, self, musics[i][0])
            else:
                label.mousePressEvent = partial(Window.music_label_cliked, self, musics[i][0])

            if frame_for_music == 'playlist':
                self.list_playlist_musics.append([musics[i][0], label, label_author])
            else:
                self.list_musics.append([musics[i][0], label, label_author])

            layout.addWidget(frame)

        space_frame = QtWidgets.QFrame(self.ui.music_widget)
        space_frame.setFrameShape(QtWidgets.QFrame.Box)
        space_frame.setLineWidth(0)
        space_frame.setObjectName("space_frame_in_musics")
        layout.addWidget(space_frame)


app = QtWidgets.QApplication([])
application = Window()
application.show()

sys.exit(app.exec())