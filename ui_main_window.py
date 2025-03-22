# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(798, 600)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"    background-color: #dbeafe;\n"
"    color: #0f172a;\n"
"    border: 2px solid #3b82f6;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #bfdbfe;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #93c5fd;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, -1, 791, 561))
        self.frame.setStyleSheet(u"background-color: rgb(155, 227, 252)")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.Code_space = QTextEdit(self.frame)
        self.Code_space.setObjectName(u"Code_space")
        self.Code_space.setGeometry(QRect(10, 100, 601, 341))
        self.Code_space.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"font: 12pt \"Terminal\";")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(619, 9, 161, 431))
        self.widget.setStyleSheet(u"background-color: white")
        self.input_bt = QPushButton(self.widget)
        self.input_bt.setObjectName(u"input_bt")
        self.input_bt.setGeometry(QRect(10, 10, 141, 51))
        self.input_bt.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #e0f2fe, stop: 1 #bae6fd\n"
"    );\n"
"    color: #1e3a8a;\n"
"    border: 2px solid #60a5fa;\n"
"    border-radius: 12px;\n"
"    padding: 8px 16px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    letter-spacing: 0.5px;\n"
"    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #bae6fd, stop: 1 #7dd3fc\n"
"    );\n"
"    border: 2px solid #3b82f6;\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #60a5fa;\n"
"    border: 2px solid #2563eb;\n"
"    color: white;\n"
"}\n"
"")
        self.output_bt = QPushButton(self.widget)
        self.output_bt.setObjectName(u"output_bt")
        self.output_bt.setGeometry(QRect(10, 70, 141, 51))
        self.output_bt.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #e0f2fe, stop: 1 #bae6fd\n"
"    );\n"
"    color: #1e3a8a;\n"
"    border: 2px solid #60a5fa;\n"
"    border-radius: 12px;\n"
"    padding: 8px 16px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    letter-spacing: 0.5px;\n"
"    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #bae6fd, stop: 1 #7dd3fc\n"
"    );\n"
"    border: 2px solid #3b82f6;\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #60a5fa;\n"
"    border: 2px solid #2563eb;\n"
"    color: white;\n"
"}\n"
"")
        self.assign_bt = QPushButton(self.widget)
        self.assign_bt.setObjectName(u"assign_bt")
        self.assign_bt.setGeometry(QRect(10, 130, 141, 51))
        self.assign_bt.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #e0f2fe, stop: 1 #bae6fd\n"
"    );\n"
"    color: #1e3a8a;\n"
"    border: 2px solid #60a5fa;\n"
"    border-radius: 12px;\n"
"    padding: 8px 16px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    letter-spacing: 0.5px;\n"
"    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #bae6fd, stop: 1 #7dd3fc\n"
"    );\n"
"    border: 2px solid #3b82f6;\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #60a5fa;\n"
"    border: 2px solid #2563eb;\n"
"    color: white;\n"
"}\n"
"")
        self.ifthen_bt = QPushButton(self.widget)
        self.ifthen_bt.setObjectName(u"ifthen_bt")
        self.ifthen_bt.setGeometry(QRect(10, 190, 141, 51))
        self.ifthen_bt.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #e0f2fe, stop: 1 #bae6fd\n"
"    );\n"
"    color: #1e3a8a;\n"
"    border: 2px solid #60a5fa;\n"
"    border-radius: 12px;\n"
"    padding: 8px 16px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    letter-spacing: 0.5px;\n"
"    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #bae6fd, stop: 1 #7dd3fc\n"
"    );\n"
"    border: 2px solid #3b82f6;\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #60a5fa;\n"
"    border: 2px solid #2563eb;\n"
"    color: white;\n"
"}\n"
"")
        self.while_bt = QPushButton(self.widget)
        self.while_bt.setObjectName(u"while_bt")
        self.while_bt.setGeometry(QRect(10, 250, 141, 51))
        self.while_bt.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #e0f2fe, stop: 1 #bae6fd\n"
"    );\n"
"    color: #1e3a8a;\n"
"    border: 2px solid #60a5fa;\n"
"    border-radius: 12px;\n"
"    padding: 8px 16px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    letter-spacing: 0.5px;\n"
"    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #bae6fd, stop: 1 #7dd3fc\n"
"    );\n"
"    border: 2px solid #3b82f6;\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #60a5fa;\n"
"    border: 2px solid #2563eb;\n"
"    color: white;\n"
"}\n"
"")
        self.for_bt = QPushButton(self.widget)
        self.for_bt.setObjectName(u"for_bt")
        self.for_bt.setGeometry(QRect(10, 310, 141, 51))
        self.for_bt.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #e0f2fe, stop: 1 #bae6fd\n"
