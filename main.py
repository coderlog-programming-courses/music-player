from email.mime import application
import os.path, sys
from PyQt5 import QtWidgets, QtCore, QtGui
from db_worker import create_datebase, output_of_all_playlists
from playlist import playlist_output_in_the_form_of_a_letter
from window import Ui_MainWindow
from loguru import logger
from functools import partial


logger.add('python.log', format='{time} {level} {message}')


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
        Window.get_music(self, 1)

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

        self.get_playlists()
    
    def playlist_label_cliked(self, playlist_id, QMouseEvent):
        if self.past_playlist == None:
            self.past_playlist = playlist_id
            for i in range(len(self.list_playlists)):
                if playlist_id in self.list_playlists[i]:
                    self.list_playlists[i][1].setStyleSheet('color: #FF0000;')
                    break
        else:
            for i in range(len(self.list_playlists)):
                if self.past_playlist in self.list_playlists[i]:
                    self.list_playlists[i][1].setStyleSheet('color: #FFFFFF;')
                    break
            self.past_playlist = playlist_id
            for i in range(len(self.list_playlists)):
                if playlist_id in self.list_playlists[i]:
                    self.list_playlists[i][1].setStyleSheet('color: #FF0000;')
                    break


    def get_playlists(self):
        for i in reversed(range(self.ui.playlist_frame_layout.count())): 
            self.ui.playlist_frame_layout.itemAt(i).widget().setParent(None)

        playlists = output_of_all_playlists()[1:]
        self.list_playlists = []

        for i in range(len(playlists)):
            playlist_id = playlists[i][0]

            self.frame = QtWidgets.QFrame(self.ui.playlist_widget)
            self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
            self.frame.setMinimumSize(QtCore.QSize(0, 40))
            self.frame.setFrameShape(QtWidgets.QFrame.Box)
            self.frame.setLineWidth(0)
            self.frame.setObjectName("frame_in_playlist")

            self.label = QtWidgets.QLabel(playlists[i][1], self.frame)
            self.label.setGeometry(QtCore.QRect(10,2,264,36))
            if playlist_id == self.past_playlist: self.label.setStyleSheet('color: #FF0000')
            else: self.label.setStyleSheet('color: #FFFFFF')
            self.label.setFont(QtGui.QFont('Arial', 15))
            self.label.mousePressEvent = partial(Window.playlist_label_cliked, self, playlist_id)
            self.list_playlists.append([playlist_id, self.label])

            self.ui.playlist_frame_layout.addWidget(self.frame)
            
        self.space_frame = QtWidgets.QFrame(self.ui.playlist_widget)
        self.space_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.space_frame.setLineWidth(0)
        self.space_frame.setObjectName("space_frame_in_playlist")
        self.ui.playlist_frame_layout.addWidget(self.space_frame)


app = QtWidgets.QApplication([])
application = Window()
application.show()

sys.exit(app.exec())