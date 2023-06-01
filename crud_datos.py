import math
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QWidget, QButtonGroup, QGridLayout, QScrollArea

from cliente import Cliente
from consulta_datos_tabular import Consulta_datos_tabular


class Crud_datos(QMainWindow):
    def __init__(self, anterior, cedula):
        super().__init__()

        self.Anterior = anterior
        self.cedulaUsuario = cedula
        # creacion de la ventana
        self.setWindowTitle("Editar usuario")
        self.setWindowIcon(QtGui.QIcon('imagenes/icos.jpg'))
        self.ancho = 900
        self.alto = 650
        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.fondo.setStyleSheet('background-color: grey;')
        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # ------ latoyut izquierdo form-------

        self.layoutIzq_form = QFormLayout()

        # labels

        self.letrero1 = QLabel()
        self.letrero1.setText("Editar cliente")
        self.letrero1.setFont(QFont("Arial", 20))

        self.letrero2 = QLabel()
        self.letrero2.setFixedWidth(355)
        self.letrero2.setText("Por favor ingrese la informacion del cliente\n"
                              "en el formulario de abajo, los campos marcados\n"
                              "con asterisco son obligatorios.")
        self.letrero2.setFont(QFont("Arial", 10))
        self.letrero2.setStyleSheet('color: black; margin-bottom: 40px;'
                                    'margin-top: 25px;'
                                    'padding-bottom: 10;'
                                    'border: 2px solid black;'
                                    'border-left: none;'
                                    'border-right: none;'
                                    'border-top: none;'
                                    )

        # labels y campos
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)
        self.nombreCompleto.setStyleSheet('background-color: white;')

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)
        self.usuario.setStyleSheet('background-color: white;')

        self.contrasena = QLineEdit()
        self.contrasena.setFixedWidth(250)
        self.contrasena.setEchoMode(QLineEdit.Password)
        self.contrasena.setStyleSheet('background-color: white;')

        self.confirmar_contrasena = QLineEdit()
        self.confirmar_contrasena.setFixedWidth(250)
        self.confirmar_contrasena.setEchoMode(QLineEdit.Password)
        self.confirmar_contrasena.setStyleSheet('background-color: white;')

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)
        self.documento.setMaxLength(10)
        self.documento.setStyleSheet('background-color: white;')

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)
        self.correo.setStyleSheet('background-color: white;')

        # Creacion de botones limpiar y registrar

        self.botonEditar = QPushButton("Editar")
        self.botonEditar.setFixedWidth(90)
        self.botonEditar.setStyleSheet('background-color: #CCCCFF;'
                                          'color: black;'
                                          'padding: 10px;'
                                          'margin-top: 10px;'
                                          'margin-left: 0px;'
                                          )
        self.botonEditar.clicked.connect(self.accionEditar)

        self.botonlimpiar = QPushButton("Limpiar")
        self.botonlimpiar.setFixedWidth(90)
        self.botonlimpiar.setStyleSheet('background-color: #CCCCFF;'
                                          'color: black;'
                                          'padding: 10px;'
                                          'margin-top: 10px;'
                                          'margin-left: 0px;'
                                          )
        self.botonlimpiar.clicked.connect(self.accionLimpiar)

        self.botonEliminar = QPushButton("Eliminar")
        self.botonEliminar.setFixedWidth(90)
        self.botonEliminar.setStyleSheet('background-color: #CCCCFF;'
                                          'color: black;'
                                          'padding: 10px;'
                                          'margin-top: 10px;'
                                          'margin-left: 0px;'
                                          )
        self.botonEliminar.clicked.connect(self.accionEliminar)

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(90)
        self.botonVolver.setStyleSheet('background-color: #CCCCFF;'
                                          'color: black;'
                                          'padding: 10px;'
                                          'margin-top: 10px;'
                                          'margin-left: 0px;'
                                          )
        self.botonVolver.clicked.connect(self.accionVolver)

        # ----Agregamos al layout izquierdo----
        self.layoutIzq_form.addRow(self.letrero1)
        self.layoutIzq_form.addRow(self.letrero2)
        self.layoutIzq_form.addRow("Nombre completo*", self.nombreCompleto)
        self.layoutIzq_form.addRow("Ingrese usuario*", self.usuario)
        self.layoutIzq_form.addRow("Ingrese contraseña*", self.contrasena)
        self.layoutIzq_form.addRow("Confirmar contraseña*", self.confirmar_contrasena)
        self.layoutIzq_form.addRow("Documento ID*", self.documento)
        self.layoutIzq_form.addRow("Correo*", self.correo)
        self.layoutIzq_form.addRow(self.botonEditar, self.botonlimpiar)
        self.layoutIzq_form.addRow(self.botonEliminar)
        self.layoutIzq_form.addRow(self.botonVolver)

        self.horizontal.addLayout(self.layoutIzq_form)

        # ---------Layout formulario lado derecho------------
        self.layoutDer_form = QFormLayout()
        self.layoutDer_form.setContentsMargins(100, 0, 0, 0)

        # letreros de informacion derecho
        self.letrero3 = QLabel()
        self.letrero3.setFixedWidth(355)
        self.letrero3.setText("Recuperar Contraseña")
        self.letrero3.setFont(QFont("Arial", 20))
        self.letrero3.setStyleSheet('color: black;')

        self.letrero4 = QLabel()
        self.letrero4.setFixedWidth(355)
        self.letrero4.setText("Por favor ingrese la información para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asterisco son obligatorios."
                              )
        self.letrero4.setFont(QFont("Arial", 10))
        self.letrero4.setStyleSheet('color: black; margin-bottom: 25px;'
                                    'margin-top: 15px;'
                                    'padding-bottom: 10;'
                                    'border: 2px solid black;'
                                    'border-left: none;'
                                    'border-right: none;'
                                    'border-top: none;'
                                    )

        # Labels y campos lado derecho (preguntas y respuestas)

        # Labels
        self.pregunta1 = QLabel("Pregunta de verificacion 1*")
        self.pregunta2 = QLabel("Pregunta de verificacion 2*")
        self.pregunta3 = QLabel("Pregunta de verificacion 3*")
        self.pregunta4 = QLabel("Respuesta de verificacion 1*")
        self.pregunta5 = QLabel("Respuesta de verificacion 2*")
        self.pregunta6 = QLabel("Respuesta de verificacion 3*")

        # campos QlineEdits
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(250)
        self.respuesta1.setStyleSheet('background-color: white;')

        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(250)
        self.respuesta2.setStyleSheet('background-color: white;')

        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(250)
        self.respuesta3.setStyleSheet('background-color: white;')

        self.respuesta4 = QLineEdit()
        self.respuesta4.setFixedWidth(250)
        self.respuesta4.setStyleSheet('background-color: white;')

        self.respuesta5 = QLineEdit()
        self.respuesta5.setFixedWidth(250)
        self.respuesta5.setStyleSheet('background-color: white;')

        self.respuesta6 = QLineEdit()
        self.respuesta6.setFixedWidth(250)
        self.respuesta6.setStyleSheet('background-color: white;')

        # Creacion de boton buscar y recuperar

        # Se agrega al layout derecho
        self.layoutDer_form.addRow(self.letrero3)
        self.layoutDer_form.addRow(self.letrero4)

        self.layoutDer_form.addRow(self.pregunta1)
        self.layoutDer_form.addRow(self.respuesta1)

        self.layoutDer_form.addRow(self.pregunta2)
        self.layoutDer_form.addRow(self.respuesta2)

        self.layoutDer_form.addRow(self.pregunta3)
        self.layoutDer_form.addRow(self.respuesta3)

        self.layoutDer_form.addRow(self.pregunta4)
        self.layoutDer_form.addRow(self.respuesta4)

        self.layoutDer_form.addRow(self.pregunta5)
        self.layoutDer_form.addRow(self.respuesta5)

        self.layoutDer_form.addRow(self.pregunta6)
        self.layoutDer_form.addRow(self.respuesta6)

        self.horizontal.addLayout(self.layoutDer_form)

        self.fondo.setLayout(self.horizontal)

        # creamos ventana de dialogo
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ventanaDialogo.resize(300, 150)

        # crear boton para aceptar
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        # titulo
        self.ventanaDialogo.setWindowTitle("Formulario de registro")

        # configuracion modal
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # crear layout vertical
        self.vertical = QVBoxLayout()

        self.mensaje = QLabel("")
        self.mensaje.setStyleSheet('background-color: #008B45; color: #FFFFFF; padding: 10 px;')

        self.vertical.addWidget(self.mensaje)
        self.vertical.addWidget(self.opciones)
        self.ventanaDialogo.setLayout(self.vertical)

        # Linea para cargar los datos de los usuarios
        self.cargar_datos()

    def accionEditar(self):

        self.datosCorrectos = True

        self.ventanaDialogo.setWindowTitle("Formulario de edición")

        if (
                self.contrasena.text() != self.confirmar_contrasena.text()
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Las contraseñas no son igiuales.")
            self.ventanaDialogo.exec_()

        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.contrasena.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.respuesta1.text() == ''
                or self.respuesta2.text() == ''
                or self.respuesta3.text() == ''
                or self.respuesta4.text() == ''
                or self.respuesta5.text() == ''
                or self.respuesta6.text() == ''
        ):
            self.datosCorrectos = False
            self.mensaje.setText("Debe seleccionar un usario con documento válido")
            self.ventanaDialogo.exec_()

            self.accionVolver()

        if self.datosCorrectos:

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

            existeDocumento = False

            for u in usuarios:

                if int(u.documento) == self.cedulaUsuario:
                    u.usuario = self.usuario.text()
                    u.contrasena = self.contrasena.text()
                    u.correo = self.correo.text()
                    u.respuesta1 = self.respuesta1.text()
                    u.respuesta2 = self.respuesta2.text()
                    u.respuesta3 = self.respuesta3.text()
                    u.respuesta4 = self.respuesta4.text()
                    u.respuesta5 = self.respuesta5.text()
                    u.respuesta6 = self.respuesta6.text()

                    existeDocumento = True
                    break

            if (
                    not existeDocumento
            ):
                self.mensaje.setText(f"No existe usuario con ese numero de documento\n"
                                     f"{self.cedulaUsuario}")
                self.ventanaDialogo.exec_()

            # Abrimos el archivo en modo agregar
            self.file = open('datos/clientes.txt', 'wb')

            for u in usuarios:
                # trae el texto de los Qline y los concatena
                self.file.write(bytes(u.nombreCompleto + ";" +
                                      u.usuario + ";" +
                                      u.contrasena + ";" +
                                      u.documento + ";" +
                                      u.correo + ";" +
                                      u.respuesta1 + ";" +
                                      u.respuesta2 + ";" +
                                      u.respuesta3 + ";" +
                                      u.respuesta4 + ";" +
                                      u.respuesta5 + ";" +
                                      u.respuesta6 + ";" + "\n", encoding='UTF-8'))
            self.file.close()

            if (
                    existeDocumento
            ):
                self.mensaje.setText("Usuario actualizado correctamente!")
                self.ventanaDialogo.exec_()
                self.accionLimpiar()
                self.accionVolver()

            self.file = open('datos/clientes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()

    def accionLimpiar(self):

        self.nombreCompleto.setText("")
        self.usuario.setText("")
        self.contrasena.setText("")
        self.confirmar_contrasena.setText("")
        self.documento.setText("")
        self.correo.setText("")
        self.respuesta1.setText("")
        self.respuesta2.setText("")
        self.respuesta3.setText("")
        self.respuesta4.setText("")
        self.respuesta5.setText("")
        self.respuesta6.setText("")

    def accionEliminar(self):

        self.datosCorrectos = True
        self.eliminar = False

        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.contrasena.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.respuesta1.text() == ''
                or self.respuesta2.text() == ''
                or self.respuesta3.text() == ''
                or self.respuesta4.text() == ''
                or self.respuesta5.text() == ''
                or self.respuesta6.text() == ''
        ):
            self.datosCorrectos = False
            self.mensaje.setText("Debe seleccionar un usario con documento válido")
            self.ventanaDialogo.exec_()
            self.accionVolver()

        if self.datosCorrectos:



            self.ventanaDialogo_eliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

            self.ventanaDialogo_eliminar.resize(300, 150)

            self.ventanaDialogo_eliminar.setWindowModality(Qt.ApplicationModal)

            self.verticalEliminar = QVBoxLayout()

            self.mensajeEliminar = QLabel("¿Estas seguro que desea eliminar este registro de usuario?")
            self.mensajeEliminar.setStyleSheet('background-color: #008B45; color: #FFFFFF; padding: 10 px;')

            self.verticalEliminar.addWidget(self.mensajeEliminar)

            # agregar las opciones de los bontes ok y cancel

            self.opcionesEliminar = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            self.opcionesBox = QDialogButtonBox(self.opcionesEliminar)

            self.opcionesBox.accepted.connect(self.ok_opcion)
            self.opcionesBox.rejected.connect(self.cancel_opcion)

            # agergamos opcionBox
            self.verticalEliminar.addWidget(self.opcionesBox)

            self.ventanaDialogo_eliminar.setLayout(self.verticalEliminar)

            self.ventanaDialogo_eliminar.exec_()

            if self.eliminar:

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
                        lista[10],
                    )
                    usuarios.append(u)
                self.file.close()

                existeDocumento = False

                # ciclo for para remover el registro de un usuario
                for u in usuarios:

                    if int(u.documento) == self.cedulaUsuario:
                        usuarios.remove(u)
                        existeDocumento = True
                        break

                self.file = open('datos/clientes.txt', 'wb')

                # reescribir el registro del usuario a vacio

                for u in usuarios:
                    self.file.write(bytes(u.nombreCompleto + ';'
                                          + u.usuario + ';'
                                          + u.contrasena + ';'
                                          + u.documento + ';'
                                          + u.correo + ';'
                                          + u.respuesta1 + ';'
                                          + u.respuesta2 + ';'
                                          + u.respuesta3 + ';'
                                          + u.respuesta4 + ';'
                                          + u.respuesta5 + ';'
                                          + u.respuesta6 + ';' + '\n', encoding='UTF-8'))
                self.file.close()

                if existeDocumento:
                    self.mensaje.setText("Usuario eliminado correctamente.")
                    self.ventanaDialogo.exec_()
                    self.accionLimpiar()
                    self.accionVolver()

    def ok_opcion(self):
        self.ventanaDialogo_eliminar.close()
        self.eliminar = True

    def cancel_opcion(self):
        self.ventanaDialogo_eliminar.close()

    def accionVolver(self):
        self.hide()
        self.Anterior.show()

    def cargar_datos(self):

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

        existeDocumento = False

        for u in usuarios:

            if int(u.documento) == self.cedulaUsuario:
                self.nombreCompleto.setText(u.nombreCompleto)
                # linea para no se deje editar
                self.nombreCompleto.setReadOnly(True)
                self.usuario.setText(u.usuario)
                self.contrasena.setText(u.contrasena)
                self.confirmar_contrasena.setText(u.contrasena)
                self.documento.setText(u.documento)
                self.documento.setReadOnly(True)
                self.correo.setText(u.correo)
                self.respuesta1.setText(u.respuesta1)
                self.respuesta2.setText(u.respuesta2)
                self.respuesta3.setText(u.respuesta3)
                self.respuesta4.setText(u.respuesta4)
                self.respuesta5.setText(u.respuesta5)
                self.respuesta6.setText(u.respuesta6)

                # se indica que se encuentra el documento
                existeDocumento = True
                break

        if (
                not existeDocumento
        ):
            self.mensaje.setText("No existe usuario con ese documento:\n"
                                 + str(self.cedulaUsuario))

            self.ventanaDialogo.exec_()
            self.accionVolver()



