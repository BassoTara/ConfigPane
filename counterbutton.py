# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QBoxLayout, QWidget
from observable import Observable

class CounterButton(QPushButton):
    '''Simple button widget that counts number of times clicked.'''
    def __init__(self, initval=0, **kwargs):
        super().__init__(**kwargs)
        self.counter = Observable(0)
        self.counter.observe(self.counterChanged)
        self.counter.value = initval

    def mouseReleaseEvent(self, event):
        self.counter.value = self.counter.value + 1
        super().mouseReleaseEvent(event)

    def counterChanged(self, newval):
        self.setText('Clicks: {}'.format(self.counter.value))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = QMainWindow()
    widget = QWidget()
    layout = QBoxLayout(QBoxLayout.TopToBottom)

    # Set the layout for our widget to the vbox.
    widget.setLayout(layout)
    window.setCentralWidget(widget)
    
    buttons = [CounterButton() for i in range(5)]
    for b in buttons:
        layout.addWidget(b)

    window.show()
    app.exec_()