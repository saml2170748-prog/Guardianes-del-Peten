from animal import Animal
class MonoAullador(Animal):
     def __init__(self, codigo, nombre, altura_m=1):
         super().__init__(codigo, nombre, "mono aullador", False)
         self.altura_m = 1 if altura_m is None else altura_m
     def mostrar_datos(self):
         return super().mostrar_datos() + f" | altura_m: {self.altura_m}"
     def aullar(self):
         return "El mono aullador aúlla: " + self.nombre


     def describir(self):
         return (
              f"{self.nombre} es un mono aullador; come hojas y frutos, "
              f"habita las copas de los árboles y se mueve trepando; mide {self.altura_m} m de altura."
         )
