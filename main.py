from pruebas_entrega5 import ejecutar_pruebas_entrega5
from animal import Animal
from sistema_monitoreo import SistemaMonitoreo
def main():
     s = SistemaMonitoreo()
     hora = "2026-10-11 18:30"
     print("=== GUARDIANES DEL PETÉN - ENTREGA 3 ===")
     for nombre, tipo in [("Laguna del Tigre", "núcleo"),
                             ("Mirador-Río Azul", "núcleo"),
                             ("El Remate", "amortiguamiento"),
                             ("Uaxactún", "uso múltiple")]:
         s.registrar_zona(nombre, tipo)
     s.registrar_guardarrecursos("GR-07", "Mateo Chayax")
     s.registrar_guardarrecursos("GR-08", "Lucía Pérez")
     s.establecer_turno("GR-07")
     for codigo, nivel in [("GPS-01", 80), ("GPS-02", 5), ("GPS-03", 65)]:
         s.registrar_collar(codigo, nivel)
     print("\nA. REGISTRAR ANIMAL")
     for datos in [("JAG-001", "Balam", "jaguar", True),
                    ("TAP-001", "Tziquin", "tapir", True),
                    ("GUA-001", "Ixchel", "guacamaya roja", True),
                    ("COC-001", "Chak", "cocodrilo de pantano", False),
                    ("MON-001", "Kuk", "mono aullador", False)]:
         s.registrar_animal(*datos)
     s.registrar_animal("jag001", "Otro", "jaguar", True)
     s.registrar_animal("JAG-001", "Repetido", "jaguar", True)
     s.registrar_animal("TAP-002", "Otro", "tapir", False)
     print("\nB. ASIGNAR COLLAR")











     s.asignar_collar("GPS-01", "JAG-001")
     s.asignar_collar("GPS-02", "TAP-001")
     s.asignar_collar("NO-EXISTE", "JAG-001")
     s.asignar_collar("GPS-01", "GUA-001")
     s.asignar_collar("GPS-03", "JAG-001")
     s.asignar_collar("GPS-03", "GUA-001")
     print("\nC. REPORTAR POSICIÓN")
     s.reportar_posicion("GPS-01", "Laguna del Tigre", hora)
     s.reportar_posicion("GPS-01", "Uaxactún", hora)    # AL-001 alta.
     s.reportar_posicion("GPS-02", "El Remate", hora)    # AL-002 media.
     s.reportar_posicion("GPS-03", "Zona desconocida", hora)
     s.reportar_posicion("NO-EXISTE", "Uaxactún", hora)
     s.reportar_posicion("GPS-03", "El Remate", "2026-02-30 25:00")
     print("\nD. REGISTRAR AVISTAMIENTO")
     s.registrar_avistamiento("GR-07", "COC-001", "El Remate", hora)
     s.registrar_avistamiento("GR-08", "MON-001", "Uaxactún", hora)
     s.registrar_avistamiento("gr7", "COC-001", "El Remate", hora)
     s.registrar_avistamiento("GR-07", "COC-999", "El Remate", hora)
     s.registrar_avistamiento("GR-07", "COC-001", "Zona desconocida", hora)
     print("\nE. ATENDER ALERTA")
     s.atender_alerta("AL-001", "GR-07", "2026-10-11 19:00")
     s.atender_alerta("AL-001", "GR-08", "2026-10-11 19:10")
     s.atender_alerta("AL-999", "GR-07", hora)


     print("\nCASO ESCONDIDO: CAMBIAR BATERÍA")
     s.cambiar_bateria("GPS-02", "GR-07", 100, "2026-10-11 19:30")
     s.cambiar_bateria("GPS-02", "GR-07", 101, hora)
     s.cambiar_bateria("GPS-02", "GR7", 80, hora)
     s.cambiar_bateria("GPS-99", "GR-07", 80, hora)
     s.cambiar_bateria("GPS-02", "GR-07", 80, "hora inválida")
     s.reportar_posicion("GPS-02", "El Remate", "2026-10-11 19:35")
     print("\nF. CONSULTAR MOVIMIENTOS")
     s.consultar_movimientos("JAG-001")
     s.consultar_movimientos("GUA-001")    # Existe, sin lecturas.
     s.consultar_movimientos("JAG-999")
     print("\nG. PRUEBAS ANTERIORES DE HERENCIA")
     for animal in s.animales:
         print("Heredado sin cambios:", animal.consultar_collar())
         print("Sobrescrito con super():", animal.mostrar_datos())
         if hasattr(animal, "rugir"):
              print("Propio:", animal.rugir())
         elif hasattr(animal, "nadar"):
              print("Propio:", animal.nadar())
         elif hasattr(animal, "volar"):
              print("Propio:", animal.volar())
         elif hasattr(animal, "sumergirse"):
              print("Propio:", animal.sumergirse())
         elif hasattr(animal, "aullar"):
              print("Propio:", animal.aullar())
     print("\nRESUMEN FINAL")
     s.listar_alertas_pendientes()
     print(f"Zonas: {len(s.zonas)} | Animales: {len(s.animales)} | Collares: {len(s.collares)}")
     print(f"Lecturas: {len(s.lecturas)} | Alertas: {len(s.alertas)} | Cambios: {len(s.cambios_bateria)}")
     print(f"SMS simulados: {len(s.sms.envios)}")
     # Entrega 3: mismo mensaje, distintas implementaciones.
     print("\n=== CICLO POLIMORFICO: CINCO ESPECIES ===")
     for animal in s.animales:











         print(animal.describir())


     print("\n=== INTENTO DE INSTANCIAR ANIMAL ABSTRACTA ===")
     try:
         Animal("GEN-001", "Ejemplo", "animal", False)
     except TypeError as error:
         print(f"TypeError: {error}")


     print("\n=== ENTREGA 5: RECURSIVIDAD ===")
     ejecutar_pruebas_entrega5()

if __name__ == "__main__":
     main()
