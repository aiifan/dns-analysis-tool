# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextBrowser,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(675, 622)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.dns = QLineEdit(Form)
        self.dns.setObjectName(u"dns")

        self.gridLayout.addWidget(self.dns, 0, 2, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(False)

        self.gridLayout.addWidget(self.comboBox, 0, 4, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 3, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 4, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.domain = QTextEdit(Form)
        self.domain.setObjectName(u"domain")
        self.domain.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.domain, 2, 1, 1, 4)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.respose = QTextBrowser(Form)
        self.respose.setObjectName(u"respose")

        self.gridLayout.addWidget(self.respose, 3, 1, 1, 4)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 3)

        self.filepath = QLineEdit(Form)
        self.filepath.setObjectName(u"filepath")

        self.gridLayout.addWidget(self.filepath, 1, 0, 1, 3)


        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.run)
        self.pushButton_2.clicked.connect(Form.openFile)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"DNS\u89e3\u6790\u5668", None))
        self.label.setText(QCoreApplication.translate("Form", u"dns:", None))
        self.dns.setPlaceholderText(QCoreApplication.translate("Form", u"192.168.68.1,223.5.5.5", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u89e3\u6790\u7c7b\u578b\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"A", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"AAAA", None))

        self.comboBox.setPlaceholderText("")
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u5bfc\u5165", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u57df\u540d\uff1a", None))
        self.domain.setPlaceholderText(QCoreApplication.translate("Form", u"baidu.com,q.com", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u7ed3\u679c\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\uff1a aiifan   \u90ae\u7bb1\uff1a aiifan@126.com", None))
        self.filepath.setPlaceholderText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u8def\u5f84(\u6587\u672c\u6587\u4ef6,\u4e00\u884c\u4e00\u4e2a\u57df\u540d)", None))
    # retranslateUi

