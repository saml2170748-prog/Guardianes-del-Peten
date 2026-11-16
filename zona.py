class Zona:
    TIPOS_VALIDOS = ('núcleo', 'amortiguamiento', 'uso múltiple')

    def __init__(self, nombre, tipo):
        if tipo not in self.TIPOS_VALIDOS:
            raise ValueError('R5: tipo de zona inválido')
        self.nombre = nombre
        self.tipo = tipo
        self.subzonas = []
        self.animales = []

    def agregar_subzona(self, zona):
        if not isinstance(zona, Zona):
            raise TypeError('R5: la subzona debe ser una Zona')
        if zona.tipo not in self.TIPOS_VALIDOS:
            raise ValueError('R5: tipo de subzona inválido')
        if zona is self or zona._contiene(self):
            raise ValueError('No se permite crear ciclos de zonas')
        if zona in self.subzonas:
            raise ValueError('La subzona ya fue agregada')
        self.subzonas.append(zona)

    def _contiene(self, objetivo):
        if self is objetivo:
            return True
        for subzona in self.subzonas:
            if subzona._contiene(objetivo):
                return True
        return False

    def ubicar(self, animal):
        if animal not in self.animales:
            self.animales.append(animal)

    def mostrar(self, nivel=0):
        print('  ' * nivel + f'{self.nombre} ({self.tipo}) - {len(self.animales)} animal(es) directo(s)')
        for subzona in self.subzonas:
            subzona.mostrar(nivel + 1)

    def contar_animales(self):
        total = len(self.animales)
        for subzona in self.subzonas:
            total += subzona.contar_animales()
        return total

    def buscar_sector(self, nombre):
        if self.nombre == nombre:
            return self
        for subzona in self.subzonas:
            encontrada = subzona.buscar_sector(nombre)
            if encontrada is not None:
                return encontrada
        return None
