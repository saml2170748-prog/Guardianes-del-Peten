from animal import Animal
class Jaguar(Animal):
     def __init__(self, codigo, nombre, territorio_km2=40):
         super().__init__(codigo, nombre, "jaguar", True)
         self.territorio_km2 = 40 if territorio_km2 is None else territorio_km2
     def mostrar_datos(self):
         return super().mostrar_datos() + f" | territorio_km2: {self.territorio_km2}"
     def rugir(self):
         return "Rugido de jaguar: " + self.nombre


     def describir(self):
         return (
              f"{self.nombre} es un jaguar carnívoro; caza en la selva del Petén, "
              f"se desplaza caminando y nadando y vigila {self.territorio_km2} km² de territorio."
         )
