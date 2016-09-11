#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import QApplication
import modules.gui as gui

def main():
    app = QApplication(sys.argv)
    fig = gui.MainFrame()
    app.exec_()

if __name__ == "__main__":
    main()
