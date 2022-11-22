class Reportes:
    def __init__(self, lista_empleados):
        self._lista_empleados = lista_empleados

class ReportesContabilidad(Reportes):

    def print_reporte(self):
        print(" ")
        print("Reporte de contabilidad")
        print("--------------------")
        for e in self._lista_empleados:
            print(f'Su nombre es {e.get_nombre_completo()} y gana {e.salario}')

class ReportesEmpleados(Reportes):

    def print_reporte(self):
        print(" ")
        print("Reporte de empleados")
        print("--------------------")
        for e in self._lista_empleados:
            print(f'Su nombre es {e.get_nombre_completo()} y es {e.puesto}')

class ReportesProgramacion(Reportes):

    def print_reporte(self):
        print(" ")
        print("Reporte de programacion")
        print("--------------------")
        for e in self._lista_empleados:
            print(f'Su nombre es {e.get_nombre_completo()} y su horario es {e.horario.get_programacion_info()}')
