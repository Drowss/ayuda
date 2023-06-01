import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout

from cliente import Cliente
from consulta_datos import Consulta_datos


class Ventana1(QMainWindow):
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # creacion de la ventana
        self.setWindowTitle("Formulario de registro")
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
        self.imagenFondo = QPixmap('imagenes/stuillorando.png')
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)

        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

        # creacion de layout horizontal para la distribucion
        self.horizontal = QHBoxLayout()

        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # ---------Creacion del layout izquierdo---------
        self.layoutIzq_form = QFormLayout()

        # hacemos los labels informativos
        self.letrero1 = QLabel()
        self.letrero1.setText("Información del cliente")
        self.letrero1.setFont(QFont("Arial", 20))
        self.letrero1.setStyleSheet('color: black;')

        self.letrero2 = QLabel()
        self.letrero2.setFixedWidth(355)
        self.letrero2.setText("Por favor ingrese la información del cliente"
                              "\nen el formulario de abajo. los campos marcados"
                              "\ncon asterisco son obligatorios."
                              )
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

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        self.contrasena = QLineEdit()
        self.contrasena.setFixedWidth(250)
        self.contrasena.setEchoMode(QLineEdit.Password)

        self.confirmar_contrasena = QLineEdit()
        self.confirmar_contrasena.setFixedWidth(250)
        self.confirmar_contrasena.setEchoMode(QLineEdit.Password)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)
        self.documento.setMaxLength(10)

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)
        # Creacion de botones limpiar y registrar

        self.botonregistrar = QPushButton("Registrar")
        self.botonregistrar.setFixedWidth(90)
        self.botonregistrar.setStyleSheet('background-color: #CCCCFF;'
                                          'color: black;'
                                          'padding: 10px;'
                                          'margin-top: 10px;'
                                          'margin-left: 0px;'
                                          )
        self.botonregistrar.clicked.connect(self.accionRegistrar)

        self.botonlimpiar = QPushButton("Limpiar")
        self.botonlimpiar.setFixedWidth(90)
        self.botonlimpiar.setStyleSheet('background-color: #CCCCFF;'
                                          'color: black;'
                                          'padding: 10px;'
                                          'margin-top: 10px;'
                                          'margin-left: 0px;'
                                          )
        self.botonlimpiar.clicked.connect(self.accionLimpiar)

        # Se agrega todo al layout formulario izquierdo
        self.layoutIzq_form.addRow(self.letrero1)
        self.layoutIzq_form.addRow(self.letrero2)
        self.layoutIzq_form.addRow("Nombre completo*", self.nombreCompleto)
        self.layoutIzq_form.addRow("Ingrese usuario*", self.usuario)
        self.layoutIzq_form.addRow("Ingrese contraseña*", self.contrasena)
        self.layoutIzq_form.addRow("Confirmar contraseña*", self.confirmar_contrasena)
        self.layoutIzq_form.addRow("Documento ID*", self.documento)
        self.layoutIzq_form.addRow("Correo*", self.correo)
        self.layoutIzq_form.addRow(self.botonregistrar, self.botonlimpiar)

        # Agregamos layout formulario al layout horizontal
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

        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(250)

        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(250)

        self.respuesta4 = QLineEdit()
        self.respuesta4.setFixedWidth(250)

        self.respuesta5 = QLineEdit()
        self.respuesta5.setFixedWidth(250)

        self.respuesta6 = QLineEdit()
        self.respuesta6.setFixedWidth(250)

        # Creacion de boton buscar y recuperar

        self.botonBuscar = QPushButton("Buscar")
        self.botonBuscar.setFixedWidth(90)
        self.botonBuscar.setStyleSheet('background-color: #CCCCFF;'
                                          'color: black;'
                                          'padding: 10px;'
                                          'margin-top: 10px;'
                                          'margin-left: 0px;'
                                          )
        self.botonBuscar.clicked.connect(self.accionBuscar)

        self.botonRecuperar = QPushButton("Recuperar")
        self.botonRecuperar.setFixedWidth(140)
        self.botonRecuperar.setStyleSheet('background-color: #CCCCFF;'
                                          'color: black;'
                                          'padding: 10px;'
                                          'margin-top: 10px;'
                                          'margin-left: 0px;'
                                          )
        self.botonRecuperar.clicked.connect(self.accionRecuperar)




        self.botonContinuar = QPushButton("Continuar")
        self.botonContinuar.setFixedWidth(90)
        self.botonContinuar.setStyleSheet('background-color: #CCCCFF;'
                                          'color: black;'
                                          'padding: 10px;'
                                          'margin-top: 10px;'
                                          'margin-left: 0px;'
                                          )
        self.botonContinuar.clicked.connect(self.accion_botonContinuar)



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

        self.layoutDer_form.addRow(self.botonBuscar, self.botonRecuperar)
        self.layoutDer_form.addRow(self.botonContinuar)

        self.horizontal.addLayout(self.layoutDer_form)

        # --------Layout que almacena toda la ventana----------
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



    def accionLimpiar(self):

        # datos correctos
        self.datosCorrectos = True

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

    def accionRegistrar(self):

        # datos correctos
        self.datosCorrectos = True

        # Validacion de passwords
        if (
                self.contrasena.text() != self.confirmar_contrasena.text()
        ):
            self.datosCorrectos = False
            self.mensaje.setText("Las contraseñas no son iguales")
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
            self.mensaje.setText("Debe ingresar todos los campos")
            self.ventanaDialogo.exec_()

        # si los datos estan correctos
        if self.datosCorrectos:
            # Abrimos el archivo en modo agregar
            self.file = open('datos/clientes.txt', 'ab')

            # trae el texto de los Qline y los concatena
            self.file.write(bytes(self.nombreCompleto.text() + ";" +
                                  self.usuario.text() + ";" +
                                  self.contrasena.text() + ";" +
                                  self.documento.text() + ";" +
                                  self.correo.text() + ";" +
                                  self.respuesta1.text() + ";" +
                                  self.respuesta2.text() + ";" +
                                  self.respuesta3.text() + ";" +
                                  self.respuesta4.text() + ";" +
                                  self.respuesta5.text() + ";" +
                                  self.respuesta6.text() + ";" + "\n", encoding='UTF-8'))
            self.file.close()

            self.file = open('datos/clientes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()

    def accionBuscar(self):

        # datos correctos
        self.datosCorrectos = True

        # ttulo ventana
        self.ventanaDialogo.setWindowTitle("Buscar preguntas de validación")

        # condicionales de campos
        # ingresa el documento
        if (
                self.documento.text() == ''

        ):
            self.datosCorrectos = False
            self.mensaje.setText("si va a buscar preguntas "
                                 "para recuperar la contraseña.\n"
                                 "Debe primero,ingresar el documento")
            self.ventanaDialogo.exec_()

        # documento es numerico

        if (
                not self.documento.text().isnumeric()
        ):
            self.datosCorrectos = False
            self.mensaje.setText("Ingrese solo numeros en el documento")
            self.ventanaDialogo.exec_()

            self.documento.setText('')

        if (
                self.datosCorrectos
        ):

            self.file = open('datos/clientes.txt', 'rb')
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                # obtenemos del string una lista con 11 datos separados por;
                lista = linea.split(";")

                # paramos el bucle si ya no encuentra mas registros en el archivo
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

                # metemos el objeto en la lista de usuarios
                usuarios.append(u)

            # cerramos ael archivo txt
            self.file.close()

            # en este punto tenemos la lista de usuarios con todos los usuarios

            existeDocumento = False

            # buscamos en la lista de usuarios si existe la cedula

            for u in usuarios:
                """comparamos el documento ingresado:
                si correspopnde con el documento, es el usuario correcto:"""

                if u.documento == self.documento.text():
                    # aqui mostramos las preguntas del formulario
                    self.respuesta1.setText(u.respuesta1)
                    self.respuesta2.setText(u.respuesta2)
                    self.respuesta3.setText(u.respuesta3)

                    # indicamos que existen
                    existeDocumento = True

                    break

            # si no existe usuario con este documento
            if (
                    not existeDocumento
            ):
                self.mensaje.setText(f"No existe usuario con este numero"
                                     f"de documento.{self.documento.text()}")
                self.ventanaDialogo.exec_()

    def accionRecuperar(self):

        self.datosCorrectos = True

        self.ventanaDialogo.setWindowTitle("Recuperar contraseña")

        if (
                self.respuesta1.text() == '' or
                self.respuesta2.text() == '' or
                self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Para recuperar la contraseña debe:"
                                 "\nbuscar las preguntas de verificación."
                                 "\n\nPrimero ingrese su documento y luego"
                                 "\npresione el boton 'buscar'.")

            self.ventanaDialogo.exec_()

        # Validamos si se buscaron las preguntas pero no se ingresaron las respuestas
        if (
                self.respuesta1.text() != '' and
                self.respuesta4.text() == '' and
                self.respuesta2.text() != '' and
                self.respuesta5.text() == '' and
                self.respuesta3.text() != '' and
                self.respuesta6.text() == ''
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Para recuperar la contraseña debe:"
                                 "\nIngresar las respuestas a cada pregunta.")

            self.ventanaDialogo.exec_()

        # condicional si son correctos
        if (
                self.datosCorrectos
        ):

            # Abrimos el archivo en modo lectura
            linea = self.file = open('datos/clientes.txt', 'rb')

            # creamos Array lista vacia
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                # obtenemos el string una lista de 12 datos separados por ;
                lista = linea.split(";")

                if linea == '':
                    break

                # creamos un objeto tipo cliente llamado u

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

            # en este punto tenemos la lista con la lista de usuarios

            # variable para controlar si existe el documento

            existeDocumento = False

            resp4 = ''
            resp5 = ''
            resp6 = ''
            passw = ''

            # buscamos en la lista usuario por usuario si existe la cedula:
            for u in usuarios:
                if u.documento == self.documento.text():
                    existeDocumento = True

                    resp4 = u.respuesta4
                    resp5 = u.respuesta5
                    resp6 = u.respuesta6
                    passw = u.contrasena

                    break

            if (
                    self.respuesta4.text().lower().strip() == resp4.lower().strip() and
                    self.respuesta5.text().lower().strip() == resp5.lower().strip() and
                    self.respuesta6.text().lower().strip() == resp6.lower().strip()

            ):
                # limpiamos los campos
                self.accionLimpiar()

                self.mensaje.setText(f"Contraseña: {passw}")
                self.ventanaDialogo.exec_()

            else:
                self.mensaje.setText("Las respuesta son incorrectas"
                                     "\npara estas preguntas de recuperación."
                                     "\n\nVuelva a intentarlo.")

                self.ventanaDialogo.exec_()

    def accion_botonContinuar(self):
        self.hide()
        self.consulta_datos = Consulta_datos(self)
        self.consulta_datos.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana1 = Ventana1()
    ventana1.show()
    sys.exit(app.exec())
