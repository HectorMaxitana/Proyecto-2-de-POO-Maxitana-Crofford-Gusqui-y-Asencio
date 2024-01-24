from PySide6.QtCore import QRegularExpression, QDate, Qt
from PySide6.QtGui import QIntValidator, QDoubleValidator, QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from Datos.estudiante_Dao import EstudianteDao
from Dominio.estudiante import Estudiante
from GUI.vtn_principal import Ui_vtn_principal
from statistics import mean, mode, median

# --INTEGRANTES--
# CROFFORD VILLAO FREDDY DARWIN
# ASENCIO MADESCO CARLOS ALEXIS
# GUSQUI PALLO MELANIE ANABEL
# MAXITANA MOREIRA HECTOR ALFREDO


class EstudianteServicio(QMainWindow):
    def __init__(self):
        super(EstudianteServicio, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.estudiante = None
        self.ui.btn_grabar.clicked.connect(self.grabar)
        self.ui.btn_busca_x_cedula.clicked.connect(self.buscar_por_cedula)
        self.ui.btn_calcular.clicked.connect(self.calcular)
        self.ui.txt_cedula.setValidator(QIntValidator())
        self.ui.txt_edad.setValidator(QIntValidator())
        self.ui.txt_estatura.setValidator(QDoubleValidator())
        self.ui.txt_peso.setValidator(QDoubleValidator())
        regex = QRegularExpression("^\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b$")
        email_validator = QRegularExpressionValidator(regex)
        self.ui.txt_email.setValidator(email_validator)

    def grabar(self):
        if self.validar_datos():
            nombre = self.ui.txt_nombre.text().capitalize()
            email = self.ui.txt_email.text().lower()
            semestre = self.ui.cb_semestre.currentText()
            cedula = self.ui.txt_cedula.text()
            edad = self.ui.txt_edad.text()
            estatura = self.ui.txt_estatura.text()
            peso = self.ui.txt_peso.text()
            fecha_nacimiento = self.ui.date_fecha_nacimiento.date().toString(Qt.ISODate)

            self.estudiante = Estudiante(nombre=nombre, email=email, semestre=semestre,
                                         cedula=cedula, edad=edad, estatura=estatura,
                                         peso=peso, fecha_nacimiento=fecha_nacimiento)

            try:
                EstudianteDao.insertar_estudiante(self.estudiante)
                self.actualizar_calculos()
                self.ui.sb_estado.showMessage('Ingreso exitoso.', 3000)
                self.limpiar_campos()
            except Exception as e:
                QMessageBox.critical(self, 'Error', 'No se pudo grabar.')
                print(e)
        else:
            QMessageBox.warning(self, 'Advertencia', 'Falta ingresar datos.')

    def validar_datos(self):
        return (len(self.ui.txt_nombre.text()) > 0
                and len(self.ui.txt_email.text()) > 0
                and self.ui.cb_semestre.currentText() != 'Seleccionar'
                and len(self.ui.txt_cedula.text()) == 10
                and len(self.ui.txt_edad.text()) > 0
                and len(self.ui.txt_estatura.text()) > 0
                and len(self.ui.txt_peso.text()) > 0
                and self.ui.date_fecha_nacimiento.date() < QDate.currentDate())

    def buscar_por_cedula(self):
        cedula = self.ui.txt_cedula.text()
        self.estudiante = Estudiante(cedula=cedula)
        estudiante_encontrado = EstudianteDao.seleccionar_x_cedudla(self.estudiante)
        self.mostrar_datos(estudiante_encontrado)

    def calcular(self):
        self.actualizar_calculos()

    def actualizar_calculos(self):
        estudiantes = EstudianteDao.seleccionar_personas()
        edades = []
        estaturas = []
        pesos = []

        for estudiante in estudiantes:
            if estudiante.edad:
                edades.append(estudiante.edad)
            if estudiante.estatura:
                estaturas.append(estudiante.estatura)
            if estudiante.peso:
                pesos.append(estudiante.peso)

        if edades:
            promedio_edad = mean(edades)
            print(f'Promedio de Edad: {promedio_edad}')
            moda_edad = mode(edades)
            print(f'Moda de Edad: {moda_edad}')
            mediana_edad = median(edades)
            print(f'Mediana de Edad: {mediana_edad}')
            min_edad = min(edades)
            print(f'Mínimo de Edad: {min_edad}')
            max_edad = max(edades)
            print(f'Máximo de Edad: {max_edad}')

        if estaturas:
            promedio_estatura = mean(estaturas)
            print(f'Promedio de Estatura: {promedio_estatura}')
            moda_estatura = mode(estaturas)
            print(f'Moda de Estatura: {moda_estatura}')
            mediana_estatura = median(estaturas)
            print(f'Mediana de Estatura: {mediana_estatura}')
            min_estatura = min(estaturas)
            print(f'Mínimo de Estatura: {min_estatura}')
            max_estatura = max(estaturas)
            print(f'Máximo de Estatura: {max_estatura}')

        if pesos:
            promedio_peso = mean(pesos)
            print(f'Promedio de Peso: {promedio_peso}')
            moda_peso = mode(pesos)
            print(f'Moda de Peso: {moda_peso}')
            mediana_peso = median(pesos)
            print(f'Mediana de Peso: {mediana_peso}')
            min_peso = min(pesos)
            print(f'Mínimo de Peso: {min_peso}')
            max_peso = max(pesos)
            print(f'Máximo de Peso: {max_peso}')

    def mostrar_datos(self, estudiante):
        self.ui.txt_email.setText(estudiante.email)
        self.ui.txt_nombre.setText(estudiante.nombre)
        self.ui.txt_edad.setText(estudiante.edad)
        self.ui.txt_estatura.setText(estudiante.estatura)
        self.ui.txt_peso.setText(estudiante.peso)
        self.ui.cb_semestre.setCurrentText(estudiante.semestre)
        self.ui.date_fecha_nacimiento.setDate(QDate.fromString(estudiante.fecha_nacimiento, Qt.ISODate))

    def limpiar_campos(self):
        self.ui.txt_email.setText('')
        self.ui.txt_nombre.setText('')
        self.ui.txt_cedula.setText('')
        self.ui.txt_edad.setText('')
        self.ui.txt_estatura.setText('')
        self.ui.txt_peso.setText('')
        self.ui.cb_semestre.setCurrentText('Seleccionar')
        self.ui.date_fecha_nacimiento.setDate(QDate.currentDate())
