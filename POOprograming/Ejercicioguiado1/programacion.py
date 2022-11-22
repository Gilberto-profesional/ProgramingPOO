import datetime

class Programacion:
    def get_programacion_info(self):
        return f'{self._hora_entra:%H:%M} {self._hora_salida:%H:%M} '


class Matutino(Programacion):
    def __init__(self):
        self._hora_entra = datetime.time(8,0)
        self._hora_salida = datetime.time(16,0)



class Vespertino(Programacion):
    def __init__(self):
        self._hora_entra = datetime.time(12,0)
        self._hora_salida = datetime.time(20,0)