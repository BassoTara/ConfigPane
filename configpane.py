# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QLabel
from PyQt5.QtGui import QIntValidator

class ConfigPane(QGridLayout):
    '''Panel of configuration options. Buggy and not very featureful.'''
    def __init__(self, params, on_configure, **kwargs):
        '''The constructor takes a list of integer params of the form (NAME, DEFAULT).'''
        super().__init__(**kwargs)
        self._textinputs = {}

        # Iterate over all config parameters.
        for (i, (p, d)) in enumerate(params):
            # Make the label and add it.
            label = QLabel(text=p)
            self.addWidget(label, i, 0)
            
            # Save the textinput in a local dict so we can recover it by parameter *name*.
            self._textinputs[p] = QLineEdit(text=str(d))
            self._textinputs[p].setValidator(QIntValidator())
            self._textinputs[p].textChanged.connect(on_configure)
            self.addWidget(self._textinputs[p], i, 1)

    # This is a simple interface to let us get parameters by *name*
    # from outside this class.
    def get_param(self, p):
        '''Return the configuration parameter from the textinput with label p.'''
        return int(self._textinputs[p].text())