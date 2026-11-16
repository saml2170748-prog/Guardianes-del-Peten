from animal import Animal
class GuacamayaRoja(Animal):
      def __init__(self, codigo, nombre, envergadura_cm=100):
          super().__init__(codigo, nombre, "guacamaya roja", True)
          self.envergadura_cm = 100 if envergadura_cm is None else envergadura_cm
      def mostrar_datos(self):
          return super().mostrar_datos() + f" | envergadura_cm: {self.envergadura_cm}"
      def volar(self):
          return "La guacamaya roja vuela: " + self.nombre


      def describir(self):
          return (
               f"{self.nombre} es una guacamaya roja; come semillas y frutos, "
               f"vive en el dosel del bosque y vuela; su envergadura es {self.envergadura_cm} cm."
          )
