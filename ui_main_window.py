# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowFVjqUv.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide6.QtWidgets import QApplication
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowyHAlPj.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QTextCursor,QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, -1, 791, 561))
        self.frame.setStyleSheet(u"background-color: rgb(255, 221, 208)")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.Code_space = QTextEdit(self.frame)
        self.Code_space.setObjectName(u"Code_space")
        self.Code_space.setGeometry(QRect(10, 10, 601, 431))
        self.Code_space.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"font: 12pt \"Terminal\";")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(619, 9, 161, 431))
        self.widget.setStyleSheet(u"background-color: white")
        self.input_bt = QPushButton(self.widget)
        self.input_bt.setObjectName(u"input_bt")
        self.input_bt.setGeometry(QRect(10, 10, 141, 91))
        self.input_bt.setStyleSheet(u"QPushButton {\n"
"                border: 2px solid black;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                background-color: lightgray;\n"
"				color: black;\n"
"				font: 14pt \"Terminal\";\n"
"            }\n"
"            QPushButton:hover {\n"
"                border-color: blue;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                border-color: red;\n"
"            }")
        self.output_bt = QPushButton(self.widget)
        self.output_bt.setObjectName(u"output_bt")
        self.output_bt.setGeometry(QRect(10, 110, 141, 91))
        self.output_bt.setStyleSheet(u"QPushButton {\n"
"                border: 2px solid black;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                background-color: lightgray;\n"
"				color: black;\n"
"				font: 14pt \"Terminal\";\n"
"            }\n"
"            QPushButton:hover {\n"
"                border-color: blue;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                border-color: red;\n"
"            }")
        self.assign_bt = QPushButton(self.widget)
        self.assign_bt.setObjectName(u"assign_bt")
        self.assign_bt.setGeometry(QRect(10, 210, 141, 91))
        self.assign_bt.setStyleSheet(u"QPushButton {\n"
"                border: 2px solid black;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                background-color: lightgray;\n"
"				color: black;\n"
"				font: 14pt \"Terminal\";\n"
"            }\n"
"            QPushButton:hover {\n"
"                border-color: blue;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                border-color: red;\n"
"            }")
        self.ifthen_bt = QPushButton(self.widget)
        self.ifthen_bt.setObjectName(u"ifthen_bt")
        self.ifthen_bt.setGeometry(QRect(10, 320, 141, 91))
        self.ifthen_bt.setStyleSheet(u"QPushButton {\n"
"                border: 2px solid black;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                background-color: lightgray;\n"
"				color: black;\n"
"				font: 14pt \"Terminal\";\n"
"            }\n"
"            QPushButton:hover {\n"
"                border-color: blue;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                border-color: red;\n"
"            }")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 450, 771, 91))
        self.widget_2.setStyleSheet(u"background-color: white;\n"
"font: 14pt \"Terminal\";")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 731, 81))
        self.label.setStyleSheet(u"color: black")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 804, 33))
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
        self.input_bt.clicked.connect(lambda: self.insert_text("Input "))
        self.output_bt.clicked.connect(lambda: self.insert_text("Output "))
        self.assign_bt.clicked.connect(lambda: self.insert_text(" -> "))
        self.ifthen_bt.clicked.connect(lambda: self.insert_text("If\n\nThen "))
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Code_space.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Terminal'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Code example</p></body></html>", None))
        self.input_bt.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.output_bt.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.assign_bt.setText(QCoreApplication.translate("MainWindow", u"Assign", None))
        self.ifthen_bt.setText(QCoreApplication.translate("MainWindow", u"If-Then", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Example text", None))
        self.menuInicio.setTitle(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

    def insert_text(self, text):
        if self.Code_space.toPlainText() == "Code example":
            self.Code_space.clear("")
        cursor = self.Code_space.textCursor()
        pos = cursor.position()
        self.Code_space.insertPlainText(text)
        cursor.setPosition(pos)
        self.Code_space.setTextCursor(cursor)
        self.Code_space.setFocus()
        print(text)
        if text == " -> ":
            self.Code_space.moveCursor(QTextCursor.MoveOperation.StartOfLine)
        else:
            self.Code_space.moveCursor(QTextCursor.MoveOperation.End)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
