import sys, os, time
from collections import OrderedDict

from PySide.QtGui import *
from PySide.QtCore import *


class Tmp_APP(QMainWindow):
    ''' '''

    def __init__(self):
        ''' '''
        super(Tmp_APP, self).__init__()
        self.groupboxes = OrderedDict()
        self.outputs = OrderedDict()
        self.inputs = OrderedDict()
        self.initUI()

    def initUI(self):
        ''' '''
        self.main_widget = QWidget()
        self.main_layout = QGridLayout(self.main_widget)

        generic_groupbox = QGroupBox('Groupbox Title')
        self.groupboxes['Results Display'] = generic_groupbox
        groupbox_layout = QVBoxLayout(generic_groupbox)
        self.main_layout.addWidget(generic_groupbox, 0, 0, 3, 3)

        # ADD WIDGITS TO LAYOUT HERE. DON'"'T FORGET TO ADD BEHAVIORS.
        
        self.setCentralWidget(self.main_widget)
        self.show()


def main():
    app = QApplication(sys.argv)
    scan_application = Tmp_APP()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
