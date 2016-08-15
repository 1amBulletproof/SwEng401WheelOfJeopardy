# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wheelofjeopardy/gui/pyqt/ui_round_game_over.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_RoundGamePopup(object):
    def setupUi(self, RoundGamePopup):
        RoundGamePopup.setObjectName(_fromUtf8("RoundGamePopup"))
        RoundGamePopup.resize(526, 221)
        self.verticalLayout = QtGui.QVBoxLayout(RoundGamePopup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.roundOrGameLabel = QtGui.QLabel(RoundGamePopup)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.roundOrGameLabel.setFont(font)
        self.roundOrGameLabel.setObjectName(_fromUtf8("roundOrGameLabel"))
        self.horizontalLayout.addWidget(self.roundOrGameLabel)
        self.label_2 = QtGui.QLabel(RoundGamePopup)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 60, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.winnerLabel = QtGui.QLabel(RoundGamePopup)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.winnerLabel.setFont(font)
        self.winnerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.winnerLabel.setObjectName(_fromUtf8("winnerLabel"))
        self.verticalLayout.addWidget(self.winnerLabel)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.okButton = QtGui.QPushButton(RoundGamePopup)
        self.okButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout_2.addWidget(self.okButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(RoundGamePopup)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), RoundGamePopup.close)
        QtCore.QMetaObject.connectSlotsByName(RoundGamePopup)

    def retranslateUi(self, RoundGamePopup):
        RoundGamePopup.setWindowTitle(_translate("RoundGamePopup", "Dialog", None))
        self.roundOrGameLabel.setText(_translate("RoundGamePopup", "TextLabel", None))
        self.label_2.setText(_translate("RoundGamePopup", "Has ended!", None))
        self.winnerLabel.setText(_translate("RoundGamePopup", "TextLabel", None))
        self.okButton.setText(_translate("RoundGamePopup", "OK", None))

