#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
from modules import conf
from modules import network

cat_emoticon = {}

cat_emoticon["welcome"] = """
             ∧＿∧         ／￣￣￣￣￣￣￣￣
            （  ´∀｀)  ＜    Welcome!
         /           |     ＼    I'm your cat of
        /            .|　    ＼    the day!
       / "⌒ヽ  |.ｲ |           ＼＿＿＿＿＿＿＿＿
 ＿＿ |     .ノ | || |＿＿
     ノく＿＿つ∪∪      ＼
  ＿（（＿＿＿＿＿＿＿＿＼
 ￣￣ヽつ￣￣￣￣￣￣ | |￣
        ^ ＿＿＿＿＿
      /   I'm fuzzy.  ＼
       ＼＿＿＿＿＿＿/

"""

cat_emoticon["connection_error"] = """
             ∧＿∧         ／￣￣￣￣￣￣￣￣
            （  ´∀｀)  ＜    Connection Failure!
         /           |     ＼    Check for network
        /            .|　    ＼    connection!
       / "⌒ヽ  |.ｲ |           ＼＿＿＿＿＿＿＿＿
 ＿＿ |     .ノ | || |＿＿
     ノく＿＿つ∪∪      ＼
  ＿（（＿＿＿＿＿＿＿＿＼
 ￣￣ヽつ￣￣￣￣￣￣ | |￣
        ^ ＿＿＿＿＿
      /   I'm fuzzy.  ＼
       ＼＿＿＿＿＿＿/

"""

cat_emoticon["login_error"] = """
             ∧＿∧         ／￣￣￣￣￣￣￣￣
            （  ´∀｀)  ＜    Log-in Failure!
         /           |     ＼    Check for ID ||
        /            .|　    ＼    password!
       / "⌒ヽ  |.ｲ |           ＼＿＿＿＿＿＿＿＿
 ＿＿ |     .ノ | || |＿＿
     ノく＿＿つ∪∪      ＼
  ＿（（＿＿＿＿＿＿＿＿＼
 ￣￣ヽつ￣￣￣￣￣￣ | |￣
        ^ ＿＿＿＿＿
      /   I'm fuzzy.  ＼
       ＼＿＿＿＿＿＿/

"""

cat_emoticon["complete"] = """
             ∧＿∧         ／￣￣￣￣￣￣￣￣
            （  ´∀｀)  ＜    Process complete!
         /           |     ＼    You did the right thing.
        /            .|　    ＼    He deserved more views.
       / "⌒ヽ  |.ｲ |           ＼＿＿＿＿＿＿＿＿
 ＿＿ |     .ノ | || |＿＿
     ノく＿＿つ∪∪      ＼
  ＿（（＿＿＿＿＿＿＿＿＼
 ￣￣ヽつ￣￣￣￣￣￣ | |￣
        ^ ＿＿＿＿＿
      /   I'm fuzzy.  ＼
       ＼＿＿＿＿＿＿/

"""

cat_emoticon["counting"] = """
             ∧＿∧         ／￣￣￣￣￣￣￣￣
            （  ´∀｀)  ＜    Processing ...
         /           |     ＼    ? / ? ...
        /            .|　    ＼    Please wait
       / "⌒ヽ  |.ｲ |           ＼＿＿＿＿＿＿＿＿
 ＿＿ |     .ノ | || |＿＿
     ノく＿＿つ∪∪      ＼
  ＿（（＿＿＿＿＿＿＿＿＼
 ￣￣ヽつ￣￣￣￣￣￣ | |￣
        ^ ＿＿＿＿＿
      /   I'm fuzzy.  ＼
       ＼＿＿＿＿＿＿/

"""


