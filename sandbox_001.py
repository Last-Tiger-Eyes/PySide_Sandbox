# proof of concept for passing in N keywords & arguments
'''
def foo(func_id='foo', **kwargs):
    print('func_id = {}'.format(func_id))
    for arg in kwargs:
        print('arg: {}\t\tkwargs[arg]: {}'.format(arg, kwargs[arg]))


def bar(func_id='bar', **kwargs):
    foo(func_id=func_id, **kwargs)


foo(func_id='foo', lamp='ridged', tablecloth='plaid')
bar(func_id='bar', ball='red', wall='brick')
'''

# proof of concept for connecting multiple things to one signal send.

import sys
from PySide.QtGui import *
from PySide.QtCore import *


# def baz(func):
#     func()


def main():
    # baz(func=lambda: print('it worked'))
    app = QApplication(sys.argv)
    bash = NSmash()
    sys.exit(app.exec_())


class NSmash(QMainWindow):
    def __init__(self):
        super(NSmash, self).__init__()
        self.initUI()

    def initUI(self):
        # SETUP MAIN LAYOUT FOR APP
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        # OUTPUT STUFF: ALWASY FIRST
        # make output layout & content
        output_layout = QHBoxLayout()
        text_display = QPlainTextEdit()
        text_display.setReadOnly(True)
        output_layout.addWidget(text_display)
        output_layout.addStretch()
        # put in groupbox
        box_display = QGroupBox('Output: display', self)
        box_display.setLayout(output_layout)

        # INPUT STUFF
        # make input layout & content
        input_layout = QVBoxLayout()
        # input_layout.addWidget(SayHelloButton())
        # input_layout.addWidget(SayGoodbyeButton())
        input_layout.addWidget(SayHelloButton(display_func=text_display.appendPlainText))
        input_layout.addWidget(SayGoodbyeButton(display_func=text_display.appendPlainText))
        input_layout.addStretch()
        # put in groupbox
        box_hiby = QGroupBox('Input: hi & bye', self)
        box_hiby.setLayout(input_layout)

        # BACK TO MAIN WIDGET & LAYOUT
        # Add input & output group widgets to layout
        main_layout.addWidget(box_hiby)
        main_layout.addWidget(box_display)
        main_layout.addStretch()
        #
        self.setCentralWidget(main_widget)
        # self.setLayout(main_layout)
        self.set_window_size()
        self.show()

    def set_window_size(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 3)
        # self.setWindowState(Qt.WindowMaximized)


class SayHelloButton(QPushButton):
    def __init__(self, parent=None, display_func=None):
        super(SayHelloButton, self).__init__(parent=parent, text='Say Hello!')
        if display_func:
            # print('display={}'.format(display_func))
            self.clicked.connect(lambda: display_func('Hello World!'))
        else:
            self.clicked.connect(lambda: print("Hello World!"))


class SayGoodbyeButton(QPushButton):
    def __init__(self, parent=None, display_func=None):
        super(SayGoodbyeButton, self).__init__(parent=parent, text='Say Goodbye!')
        if display_func:
            # print('display={}'.format(display_func))
            self.clicked.connect(lambda: display_func('Goodbye Cruel World!!!'))
        else:
            self.clicked.connect(lambda: print("Goodbye Cruel World!!!"))


if __name__ == "__main__":
    main()
