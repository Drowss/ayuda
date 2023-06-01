import math
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QWidget, QButtonGroup, QGridLayout, QScrollArea

from cliente import Cliente
from consulta_datos_tabular import Consulta_datos_tabular

from crud_datos import Crud_datos



class Consulta_datos(QMainWindow):
    def __init__(self, anterior):
        super().__init__()

        self.Anterior = anterior
        # creacion de la ventana
        self.setWindowTitle("Usuarios Registrados")
        self.setWindowIcon(QtGui.QIcon('imagenes/icos.jpg'))
        self.ancho = 900
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap('imagenes/stuicobain.jpg')
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)

        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

        # creacion de layout horizontal para la distribucion
        self.vertical = QVBoxLayout()

        # hacemos los labels informativos
        self.letrero1 = QLabel()
        self.letrero1.setText("Usuario registrado")
        self.letrero1.setFont(QFont("Arial", 20))
        self.letrero1.setStyleSheet('color: black;')

        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet('background-color:transparent;')
        self.scrollArea.setWidgetResizable(True)

        self.contenedora = QWidget()
        self.cuadricula = QGridLayout(self.contenedora)
        self.scrollArea.setWidget(self.contenedora)
        self.vertical.addWidget(self.scrollArea)

        self.file = open('datos/clientes.txt', 'rb')
        self.usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")

            if linea == '':
                break

            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10]
            )

            self.usuarios.append(u)
        self.file.close()

        self.numeroUsuarios = len(self.usuarios)
        self.contador = 0

        self.elementosPorColumna = 3

        self.numerosFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1

        self.botones = QButtonGroup()
        self.botones.setExclusive(False)

        for fila in range(self.numerosFilas):
            for columna in range(self.elementosPorColumna):
                if self.contador < self.numeroUsuarios:
                    self.ventanaAuxiliar = QWidget()
                    self.ventanaAuxiliar.setFixedWidth(100)
                    self.ventanaAuxiliar.setFixedHeight(200)
                    self.verticalCuadricula = QVBoxLayout()
                    self.botonAccion = QPushButton(self.usuarios[self.contador].documento)
                    self.botonAccion.setFixedWidth(90)
                    self.botonAccion.setFixedHeight(40)
                    self.botonAccion.setStyleSheet('background-color: #CCCCFF;'
                                          'color: black;'
                                          'padding: 10px;'
                                          'margin-top: 10px;'
                                          'margin-left: 0px;'
                                          )
                    self.verticalCuadricula.addWidget(self.botonAccion)
                    self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].documento))
                    self.verticalCuadricula.addStretch()
                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)
                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)
                    self.contador += 1

        self.botones.idClicked.connect(self.metodo_accionBotones)

        # ------------- boton tabular ------------
        self.tabular = QPushButton("Forma Tabular")
        self.tabular.setFixedWidth(100)
        self.tabular.setStyleSheet('background-color: #CCCCFF;'
                                          'color: black;'
                                          'padding: 10px;'
                                          'margin-top: 10px;'
                                          'margin-left: 0px;'
                                          )
        self.tabular.clicked.connect(self.metodo_accionTabular)
        self.vertical.addWidget(self.tabular)

        # -----------------Boton volver----------------
        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(100)
        self.botonVolver.setStyleSheet('background-color: #CCCCFF;'
                                          'color: black;'
                                          'padding: 10px;'
                                          'margin-top: 10px;'
                                          'margin-left: 0px;'
                                          )
        self.botonVolver.clicked.connect(self.metodo_botonVolver)
        self.vertical.addWidget(self.botonVolver)

        self.fondo.setLayout(self.vertical)

        # clase 3 son dos commits al principio y al final

    def metodo_accionBotones(self, cedulaUsuario):

        self.hide()
        self.crud_datos = Crud_datos(self, cedulaUsuario)
        self.crud_datos.show()


    def metodo_accionTabular(self):
        self.hide()
        self.consulta_datos_tabular = Consulta_datos_tabular(self)
        self.consulta_datos_tabular.show()


    # commit clase 4 boton volver y al final otro commit con ventana 4 lista
    def metodo_botonVolver(self):
        self.hide()
        self.Anterior.show()


