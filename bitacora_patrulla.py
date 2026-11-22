class BitacoraPatrulla:
    """LIFO: la anotación más reciente se deshace primero."""

    def __init__(self):
        self._entradas = []

    def registrar(self, entrada):
        self._entradas.append(entrada)

    def deshacer(self):
        if self.esta_vacia():
            return None
        return self._entradas.pop()

    def ultima(self):
        if self.esta_vacia():
            return None
        return self._entradas[-1]

    def esta_vacia(self):
        return len(self._entradas) == 0

    def mostrar(self):
        if self.esta_vacia():
            print('Bitácora vacía')
            return
        for numero, entrada in enumerate(reversed(self._entradas), start=1):
            print(f'{numero}. {entrada}')
