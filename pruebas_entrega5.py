"""Prueba de Entrega 5; se puede ejecutar por separado sin alterar el main.py previo.
Después de comprobarla, llamar a ejecutar_pruebas_entrega5() desde el main.py existente.
"""
from zona import Zona
from jaguar import Jaguar
from tapir import Tapir
from guacamaya_roja import GuacamayaRoja
from cocodrilo_de_pantano import CocodriloDePantano
from mono_aullador import MonoAullador
from sistema_monitoreo import SistemaMonitoreo


def ejecutar_pruebas_entrega5():
    sistema = SistemaMonitoreo()

    # Primer nivel, segundo nivel y tercer nivel debajo de la reserva.
    laguna = Zona('Laguna del Tigre', 'núcleo')
    mirador = Zona('Mirador-Río Azul', 'núcleo')
    sector_norte = Zona('Sector Norte', 'núcleo')
    sector_sur = Zona('Sector Sur', 'núcleo')
    aguada_escondida = Zona('Aguada Escondida', 'núcleo')
    aguada_ceiba = Zona('Aguada de la Ceiba', 'núcleo')
    sendero_verde = Zona('Sendero Verde', 'núcleo')

    sistema.zonas.extend([laguna, mirador])
    laguna.agregar_subzona(sector_norte)
    laguna.agregar_subzona(sector_sur)
    sector_norte.agregar_subzona(aguada_escondida)
    sector_sur.agregar_subzona(aguada_ceiba)
    mirador.agregar_subzona(sendero_verde)

    balam = Jaguar('AN-001', 'Balam')
    tuki = Tapir('AN-002', 'Tuki')
    roja = GuacamayaRoja('AN-003', 'Roja')
    coco = CocodriloDePantano('AN-004', 'Coco')
    aullador = MonoAullador('AN-005', 'Aullador')

    laguna.ubicar(balam)
    sector_norte.ubicar(tuki)
    aguada_escondida.ubicar(roja)  # nivel más profundo
    sector_sur.ubicar(coco)
    mirador.ubicar(aullador)

    print('\n=== ENTREGA 5: MAPA RECURSIVO ===')
    for zona in sistema.zonas:
        zona.mostrar()
    print('\n=== CONTEO RECURSIVO ===')
    print('Animales en toda la reserva:', sistema.contar_animales())
    print('Animales dentro de Laguna del Tigre:', laguna.contar_animales())

    print('\n=== BÚSQUEDA RECURSIVA ===')
    for nombre in ('Aguada Escondida', 'Laguna del Tigre', 'Sector Fantasma'):
        resultado = sistema.buscar_sector(nombre)
        print(f'{nombre}: {resultado.nombre if resultado is not None else None}')

    assert sistema.contar_animales() == 5
    assert laguna.contar_animales() == 4
    assert sistema.buscar_sector('Aguada Escondida') is aguada_escondida
    assert sistema.buscar_sector('Laguna del Tigre') is laguna
    assert sistema.buscar_sector('Sector Fantasma') is None
    print('\nTodas las pruebas de recursividad pasaron correctamente.')


if __name__ == '__main__':
    ejecutar_pruebas_entrega5()
