# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/user/mlink/pycode/tokenPopup.ui'
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

class Ui_tokenDialog(object):
    def setupUi(self, tokenDialog):
        tokenDialog.setObjectName(_fromUtf8("tokenDialog"))
        tokenDialog.resize(526, 239)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(tokenDialog)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.everythingLayout = QtGui.QVBoxLayout()
        self.everythingLayout.setObjectName(_fromUtf8("everythingLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(tokenDialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.playerLabel = QtGui.QLabel(tokenDialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.playerLabel.setFont(font)
        self.playerLabel.setObjectName(_fromUtf8("playerLabel"))
        self.horizontalLayout_2.addWidget(self.playerLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.everythingLayout.addLayout(self.horizontalLayout_2)
        self.question = QtGui.QLabel(tokenDialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.question.setFont(font)
        self.question.setObjectName(_fromUtf8("question"))
        self.everythingLayout.addWidget(self.question)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.useTokenButton = QtGui.QPushButton(tokenDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.useTokenButton.sizePolicy().hasHeightForWidth())
        self.useTokenButton.setSizePolicy(sizePolicy)
        self.useTokenButton.setMinimumSize(QtCore.QSize(0, 32))
        self.useTokenButton.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.useTokenButton.setFont(font)
        self.useTokenButton.setObjectName(_fromUtf8("useTokenButton"))
        self.horizontalLayout.addWidget(self.useTokenButton)
        self.denyTokenButton = QtGui.QPushButton(tokenDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.denyTokenButton.sizePolicy().hasHeightForWidth())
        self.denyTokenButton.setSizePolicy(sizePolicy)
        self.denyTokenButton.setMinimumSize(QtCore.QSize(0, 32))
        self.denyTokenButton.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.denyTokenButton.setFont(font)
        self.denyTokenButton.setObjectName(_fromUtf8("denyTokenButton"))
        self.horizontalLayout.addWidget(self.denyTokenButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.everythingLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.everythingLayout)

        self.retranslateUi(tokenDialog)
        QtCore.QMetaObject.connectSlotsByName(tokenDialog)

    def retranslateUi(self, tokenDialog):
        tokenDialog.setWindowTitle(_translate("tokenDialog", "Dialog", None))
        self.label.setText(_translate("tokenDialog", "Player:", None))
        self.playerLabel.setText(_translate("tokenDialog", "TextLabel", None))
        self.question.setText(_translate("tokenDialog", "You have an available token. Would you like to use it?", None))
        self.useTokenButton.setText(_translate("tokenDialog", "YES!", None))
        self.denyTokenButton.setText(_translate("tokenDialog", "No Thanks", None))