"    );\n"
"    color: #1e3a8a;\n"
"    border: 2px solid #60a5fa;\n"
"    border-radius: 12px;\n"
"    padding: 8px 16px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    letter-spacing: 0.5px;\n"
"    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #bae6fd, stop: 1 #7dd3fc\n"
"    );\n"
"    border: 2px solid #3b82f6;\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #60a5fa;\n"
"    border: 2px solid #2563eb;\n"
"    color: white;\n"
"}\n"
"")
        self.while_bt_3 = QPushButton(self.widget)
        self.while_bt_3.setObjectName(u"while_bt_3")
        self.while_bt_3.setGeometry(QRect(10, 370, 141, 51))
        self.while_bt_3.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #e0f2fe, stop: 1 #bae6fd\n"
"    );\n"
"    color: #1e3a8a;\n"
"    border: 2px solid #60a5fa;\n"
"    border-radius: 12px;\n"
"    padding: 8px 16px;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    letter-spacing: 0.5px;\n"
"    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #bae6fd, stop: 1 #7dd3fc\n"
"    );\n"
"    border: 2px solid #3b82f6;\n"
"    color: #1d4ed8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #60a5fa;\n"
"    border: 2px solid #2563eb;\n"
"    color: white;\n"
"}\n"
"")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 450, 771, 91))
        self.widget_2.setStyleSheet(u"background-color: white;\n"
"font: 14pt \"Terminal\";")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 731, 81))
        self.label.setStyleSheet(u"color: black")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, -1, 601, 91))
        font = QFont()
        font.setFamilies([u"Segoe UI,sans-serif"])
        font.setBold(True)
        font.setItalic(False)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    border: none;  \n"
"    border-radius: 0px;  \n"
"    margin-top: 20px;\n"
"    padding: 10px;\n"
"    background-color: white;  \n"
"    font: bold 14px \"Segoe UI\", sans-serif;\n"
"    color: #1e3a8a;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 4px 10px;\n"
"    background-color: transparent;\n"
"    color: #1e3a8a;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.nuevo_bt = QPushButton(self.groupBox)
        self.nuevo_bt.setObjectName(u"nuevo_bt")
        self.nuevo_bt.setGeometry(QRect(20, 40, 101, 31))
        icon = QIcon()
        icon.addFile(u"imagenes/nuevo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nuevo_bt.setIcon(icon)
        self.abrir_bt = QPushButton(self.groupBox)
        self.abrir_bt.setObjectName(u"abrir_bt")
        self.abrir_bt.setGeometry(QRect(130, 40, 101, 31))
        icon1 = QIcon()
        icon1.addFile(u"imagenes/abrir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.abrir_bt.setIcon(icon1)
        self.ejecutar_bt = QPushButton(self.groupBox)
        self.ejecutar_bt.setObjectName(u"ejecutar_bt")
        self.ejecutar_bt.setGeometry(QRect(360, 40, 111, 31))
        icon2 = QIcon()
        icon2.addFile(u"imagenes/ejecutar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ejecutar_bt.setIcon(icon2)
        self.guardar_bt = QPushButton(self.groupBox)
        self.guardar_bt.setObjectName(u"guardar_bt")
        self.guardar_bt.setGeometry(QRect(240, 40, 111, 31))
        icon3 = QIcon()
        icon3.addFile(u"imagenes/salvar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.guardar_bt.setIcon(icon3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 798, 26))
        self.menuInicio = QMenu(self.menubar)
        self.menuInicio.setObjectName(u"menuInicio")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuInicio.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Code_space.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Terminal'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Code example</p></body></html>", None))
        self.input_bt.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.output_bt.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.assign_bt.setText(QCoreApplication.translate("MainWindow", u"Assign", None))
        self.ifthen_bt.setText(QCoreApplication.translate("MainWindow", u"If-Then", None))
        self.while_bt.setText(QCoreApplication.translate("MainWindow", u"While", None))
        self.for_bt.setText(QCoreApplication.translate("MainWindow", u"For", None))
        self.while_bt_3.setText(QCoreApplication.translate("MainWindow", u"Function", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Example text", None))
        self.groupBox.setTitle("")
        self.nuevo_bt.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.abrir_bt.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.ejecutar_bt.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        self.guardar_bt.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.menuInicio.setTitle(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

