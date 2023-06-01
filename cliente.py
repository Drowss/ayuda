class Cliente:
    def __init__(self, nombreCompleto, usuario, contrasena, documento, correo, respuesta1, respuesta2, respuesta3, respuesta4, respuesta5, respuesta6):
        self.nombreCompleto = nombreCompleto
        self.usuario = usuario
        self.contrasena = contrasena
        self.documento = documento
        self.correo = correo
        self.respuesta1 = respuesta1
        self.respuesta2 = respuesta2
        self.respuesta3 = respuesta3
        self.respuesta4 = respuesta4
        self.respuesta5 = respuesta5
        self.respuesta6 = respuesta6

    def __str__(self):
        return f"Nombre: {self.nombreCompleto} Documento: {self.documento}"

