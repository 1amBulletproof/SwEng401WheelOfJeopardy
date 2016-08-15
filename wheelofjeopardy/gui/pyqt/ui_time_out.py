# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wheelofjeopardy/gui/pyqt/ui_time_out.ui'
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

class Ui_TimeOutPopup(object):
    def setupUi(self, TimeOutPopup):
        TimeOutPopup.setObjectName(_fromUtf8("TimeOutPopup"))
        TimeOutPopup.resize(526, 221)
        self.verticalLayout = QtGui.QVBoxLayout(TimeOutPopup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(TimeOutPopup)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 56, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(TimeOutPopup)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.answerLabel = QtGui.QLabel(TimeOutPopup)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.answerLabel.setFont(font)
        self.answerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.answerLabel.setObjectName(_fromUtf8("answerLabel"))
        self.horizontalLayout_3.addWidget(self.answerLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.okButton = QtGui.QPushButton(TimeOutPopup)
        self.okButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout_2.addWidget(self.okButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(TimeOutPopup)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), TimeOutPopup.close)
        QtCore.QMetaObject.connectSlotsByName(TimeOutPopup)

    def retranslateUi(self, TimeOutPopup):
        TimeOutPopup.setWindowTitle(_translate("TimeOutPopup", "Dialog", None))
        self.label_2.setText(_translate("TimeOutPopup", "the timer ran out! :(", None))
        self.label_3.setText(_translate("TimeOutPopup", "correct answer: ", None))
        self.answerLabel.setText(_translate("TimeOutPopup", "TextLabel", None))
        self.okButton.setText(_translate("TimeOutPopup", "OK :(", None))

