from animal import Animal
class CocodriloDePantano(Animal):
      def __init__(self, codigo, nombre, longitud_m=3):
          super().__init__(codigo, nombre, "cocodrilo de pantano", False)
          self.longitud_m = 3 if longitud_m is None else longitud_m
      def mostrar_datos(self):


          return super().mostrar_datos() + f" | longitud_m: {self.longitud_m}"
      def sumergirse(self):
          return "El cocodrilo se sumerge: " + self.nombre


      def describir(self):
          return (
               f"{self.nombre} es un cocodrilo de pantano carnívoro; come peces, "
               f"habita lagunas y humedales y se desplaza nadando y caminando; mide {self.longitud_m} m."
          )
