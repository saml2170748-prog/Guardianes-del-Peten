from animal import Animal
class Tapir(Animal):
     def __init__(self, codigo, nombre, peso_kg=220):
         super().__init__(codigo, nombre, "tapir", True)
         self.peso_kg = 220 if peso_kg is None else peso_kg
     def mostrar_datos(self):
         return super().mostrar_datos() + f" | peso_kg: {self.peso_kg}"
     def nadar(self):











          return "El tapir nada en el río: " + self.nombre


     def describir(self):
         return (
              f"{self.nombre} es un tapir herbívoro; come hojas y frutos, "
              f"habita bosques húmedos y camina y nada; pesa {self.peso_kg} kg."
         )
