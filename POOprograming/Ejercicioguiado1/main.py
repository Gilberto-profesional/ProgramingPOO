from empleado import Gerente, Tecnicos, Gestores, Administrador
from reportes import ReportesContabilidad, ReportesEmpleados, ReportesProgramacion
from programacion import Matutino, Vespertino

if __name__ == "__main__":

    empleados=[
    Gerente("Roberto","Martinez", "20,000.00", Matutino()),
    Gestores("Alejandra","Gomez  ", "8,000.00", Matutino()),
    Gestores("Selene","Rodriguez", "8,000.00", Matutino()),
    Tecnicos("Artemio","Cardenas", "9,000.00",Vespertino()),
    Tecnicos("Salvador","Magaña", "9,000.00",Vespertino()),
    Tecnicos("Rolando","Requenes", "9,000.00",Matutino()),
    Administrador("Marco","Magallanes", "15,000.00",Matutino()),
    ]

    reportes=[
        ReportesContabilidad(empleados),
        ReportesEmpleados(empleados),
        ReportesProgramacion(empleados)
    ]

    for r in reportes:
        r.print_reporte()



