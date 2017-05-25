import sys, os, time
from collections import OrderedDict

from PySide.QtGui import *
from PySide.QtCore import *


class Tmp_APP(QMainWindow):
    ''' '''

    def __init__(self):
        ''' '''
        super().__init__()
        self.groupboxes = OrderedDict()
        self.outputs = OrderedDict()
        self.inputs = OrderedDict()
        self.initUI()

    def initUI(self):
        ''' '''
        self.main_widget = QWidget()
        self.main_layout = QGridLayout(self.main_widget)

        display_groupbox = QGroupBox('Results Display')
        self.groupboxes['Results Display'] = display_groupbox
        display_layout = QVBoxLayout(display_groupbox)
        self.main_layout.addWidget(display_groupbox, 0, 0, 3, 3)

        display_widget = QTextEdit()
        display_widget.setReadOnly(True)
        self.outputs['results text box'] = display_widget
        display_layout.addWidget(display_widget)

        hello_btn = QPushButton("Hello!")
        hello_btn.clicked.connect(lambda: self.output_hello('Hello!'))
        self.main_layout.addWidget(hello_btn, 4, 0, 1, 1)

        da_list = QListWidget()
        da_list.addItems(['None', 'one', 'two', 'three'])
        da_list.setSelectionMode(QAbstractItemView.MultiSelection)
        self.inputs['da list'] = da_list
        self.main_layout.addWidget(da_list, 5, 0)

        clear_btn = QPushButton("Clear Selections")
        clear_btn.clicked.connect(self.clear_selections)
        self.main_layout.addWidget(clear_btn, 4, 1, 1, 1)

        self.setCentralWidget(self.main_widget)
        self.show()

    def output_hello(self, output_str):
        self.outputs['results text box'].clear()
        more = self.inputs['da list'].selectedItems()
        for m in more:
            output_str += m.text()
            # output_str += ' '+str(m)
        self.outputs['results text box'].append(output_str)

    def clear_selections(self):
        for item in self.inputs['da list'].selectedItems():
            item.setSelected(False)


def main():
    app = QApplication(sys.argv)
    scan_application = Tmp_APP()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
