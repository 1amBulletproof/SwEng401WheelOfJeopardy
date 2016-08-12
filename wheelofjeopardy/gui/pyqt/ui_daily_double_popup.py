# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wheelofjeopardy/gui/pyqt/ui_daily_double_popup.ui'
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

class Ui_DailyDoublePopup(object):
    def setupUi(self, DailyDoublePopup):
        DailyDoublePopup.setObjectName(_fromUtf8("DailyDoublePopup"))
        DailyDoublePopup.resize(422, 239)
        self.verticalLayout = QtGui.QVBoxLayout(DailyDoublePopup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(DailyDoublePopup)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(DailyDoublePopup)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.maxLabel = QtGui.QLabel(DailyDoublePopup)
        self.maxLabel.setObjectName(_fromUtf8("maxLabel"))
        self.horizontalLayout_3.addWidget(self.maxLabel)
        self.maxLabelValue = QtGui.QLabel(DailyDoublePopup)
        self.maxLabelValue.setObjectName(_fromUtf8("maxLabelValue"))
        self.horizontalLayout_3.addWidget(self.maxLabelValue)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.minLabel = QtGui.QLabel(DailyDoublePopup)
        self.minLabel.setObjectName(_fromUtf8("minLabel"))
        self.horizontalLayout_3.addWidget(self.minLabel)
        self.minLabelValue = QtGui.QLabel(DailyDoublePopup)
        self.minLabelValue.setObjectName(_fromUtf8("minLabelValue"))
        self.horizontalLayout_3.addWidget(self.minLabelValue)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.wagerAmount = QtGui.QLineEdit(DailyDoublePopup)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.wagerAmount.setFont(font)
        self.wagerAmount.setObjectName(_fromUtf8("wagerAmount"))
        self.horizontalLayout.addWidget(self.wagerAmount)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.submitWagerButton = QtGui.QPushButton(DailyDoublePopup)
        self.submitWagerButton.setObjectName(_fromUtf8("submitWagerButton"))
        self.horizontalLayout_2.addWidget(self.submitWagerButton)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(DailyDoublePopup)
        QtCore.QObject.connect(self.submitWagerButton, QtCore.SIGNAL(_fromUtf8("clicked()")), DailyDoublePopup.close)
        QtCore.QMetaObject.connectSlotsByName(DailyDoublePopup)

    def retranslateUi(self, DailyDoublePopup):
        DailyDoublePopup.setWindowTitle(_translate("DailyDoublePopup", "Dialog", None))
        self.label.setText(_translate("DailyDoublePopup", "This is a daily double square! Congratulations!", None))
        self.label_2.setText(_translate("DailyDoublePopup", "What is your wager? (no cents please)", None))
        self.maxLabel.setText(_translate("DailyDoublePopup", "Max:", None))
        self.maxLabelValue.setText(_translate("DailyDoublePopup", "TextLabel", None))
        self.minLabel.setText(_translate("DailyDoublePopup", "Min:", None))
        self.minLabelValue.setText(_translate("DailyDoublePopup", "TextLabel", None))
        self.submitWagerButton.setText(_translate("DailyDoublePopup", "Submit Wager!", None))
