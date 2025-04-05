# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'traducir.ui'
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
    QSizePolicy, QTextEdit, QWidget)

class Ui_Traducir(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 801, 601))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 801, 601))
        self.widget_2.setStyleSheet(u"background-color: white;\n"
"font: 14pt \"Terminal\";")
        self.label1 = QLabel(self.widget_2)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(40, 190, 731, 371))
        self.label1.setStyleSheet(u"\n"
"background-color:rgb(216, 249, 255)")
        self.label_titulo = QLabel(self.widget_2)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(260, 40, 491, 111))
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.label_titulo.setFont(font)
        self.label_titulo.setStyleSheet(u"QLabel {\n"
"    border: 4px solid #5DADE2;\n"
"    background-color: #D8F9FF;  /* Azul claro del fondo de la imagen */\n"
"    color: black;               /* Texto en negro */\n"
"    padding: 10px;              /* Espaciado interno */\n"
"    border-radius: 50px;        /* Bordes redondeados */\n"
"}\n"
"\n"
"QLabel {\n"
"    font-family: \"Impact\";\n"
"    font-size: 20pt;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"\n"
"")
        self.textEdit = QTextEdit(self.widget_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(50, 200, 711, 351))
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"    border: 4px outset #5DADE2;  /* Borde con efecto elevado */\n"
"    background-color: white;  /* Fondo blanco */\n"
"    padding: 5px;  /* Espaciado interno */\n"
"    font-size: 14pt; \n"
"}\n"
"\n"
"")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 121, 121))
        self.label.setPixmap(QPixmap(u"imagenes/ruby.png"))
        self.label.setScaledContents(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label1.setText("")
        self.label_titulo.setText(QCoreApplication.translate("Dialog", u"Traduccion a Ruby", None))
        self.label.setText("")
    # retranslateUi

