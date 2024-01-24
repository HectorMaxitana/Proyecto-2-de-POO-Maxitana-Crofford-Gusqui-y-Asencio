# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_vtn_principal(object):
    def setupUi(self, vtn_principal):
        if not vtn_principal.objectName():
            vtn_principal.setObjectName(u"vtn_principal")
        vtn_principal.resize(600, 321)
        self.centralwidget = QWidget(vtn_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.txt_nombre = QLineEdit(self.centralwidget)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(180, 20, 201, 20))
        self.txt_email = QLineEdit(self.centralwidget)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(180, 80, 201, 20))
        self.cb_semestre = QComboBox(self.centralwidget)
        self.cb_semestre.addItem("")
        self.cb_semestre.addItem("")
        self.cb_semestre.addItem("")
        self.cb_semestre.addItem("")
        self.cb_semestre.setObjectName(u"cb_semestre")
        self.cb_semestre.setGeometry(QRect(180, 110, 201, 22))
        self.lbl_nombre = QLabel(self.centralwidget)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(130, 20, 47, 13))
        self.lbl_email = QLabel(self.centralwidget)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(140, 80, 31, 16))
        self.lbl_semestre = QLabel(self.centralwidget)
        self.lbl_semestre.setObjectName(u"lbl_semestre")
        self.lbl_semestre.setGeometry(QRect(130, 110, 47, 13))
        self.btn_grabar = QPushButton(self.centralwidget)
        self.btn_grabar.setObjectName(u"btn_grabar")
        self.btn_grabar.setGeometry(QRect(170, 260, 75, 23))
        self.lbl_cedula = QLabel(self.centralwidget)
        self.lbl_cedula.setObjectName(u"lbl_cedula")
        self.lbl_cedula.setGeometry(QRect(130, 50, 31, 16))
        self.txt_cedula = QLineEdit(self.centralwidget)
        self.txt_cedula.setObjectName(u"txt_cedula")
        self.txt_cedula.setGeometry(QRect(180, 50, 201, 22))
        self.txt_cedula.setMaxLength(10)
        self.btn_busca_x_cedula = QPushButton(self.centralwidget)
        self.btn_busca_x_cedula.setObjectName(u"btn_busca_x_cedula")
        self.btn_busca_x_cedula.setGeometry(QRect(400, 50, 111, 24))
        self.txt_edad = QLineEdit(self.centralwidget)
        self.txt_edad.setObjectName(u"txt_edad")
        self.txt_edad.setGeometry(QRect(180, 140, 113, 22))
        self.lbl_edad = QLabel(self.centralwidget)
        self.lbl_edad.setObjectName(u"lbl_edad")
        self.lbl_edad.setGeometry(QRect(150, 140, 21, 16))
        self.btn_calcular = QPushButton(self.centralwidget)
        self.btn_calcular.setObjectName(u"btn_calcular")
        self.btn_calcular.setGeometry(QRect(280, 260, 75, 24))
        self.lbl_estatura = QLabel(self.centralwidget)
        self.lbl_estatura.setObjectName(u"lbl_estatura")
        self.lbl_estatura.setGeometry(QRect(140, 170, 35, 21))
        self.txt_estatura = QLineEdit(self.centralwidget)
        self.txt_estatura.setObjectName(u"txt_estatura")
        self.txt_estatura.setGeometry(QRect(180, 170, 201, 22))
        self.txt_estatura.setMaxLength(10)
        self.lbl_peso = QLabel(self.centralwidget)
        self.lbl_peso.setObjectName(u"lbl_peso")
        self.lbl_peso.setGeometry(QRect(150, 200, 21, 21))
        self.txt_peso = QLineEdit(self.centralwidget)
        self.txt_peso.setObjectName(u"txt_peso")
        self.txt_peso.setGeometry(QRect(180, 200, 201, 22))
        self.txt_peso.setMaxLength(10)
        self.lbl_peso_2 = QLabel(self.centralwidget)
        self.lbl_peso_2.setObjectName(u"lbl_peso_2")
        self.lbl_peso_2.setGeometry(QRect(100, 220, 81, 41))
        self.date_fecha_nacimiento = QDateEdit(self.centralwidget)
        self.date_fecha_nacimiento.setObjectName(u"date_fecha_nacimiento")
        self.date_fecha_nacimiento.setGeometry(QRect(180, 230, 110, 21))
        self.lbl_integrantes = QLabel(self.centralwidget)
        self.lbl_integrantes.setObjectName(u"lbl_integrantes")
        self.lbl_integrantes.setGeometry(QRect(410, 90, 161, 91))
        vtn_principal.setCentralWidget(self.centralwidget)
        self.sb_estado = QStatusBar(vtn_principal)
        self.sb_estado.setObjectName(u"sb_estado")
        vtn_principal.setStatusBar(self.sb_estado)
        QWidget.setTabOrder(self.txt_nombre, self.txt_cedula)
        QWidget.setTabOrder(self.txt_cedula, self.txt_email)
        QWidget.setTabOrder(self.txt_email, self.cb_semestre)
        QWidget.setTabOrder(self.cb_semestre, self.btn_grabar)

        self.retranslateUi(vtn_principal)

        QMetaObject.connectSlotsByName(vtn_principal)
    # setupUi

    def retranslateUi(self, vtn_principal):
        vtn_principal.setWindowTitle(QCoreApplication.translate("vtn_principal", u"Estudiante", None))
        self.cb_semestre.setItemText(0, QCoreApplication.translate("vtn_principal", u"Seleccionar", None))
        self.cb_semestre.setItemText(1, QCoreApplication.translate("vtn_principal", u"Primer Semestre", None))
        self.cb_semestre.setItemText(2, QCoreApplication.translate("vtn_principal", u"Segundo Semestre", None))
        self.cb_semestre.setItemText(3, QCoreApplication.translate("vtn_principal", u"Tercer Semestre", None))

        self.lbl_nombre.setText(QCoreApplication.translate("vtn_principal", u"Nombre:", None))
        self.lbl_email.setText(QCoreApplication.translate("vtn_principal", u"Email:", None))
        self.lbl_semestre.setText(QCoreApplication.translate("vtn_principal", u"Semestre:", None))
        self.btn_grabar.setText(QCoreApplication.translate("vtn_principal", u"Grabar", None))
        self.lbl_cedula.setText(QCoreApplication.translate("vtn_principal", u"Cedula:", None))
        self.btn_busca_x_cedula.setText(QCoreApplication.translate("vtn_principal", u"Buscar por Cedula", None))
        self.lbl_edad.setText(QCoreApplication.translate("vtn_principal", u"Edad:", None))
        self.btn_calcular.setText(QCoreApplication.translate("vtn_principal", u"Calcular", None))
        self.lbl_estatura.setText(QCoreApplication.translate("vtn_principal", u"Estatura:", None))
        self.lbl_peso.setText(QCoreApplication.translate("vtn_principal", u"Peso:", None))
        self.lbl_peso_2.setText(QCoreApplication.translate("vtn_principal", u"Fecha de nacimiento:", None))
    # retranslateUi

