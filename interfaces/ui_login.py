# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginVxJqxq.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 640)
        Form.setStyleSheet(u"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: #fff;\n"
"	color: red;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #454544;\n"
"	font-weight: bold;\n"
"	font-size: 13px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: #1b3cbd;\n"
"	color: #fff;\n"
"	font-size: 13px;\n"
"	font-weight: bold;\n"
"	border-top-right-radius: 15px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	border-bottom-left-radius: 15px;\n"
"	padding: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #1b3cbd;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #254de8;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #1b3cbd;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"	background-color: transparent;\n"
"	color: #5c55e9;\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	border: no"
                        "ne;\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: #323232;\n"
"    border: 1px solid darkgray;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"	background-color: #5c55e9;\n"
"    border: 1px solid #5c55e9;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #5c55e9;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #c2c7d5;\n"
"	color: #2a547f;\n"
"	border: none;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView\n"
"{\n"
"	background-color: #5c55e9;\n"
"	color: #fff;\n"
"	font-size: 14px;\n"
""
                        "	font-weight: bold;\n"
"	show-decoration-selected: 0;\n"
"	border-radius: 4px;\n"
"	padding-left: -15px;\n"
"	padding-right: -15px;\n"
"	padding-top: 5px;\n"
"\n"
"} \n"
"\n"
"\n"
"QListView:disabled \n"
"{\n"
"	background-color: #5c5c5c;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item\n"
"{\n"
"	background-color: #454e5e;\n"
"	border: none;\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	padding-left : 10px;\n"
"	height: 32px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected\n"
"{\n"
"	color: #000;\n"
"	background-color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected\n"
"{\n"
"	color:white;\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected:hover\n"
"{\n"
"	color: #fff;\n"
"	background-color: #5564f2;\n"
"	border: none;\n"
"	padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeView-----*/\n"
"QTreeView \n"
"{\n"
"	background-color: #fff;\n"
"	show-decoration-selected: 0;\n"
"	color: #454544;\n"
"\n"
"}\n"
"\n"
"\n"
"QT"
                        "reeView:disabled\n"
"{\n"
"	background-color: #242526;\n"
"	show-decoration-selected: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item \n"
"{\n"
"	border-top-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:hover \n"
"{\n"
"	background-color: #bcbdbb;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected \n"
"{\n"
"	background-color: #5c55e9;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected:active\n"
"{\n"
"	background-color: #5c55e9;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected:disabled\n"
"{\n"
"	background-color: #525251;\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"	image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"	image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*"
                        "-----QTableView & QTableWidget-----*/\n"
"QTableView\n"
"{\n"
"    background-color: #fff;\n"
"	border: 1px solid gray;\n"
"    color: #454544;\n"
"    gridline-color: gray;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::disabled\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:hover \n"
"{\n"
"    background-color: #bcbdbb;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{\n"
"	background-color: #5c55e9;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected:disabled\n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"	background-color: #ced5e3;\n"
"	border: none;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section\n"
"{\n"
"	color: #2a547f;\n"
"	border: 0px;\n"
"	background-color: #ce"
                        "d5e3;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    color: #fff;\n"
"    background-color: #5c55e9;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked:disabled\n"
"{\n"
"    color: #656565;\n"
"    background-color: #525251;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal \n"
"{\n"
"    background-color: transpare"
                        "nt;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    border: none;\n"
"	min-width: 100px;\n"
"    background-color: #7e92b7;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizontal \n"
"{\n"
"    width: 0px;\n"
"    background-color: #d8dce6;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    background-color: transparent;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"	min-height: 100px;\n"
"    background-color: #7e92b7;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical \n"
"{\n"
"    height: 0px;\n"
"    background-color: #d8dce6;\n"
"\n"
"}\n"
"")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(560, -30, 471, 691))
        self.frame.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1264b5, stop:0.5 #1976d3, stop:1 #1264b5);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 110, 111, 81))
        font = QFont()
        font.setFamilies([u"Century"])
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: transparent;")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 150, 171, 81))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: transparent;")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 280, 311, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent;\n"
"	font: 11pt \"Century\";\n"
"	color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"    border-bottom: 1px solid #ffffff; /* Cambia \"#yourBorderColor\" al color que desees para el borde inferior */\n"
"    padding-bottom: 1px; /* Ajusta el valor seg\u00fan el grosor del borde inferior */\n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom: 1px solid #ffffff; /* Cambia \"#yourHoverColor\" al color que desees cuando el cursor est\u00e9 sobre el QLineEdit */\n"
"}\n"
"QLineEdit::placeholder{\n"
"	color: #ffffff\n"
"}\n"
"QLineEdit::placeholder {\n"
"    color: white; /* Establece el color del texto del marcador de posici\u00f3n en blanco */\n"
"}\n"
"")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(90, 370, 311, 31))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent;\n"
"	font: 11pt \"Century\";\n"
"	color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"    border-bottom: 1px solid #ffffff; /* Cambia \"#yourBorderColor\" al color que desees para el borde inferior */\n"
"    padding-bottom: 1px; /* Ajusta el valor seg\u00fan el grosor del borde inferior */\n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom: 1px solid #ffffff; /* Cambia \"#yourHoverColor\" al color que desees cuando el cursor est\u00e9 sobre el QLineEdit */\n"
"}\n"
"QLineEdit::placeholder{\n"
"	color: #ffffff\n"
"}\n"
"QLineEdit::placeholder {\n"
"    color: white; /* Establece el color del texto del marcador de posici\u00f3n en blanco */\n"
"}\n"
"")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(370, 280, 31, 31))
        self.widget.setStyleSheet(u"image: url(:/Icons/assets/Icons/usuario.png);\n"
"background-color: transparent;")
        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(370, 370, 31, 31))
        self.widget_3.setStyleSheet(u"image: url(:/Icons/assets/Icons/llave.png);\n"
"background-color: transparent;")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 470, 321, 41))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #1976d3;\n"
"    border-radius: 20px; /* Ajusta el valor seg\u00fan el radio de redondeo deseado */\n"
"    padding: 5px 10px; /* Ajusta el valor seg\u00fan el espaciado interior deseado */\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/Icons/assets/Icons/flecha-derecha.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(25, 25))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 60, 241, 81))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: transparent;")
        self.widget_10 = QWidget(Form)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(370, 420, 31, 31))
        self.widget_10.setStyleSheet(u"background-color: transparent;\n"
"image: url(:/Icons/assets/Icons/cerrar.png);")
        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(300, 0, 31, 31))
        self.widget_11.setStyleSheet(u"background-color: transparent;\n"
"image: url(:/Icons/assets/Icons/cerrar.png);")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 10, 41, 31))
        self.pushButton_2.setStyleSheet(u"background-color: #ffffff;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/assets/Icons/energia.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(20, 20))
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(70, 361, 331, 31))
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent;\n"
"	font: 11pt \"Century\";\n"
"	color: rgb(0, 0, 0);\n"
"    border: 0px;\n"
"    border-bottom: 1px solid #000000; /* Cambia \"#yourBorderColor\" al color que desees para el borde inferior */\n"
"    padding-bottom: 1px; /* Ajusta el valor seg\u00fan el grosor del borde inferior */\n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom: 1px solid #000000; /* Cambia \"#yourHoverColor\" al color que desees cuando el cursor est\u00e9 sobre el QLineEdit */\n"
"}\n"
"QLineEdit::placeholder{\n"
"	color: #000000\n"
"}\n"
"QLineEdit::placeholder {\n"
"    color: 000000; /* Establece el color del texto del marcador de posici\u00f3n en blanco */\n"
"}\n"
"")
        self.widget_4 = QWidget(Form)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(370, 360, 31, 31))
        self.widget_4.setStyleSheet(u"background-color: transparent;\n"
"image: url(:/Icons/assets/Icons/comprobacion-de-usuario.png);")
        self.widget_12 = QWidget(Form)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(370, 480, 31, 31))
        self.widget_12.setStyleSheet(u"background-color: transparent;\n"
"image: url(:/Icons/assets/Icons/cerrar.png);")
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(300, 0, 31, 31))
        self.widget_13.setStyleSheet(u"background-color: transparent;\n"
"image: url(:/Icons/assets/Icons/cerrar.png);")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 20, 361, 81))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: transparent;")
        self.lineEdit_6 = QLineEdit(Form)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(70, 480, 331, 31))
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent;\n"
"	font: 11pt \"Century\";\n"
"	color: rgb(0, 0, 0);\n"
"    border: 0px;\n"
"    border-bottom: 1px solid #000000; /* Cambia \"#yourBorderColor\" al color que desees para el borde inferior */\n"
"    padding-bottom: 1px; /* Ajusta el valor seg\u00fan el grosor del borde inferior */\n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom: 1px solid #000000; /* Cambia \"#yourHoverColor\" al color que desees cuando el cursor est\u00e9 sobre el QLineEdit */\n"
"}\n"
"QLineEdit::placeholder{\n"
"	color: #000000\n"
"}\n"
"QLineEdit::placeholder {\n"
"    color: 000000; /* Establece el color del texto del marcador de posici\u00f3n en blanco */\n"
"}\n"
"")
        self.lineEdit_6.setEchoMode(QLineEdit.Password)
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(70, 300, 331, 31))
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent;\n"
"	font: 11pt \"Century\";\n"
"	color: rgb(0, 0, 0);\n"
"    border: 0px;\n"
"    border-bottom: 1px solid #000000; /* Cambia \"#yourBorderColor\" al color que desees para el borde inferior */\n"
"    padding-bottom: 1px; /* Ajusta el valor seg\u00fan el grosor del borde inferior */\n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom: 1px solid #000000; /* Cambia \"#yourHoverColor\" al color que desees cuando el cursor est\u00e9 sobre el QLineEdit */\n"
"}\n"
"QLineEdit::placeholder{\n"
"	color: #000000\n"
"}\n"
"QLineEdit::placeholder {\n"
"    color: 000000; /* Establece el color del texto del marcador de posici\u00f3n en blanco */\n"
"}\n"
"")
        self.lineEdit_5 = QLineEdit(Form)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(70, 421, 331, 31))
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent;\n"
"	font: 11pt \"Century\";\n"
"	color: rgb(0, 0, 0);\n"
"    border: 0px;\n"
"    border-bottom: 1px solid #000000; /* Cambia \"#yourBorderColor\" al color que desees para el borde inferior */\n"
"    padding-bottom: 1px; /* Ajusta el valor seg\u00fan el grosor del borde inferior */\n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom: 1px solid #000000; /* Cambia \"#yourHoverColor\" al color que desees cuando el cursor est\u00e9 sobre el QLineEdit */\n"
"}\n"
"QLineEdit::placeholder{\n"
"	color: #000000\n"
"}\n"
"QLineEdit::placeholder {\n"
"    color: 000000; /* Establece el color del texto del marcador de posici\u00f3n en blanco */\n"
"}\n"
"")
        self.lineEdit_5.setEchoMode(QLineEdit.Password)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(370, 299, 31, 31))
        self.widget_2.setStyleSheet(u"background-color: transparent;\n"
"image: url(:/Icons/assets/Icons/en.png);")
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(70, 570, 321, 41))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #1264b5;\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 20px; /* Ajusta el valor seg\u00fan el radio de redondeo deseado */\n"
"    padding: 5px 10px; /* Ajusta el valor seg\u00fan el espaciado interior deseado */\n"
"}\n"
"\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/assets/Icons/tornillo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(25, 25))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, -10, 501, 291))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">Login</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">\u00a1Bienvenido de nuevo!</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Email", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.pushButton.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; color:#4f79b1;\">Welcome to a new experience</span></p></body></html>", None))
        self.pushButton_2.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"Usuario", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:26pt; color:#000000;\">Register</span></p></body></html>", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Form", u"Confirmar contrase\u00f1a", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"Email", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Reg\u00edstrate", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<img src=\":/img/assets/img/Logo Azul.png\" width=\"400\" height=\"400\">", None))
    # retranslateUi

