# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wheelofjeopardy/gui/pyqt/ui_moderator_popup.ui'
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

class Ui_ModeratorPopup(object):
    def setupUi(self, ModeratorPopup):
        ModeratorPopup.setObjectName(_fromUtf8("ModeratorPopup"))
        ModeratorPopup.resize(515, 318)
        self.verticalLayout = QtGui.QVBoxLayout(ModeratorPopup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mainLabel = QtGui.QLabel(ModeratorPopup)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.mainLabel.setFont(font)
        self.mainLabel.setObjectName(_fromUtf8("mainLabel"))
        self.verticalLayout.addWidget(self.mainLabel)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.correctAnswerLabel = QtGui.QLabel(ModeratorPopup)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.correctAnswerLabel.setFont(font)
        self.correctAnswerLabel.setObjectName(_fromUtf8("correctAnswerLabel"))
        self.horizontalLayout_3.addWidget(self.correctAnswerLabel)
        self.correctAnswer = QtGui.QLabel(ModeratorPopup)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.correctAnswer.setFont(font)
        self.correctAnswer.setObjectName(_fromUtf8("correctAnswer"))
        self.horizontalLayout_3.addWidget(self.correctAnswer)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.playerAnswerLabel = QtGui.QLabel(ModeratorPopup)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.playerAnswerLabel.setFont(font)
        self.playerAnswerLabel.setObjectName(_fromUtf8("playerAnswerLabel"))
        self.horizontalLayout_4.addWidget(self.playerAnswerLabel)
        self.playerAnswer = QtGui.QLabel(ModeratorPopup)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.playerAnswer.setFont(font)
        self.playerAnswer.setObjectName(_fromUtf8("playerAnswer"))
        self.horizontalLayout_4.addWidget(self.playerAnswer)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.playerCorrectRadio = QtGui.QRadioButton(ModeratorPopup)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.playerCorrectRadio.setFont(font)
        self.playerCorrectRadio.setObjectName(_fromUtf8("playerCorrectRadio"))
        self.horizontalLayout.addWidget(self.playerCorrectRadio)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.playerIncorrectRadio = QtGui.QRadioButton(ModeratorPopup)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.playerIncorrectRadio.setFont(font)
        self.playerIncorrectRadio.setObjectName(_fromUtf8("playerIncorrectRadio"))
        self.horizontalLayout.addWidget(self.playerIncorrectRadio)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.okButton = QtGui.QPushButton(ModeratorPopup)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout_2.addWidget(self.okButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ModeratorPopup)
        QtCore.QMetaObject.connectSlotsByName(ModeratorPopup)

    def retranslateUi(self, ModeratorPopup):
        ModeratorPopup.setWindowTitle(_translate("ModeratorPopup", "Dialog", None))
        self.mainLabel.setText(_translate("ModeratorPopup", "Moderator: Is the player\'s answer correct?", None))
        self.correctAnswerLabel.setText(_translate("ModeratorPopup", "Correct Answer:", None))
        self.correctAnswer.setText(_translate("ModeratorPopup", "TextLabel", None))
        self.playerAnswerLabel.setText(_translate("ModeratorPopup", "Player\'s Answer:", None))
        self.playerAnswer.setText(_translate("ModeratorPopup", "TextLabel", None))
        self.playerCorrectRadio.setText(_translate("ModeratorPopup", "YES!", None))
        self.playerIncorrectRadio.setText(_translate("ModeratorPopup", "Definitely Not.", None))
        self.okButton.setText(_translate("ModeratorPopup", "OK", None))

