# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Welcome(object):
    def setupUi(self, Welcome):
        if not Welcome.objectName():
            Welcome.setObjectName(u"Welcome")
        Welcome.resize(800, 600)
        self.frame = QFrame(Welcome)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 801, 601))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(24, 20, 751, 561))
        self.label.setStyleSheet(u"background-color: rgb(155, 227, 252)")
        self.nombre_pro = QLabel(self.frame)
        self.nombre_pro.setObjectName(u"nombre_pro")
        self.nombre_pro.setGeometry(QRect(260, 70, 301, 41))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(26)
        font.setBold(True)
        self.nombre_pro.setFont(font)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 90, 491, 441))
        self.label_2.setPixmap(QPixmap(u"imagenes/bienvenido.png"))
        self.label_2.setScaledContents(True)
        self.continuar = QPushButton(self.frame)
        self.continuar.setObjectName(u"continuar")
        self.continuar.setGeometry(QRect(350, 520, 121, 41))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI,sans-serif"])
        font1.setBold(True)
        self.continuar.setFont(font1)
        self.continuar.setStyleSheet(u"QPushButton {\n"
"    background-color: #00B4D8;\n"
"    color: white;\n"
"    border: 2px solid #0077B6;\n"
"    border-radius: 10px;\n"
"    padding: 10px 20px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0096C7;\n"
"    border-color: #023E8A;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0077B6;\n"
"    border-color: #03045E;\n"
"}\n"
"")

        self.retranslateUi(Welcome)

        QMetaObject.connectSlotsByName(Welcome)
    # setupUi

    def retranslateUi(self, Welcome):
        Welcome.setWindowTitle(QCoreApplication.translate("Welcome", u"Dialog", None))
        self.label.setText("")
        self.nombre_pro.setText(QCoreApplication.translate("Welcome", u"CompilaSoft", None))
        self.label_2.setText("")
        self.continuar.setText(QCoreApplication.translate("Welcome", u"Continuar", None))
    # retranslateUi



