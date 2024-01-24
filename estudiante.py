# --INTEGRANTES--
# CROFFORD VILLAO FREDDY DARWIN
# ASENCIO MADESCO CARLOS ALEXIS
# GUSQUI PALLO MELANIE ANABEL
# MAXITANA MOREIRA HECTOR ALFREDO

class Estudiante:
    def __init__(self, nombre=None, email=None, semestre=None, cedula=None, edad=None,
                 estatura=None, peso=None, fecha_nacimiento=None):
        self._nombre = nombre
        self._email = email
        self._semestre = semestre
        self._cedula = cedula
        self._edad = edad
        self._estatura = estatura
        self._peso = peso
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor

    @property
    def semestre(self):
        return self._semestre

    @semestre.setter
    def semestre(self, valor):
        self._semestre = valor

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def estatura(self):
        return self._estatura

    @estatura.setter
    def estatura(self, estatura):
        self._estatura = estatura

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f'Estudiante: {self.__dict__.__str__()}'

