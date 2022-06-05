import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from maps import map

def locshow():
    map()
    app = QApplication(sys.argv)
    web = QWebEngineView()
    web.setWindowTitle("GARBAGE COLLECTORS")
    web.load(QUrl("C:/Users/DELL/Documents/VS/HACKATHONS/SCRAPATROL/map.html"))
    web.resize(360,640)
    web.show()
    app.exec_()
#locshow()