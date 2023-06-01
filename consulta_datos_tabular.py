import math
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QWidget, QButtonGroup, QGridLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QToolBar, QAction, QMessageBox

from cliente import Cliente


class Consulta_datos_tabular(QMainWindow):
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
        self.imagenFondo = QPixmap('imagenes/stuienojado.jpeg')
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)

        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

        # creacion de layout horizontal para la distribucion
        self.vertical = QVBoxLayout()

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

        # ---- Construccion del toolbar----
        self.toolbar = QToolBar('Main Toolbar')
        self.toolbar.setIconSize(QSize(25, 25))
        self.addToolBar(self.toolbar)

        # toolbar eliminar
        self.delete = QAction(QIcon('imagenes/delete.jpg'), "&borrar", self)
        self.delete.triggered.connect(self.accion_delete)
        self.toolbar.addAction(self.delete)

        # toolbar agregar
        self.agregar = QAction(QIcon('imagenes/agregar.png'), "&agregar", self)
        self.agregar.triggered.connect(self.accion_agregar)
        self.toolbar.addAction(self.agregar)

        # toolbar editar
        self.editar = QAction(QIcon('imagenes/editar.png'), "&editar", self)
        self.editar.triggered.connect(self.accion_editar)
        self.toolbar.addAction(self.editar)

        # ---- Fin toolbar------

        # hacemos los labels informativos
        self.letrero1 = QLabel()
        self.letrero1.setText("Usuario registrado")
        self.letrero1.setFont(QFont("Arial", 20))
        self.letrero1.setStyleSheet('color: black;')

        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)

        # para crear la tabla para que se vean de forma tabular
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(11)

        # definimos los numeros de colimnas que tendra la tabla

        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 150)
        self.tabla.setColumnWidth(5, 150)
        self.tabla.setColumnWidth(6, 150)
        self.tabla.setColumnWidth(7, 150)
        self.tabla.setColumnWidth(8, 150)
        self.tabla.setColumnWidth(9, 150)
        self.tabla.setColumnWidth(10, 150)

        self.tabla.setHorizontalHeaderLabels(["Nombre",
                                              "Usuario",
                                              "Contraseña",
                                              "Documento",
                                              "Correo",
                                              "Pregunta 1",
                                              "Pregunta 2",
                                              "Pregunta 3",
                                              "Respuesta 1",
                                              "Respuesta 2",
                                              "Respuesta 3"
                                              ])

        self.tabla.setRowCount(self.numeroUsuarios)

        for u in self.usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.nombreCompleto))
            # evitar que se deje modificar
            self.tabla.item(self.contador, 0).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.contrasena))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            # evitar que se deje modificar
            self.tabla.item(self.contador, 3).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.respuesta3))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta4))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.respuesta5))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta6))

            self.contador += 1

        self.scrollArea.setWidget(self.tabla)
        self.vertical.addWidget(self.scrollArea)

        self.vertical.addStretch()

        # Boton volver

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(100)
        self.botonVolver.setStyleSheet('background-color: #CCCCFF;'
                                          'color: black;'
                                          'padding: 10px;'
                                          'margin-top: 10px;'
                                          'margin-left: 0px;'
                                          )

        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        # Se agrega el boton al layout vertical

        self.vertical.addWidget(self.botonVolver)

        self.fondo.setLayout(self.vertical)

    def metodo_botonVolver(self):
        self.hide()
        self.Anterior.show()

    def accion_delete(self):
        filaActual = self.tabla.currentRow()

        if filaActual < 0:
            return QMessageBox.warning(self, "Warning", "Para borrar, debe seleccionar un registro")

        boton = QMessageBox.question(
            self,
            'Confirmation',
            '¿Estas seguro de borrar este registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if boton == QMessageBox.StandardButton.Yes:

            if (
                    self.tabla.item(filaActual, 0).text() != '' and
                    self.tabla.item(filaActual, 1).text() != '' and
                    self.tabla.item(filaActual, 2).text() != '' and
                    self.tabla.item(filaActual, 3).text() != '' and
                    self.tabla.item(filaActual, 4).text() != '' and
                    self.tabla.item(filaActual, 5).text() != '' and
                    self.tabla.item(filaActual, 6).text() != '' and
                    self.tabla.item(filaActual, 7).text() != '' and
                    self.tabla.item(filaActual, 8).text() != '' and
                    self.tabla.item(filaActual, 9).text() != '' and
                    self.tabla.item(filaActual, 10).text() != ''
            ):
                self.file = open('datos/clientes.txt', 'rb')

                usuarios = []

                while self.file:
                    linea = self.file.readline().decode('UTF-8')
                    lista = linea.split(';')

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

                    usuarios.append(u)

                self.file.close()

                for u in usuarios:

                    if (
                            u.documento == self.tabla.item(filaActual, 3).text()
                    ):
                        usuarios.remove(u)
                        break

                self.file = open('datos/clientes.txt', 'wb')

                for u in usuarios:
                    self.file.write(bytes(u.nombreCompleto + ';' +
                                          u.usuario + ';' +
                                          u.contrasena + ';' +
                                          u.documento + ';' +
                                          u.correo + ';' +
                                          u.respuesta1 + ';' +
                                          u.respuesta2 + ';' +
                                          u.respuesta3 + ';' +
                                          u.respuesta4 + ';' +
                                          u.respuesta5 + ';' +
                                          u.respuesta6 + ';' + '\n', encoding='UTF-8'))
                self.file.close()

                # hacemos que la tabla no se vea en el registro

                self.tabla.removeRow(filaActual)

                return QMessageBox.question(
                    self,
                    'confirmation',
                    'El registro ha sido eliminado exitosamente.',
                    QMessageBox.StandardButton.Yes
                )
            else:
                # Hacemos que en la tabla no se vea el registro en caso de tratarse de na fila vacia
                self.tabla.removeRow(filaActual)

    def accion_agregar(self):
        ultimafila = self.tabla.rowCount()

        # insertas una fila nueva despues de la ultima fila
        self.tabla.insertRow(ultimafila)

        # LLenamos las celdas con espacios en blancos

        self.tabla.setItem(ultimafila, 0, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 1, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 2, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 3, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 4, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 5, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 6, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 7, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 8, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 9, QTableWidgetItem(''))
        self.tabla.setItem(ultimafila, 10, QTableWidgetItem(''))

    def accion_editar(self):

        filaActual = self.tabla.currentRow()

        if filaActual < 0:
            return QMessageBox.warning(
                self,
                'Warning',
                'Para ingresar debe seleccionar un registro.',

            )

        boton = QMessageBox.question(
            self,
            'Confirmation',
            '¿Seguro que quiere ingresar este nuevo registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        datosVacios = True

        if boton == QMessageBox.StandardButton.Yes:

            if (
                    self.tabla.item(filaActual, 0).text() != '' and
                    self.tabla.item(filaActual, 1).text() != '' and
                    self.tabla.item(filaActual, 2).text() != '' and
                    self.tabla.item(filaActual, 3).text() != '' and
                    self.tabla.item(filaActual, 4).text() != '' and
                    self.tabla.item(filaActual, 5).text() != '' and
                    self.tabla.item(filaActual, 6).text() != '' and
                    self.tabla.item(filaActual, 7).text() != '' and
                    self.tabla.item(filaActual, 8).text() != '' and
                    self.tabla.item(filaActual, 9).text() != '' and
                    self.tabla.item(filaActual, 10).text() != ''
            ):

                datosVacios = False

                self.file = open('datos/clientes.txt', 'rb')

                usuarios = []

                while self.file:
                    linea = self.file.readline().decode('UTF-8')
                    lista = linea.split(';')

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

                    usuarios.append(u)

                self.file.close()

                # variables controladoras si existe registro y si se va a editar
                existeRegistro = False
                existeDocumento = False

                for u in usuarios:

                    if (
                            u.nombreCompleto == self.tabla.item(filaActual, 0).text() and
                            u.usuario == self.tabla.item(filaActual, 1).text() and
                            u.contrasena == self.tabla.item(filaActual, 2).text() and
                            u.documento == self.tabla.item(filaActual, 3).text() and
                            u.correo == self.tabla.item(filaActual, 4).text() and
                            u.respuesta1 == self.tabla.item(filaActual, 5).text() and
                            u.respuesta2 == self.tabla.item(filaActual, 6).text() and
                            u.respuesta3 == self.tabla.item(filaActual, 7).text() and
                            u.respuesta4 == self.tabla.item(filaActual, 8).text() and
                            u.respuesta5 == self.tabla.item(filaActual, 9).text() and
                            u.respuesta6 == self.tabla.item(filaActual, 10).text()
                    ):
                        existeRegistro = True

                        return QMessageBox.warning(
                            self,
                            'Warning',
                            'Resgistro duplicado, no se pude registrar')
                        break

                if not existeRegistro:

                    for u in usuarios:

                        if (
                                u.documento == self.tabla.item(filaActual, 3).text()
                        ):

                            existeDocumento = True

                            u.nombreCompleto = self.tabla.item(filaActual, 0).text()
                            u.usuario = self.tabla.item(filaActual, 1).text()
                            u.contrasena = self.tabla.item(filaActual, 2).text()
                            u.documento = self.tabla.item(filaActual, 3).text()
                            u.correo = self.tabla.item(filaActual, 4).text()
                            u.respuesta1 = self.tabla.item(filaActual, 5).text()
                            u.respuesta2 = self.tabla.item(filaActual, 6).text()
                            u.respuesta3 = self.tabla.item(filaActual, 7).text()
                            u.respuesta4 = self.tabla.item(filaActual, 8).text()
                            u.respuesta5 = self.tabla.item(filaActual, 9).text()
                            u.respuesta6 = self.tabla.item(filaActual, 10).text()

                            self.file = open('datos/clientes.txt', 'wb')

                            for u in usuarios:
                                self.file.write(bytes(
                                    u.nombreCompleto + ';' +
                                    u.usuario + ';' +
                                    u.contrasena + ';' +
                                    u.documento + ';' +
                                    u.correo + ';' +
                                    u.respuesta1 + ';' +
                                    u.respuesta2 + ';' +
                                    u.respuesta3 + ';' +
                                    u.respuesta4 + ';' +
                                    u.respuesta5 + ';' +
                                    u.respuesta6 + ';' + '\n', encoding='UTF-8'
                                ))

                            self.file.close()

                            return QMessageBox.question(
                                self,
                                'Confirmation',
                                'Los datos del registro se han editados exitosamente.',
                                QMessageBox.StandardButton.Ok
                            )
                            break

                    if not existeDocumento:
                        self.file = open('datos/clientes.txt', 'ab')

                        self.file.write(bytes(
                            self.tabla.item(filaActual, 0).text() + ';' +
                            self.tabla.item(filaActual, 1).text() + ';' +
                            self.tabla.item(filaActual, 2).text() + ';' +
                            self.tabla.item(filaActual, 3).text() + ';' +
                            self.tabla.item(filaActual, 4).text() + ';' +
                            self.tabla.item(filaActual, 6).text() + ';' +
                            self.tabla.item(filaActual, 7).text() + ';' +
                            self.tabla.item(filaActual, 8).text() + ';' +
                            self.tabla.item(filaActual, 9).text() + ';' +
                            self.tabla.item(filaActual, 10).text() + ';' + '\n', encoding='UTF-8'))

                        self.file.seek(0, 2)
                        self.file.close()
                    return QMessageBox.question(
                        self,
                        'Confirmation',
                        'Los datos del registro se han ingresado correctamente.',
                        QMessageBox.StandardButton.Ok

                    )

            if datosVacios:
                return QMessageBox.warning(
                    self,
                    'Warning',
                    'Debe ingresar todos los datos en el registro'
                )
