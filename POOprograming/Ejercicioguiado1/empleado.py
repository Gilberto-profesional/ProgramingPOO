class Empleado:
    def __init__(self, nombre,apellido, salario,horario):
        self._nombre = nombre
        self._apellido= apellido
        self.salario = salario
        self.horario = horario

    def get_nombre_completo(self):
        NombreCompleto= self._nombre + " " + self._apellido
        return NombreCompleto   

class Gerente(Empleado):
    puesto = "Gerente general"

class Tecnicos(Empleado):
    puesto = "Tecnico"

class Gestores(Empleado):
    puesto = "Gestor de cobranzas"

class Administrador(Empleado):
    puesto = "Administrador de servicios de cable"
     