class MainFrame(QtGui.QWidget):

    # POST method variables
    data = {"usr_id" : "",
            "usr_pwd" : ""}

    # GET method variables
    headers = {'Referer' : conf.referer}

    pools = 1
    interval = 1
    view_count = 0

    # gui-variables
    _btn = {}
    _spinbox = {}
    _title = {}
    _textbox = {}

    def __init__(self, master=None):
        super(MainFrame, self).__init__()
        QtCore.pyqtSignal(int)

        self.grid = QtGui.QGridLayout()

        self.set_title()
        self.set_textbox()
        self.set_spinbox()
        self.set_button()
        self.add_widget()

        self.connect_activity()

        self.setLayout(self.grid)
        self.show()


    def add_widget(self):
        self.grid.addWidget(self._title["id"], 0, 0)
        self.grid.addWidget(self._title["pwd"], 1, 0)

        self.grid.addWidget(self._textbox["id"], 0, 1, 1, 3)
        self.grid.addWidget(self._textbox["pwd"], 1, 1, 1, 3)

        self.grid.addWidget(self._title["interval"], 2, 0)
        self.grid.addWidget(self._title["cnt"], 3, 0)

        self.grid.addWidget(self._spinbox["interval"], 2, 1)
        self.grid.addWidget(self._spinbox["cnt"], 3, 1)

        self.grid.addWidget(self._title["pool"], 2, 2)
        self.grid.addWidget(self._spinbox["pool"], 2, 3)

        self.grid.addWidget(self._btn["run"], 3, 2, 1, 2)

        self.grid.addWidget(self._textbox["status"], 4, 0, 5, 4)


    def connect_activity(self):
        self._spinbox["interval"].valueChanged.connect(self.update_interval)
        self._spinbox["cnt"].valueChanged.connect(self.update_view_count)
        self._spinbox["pool"].valueChanged.connect(self.update_pool_number)

        self._textbox["id"].textChanged[str].connect(self.update_id)
        self._textbox["pwd"].textChanged[str].connect(self.update_pwd)

        self._btn["run"].clicked.connect(self.run)


    def set_textbox(self):
        self._textbox["id"] = QtGui.QLineEdit(self)
        self._textbox["pwd"] = QtGui.QLineEdit(self)
        self._textbox["pwd"].setEchoMode(QtGui.QLineEdit.Password)

        self._textbox["status"] = QtGui.QTextEdit(self)
        self._textbox["status"].setReadOnly(True)
        self._textbox["status"].setLineWrapMode(QtGui.QTextEdit.NoWrap)

        if network.check_network_connection():
            self._textbox["status"].setPlainText(cat_emoticon["welcome"])
        else:
            self._textbox["status"].setPlainText(cat_emoticon["connection_error"])
        self._textbox["status"].moveCursor(QtGui.QTextCursor.Start)


    def set_title(self):
        self.setWindowTitle("Eclass' Got Talent")

        self._title["id"] = QtGui.QLabel("Id: ")
        self._title["id"].setStyleSheet("font: bold")
        self._title["id"].setAlignment(QtCore.Qt.AlignCenter)

        self._title["pwd"] = QtGui.QLabel("Pwd: ")
        self._title["pwd"].setStyleSheet("font: bold")
        self._title["pwd"].setAlignment(QtCore.Qt.AlignCenter)

        self._title["interval"] = QtGui.QLabel("Interval (sec): ")
        self._title["interval"].setStyleSheet("font: bold")
        self._title["interval"].setAlignment(QtCore.Qt.AlignCenter)

        self._title["cnt"] = QtGui.QLabel("View counts: ")
        self._title["cnt"].setStyleSheet("font: bold")
        self._title["cnt"].setAlignment(QtCore.Qt.AlignCenter)

        self._title["pool"] = QtGui.QLabel("Pools : ")
        self._title["pool"].setStyleSheet("font: bold")
        self._title["pool"].setAlignment(QtCore.Qt.AlignCenter)


    def set_button(self):
        self._btn["run"] = QtGui.QPushButton("Let him shine", self)
        self._btn["run"].setStyleSheet("font: bold")


    def set_spinbox(self):
        self._spinbox["interval"] = QtGui.QSpinBox()
        self._spinbox["interval"].setRange(0, 100)
        self._spinbox["interval"].setSingleStep(1)
        self._spinbox["interval"].setValue(1)

        self._spinbox["cnt"] = QtGui.QSpinBox()
        self._spinbox["cnt"].setRange(0, 9999)
        self._spinbox["cnt"].setSingleStep(1)
        self._spinbox["cnt"].setValue(0)

        self._spinbox["pool"] = QtGui.QSpinBox()
        self._spinbox["pool"].setRange(0, 10)
        self._spinbox["pool"].setSingleStep(1)
        self._spinbox["pool"].setValue(1)


    def update_pool_number(self, value):
        self.pools = value


    def update_view_count(self, value):
        self.view_count = value


    def update_interval(self, value):
        self.interval = value


    def update_id(self, text):
        self.data["usr_id"] = text


    def update_pwd(self, text):
        self.data["usr_pwd"] = text


    def run(self):
        import time

        if not network.check_network_connection():
            self._textbox["status"].setPlainText(cat_emoticon["connection_error"])
            return

        cookie = network.authorize_session(self.data, self.headers)

        if len(cookie) == 0:
            self._textbox["status"].setPlainText(cat_emoticon["login_error"])
            return
        else:
            """
            cat_emoticon["counting"].replace("?", "0", 1)
            cat_emoticon["counting"].replace("?", str(self.view_count), 1)
            self._textbox["status"].setPlainText(cat_emoticon["counting"])
            """

            for i in range(self.view_count):
                network.request_lecture(cookie, self.interval)

        self._textbox["status"].setPlainText(cat_emoticon["complete"])
