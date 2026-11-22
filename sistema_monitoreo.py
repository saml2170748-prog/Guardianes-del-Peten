         zona = self.buscar(self.zonas, "nombre", nombre_zona)
         if not animal or not zona:
              return self.rechazar("animal o zona inexistente")
         if not self.hora_valida(hora):
              return self.rechazar("art. 10: fecha u hora inválida")
         self.lecturas.append(Lectura(animal, zona, hora, "avistamiento", guardia))
         print(f"Avistamiento: {animal.codigo} por {guardia.codigo}")
         return True
     def listar_alertas_pendientes(self):
         pendientes = []
         for alerta in self.alertas:
              if alerta.estado == "pendiente":
                  pendientes.append(alerta)
                  print(f"Pendiente: {alerta.codigo}, {alerta.tipo}")
         if not pendientes:
              print("No hay alertas pendientes")
         return pendientes
     def atender_alerta(self, codigo_alerta, codigo_guardia, hora):
         self.listar_alertas_pendientes()
         alerta = self.buscar(self.alertas, "codigo", codigo_alerta)
         if not alerta:
              return self.rechazar("alerta inexistente")
         if alerta.estado == "atendida":
              return self.rechazar(f"art. 8: ya atendida por {alerta.responsable.codigo}")
         if not self.codigo_guardia_valido(codigo_guardia):
              return self.rechazar("art. 7: código de guardarrecursos inválido")
         guardia = self.buscar(self.guardarrecursos, "codigo", codigo_guardia)
         if not guardia:
              return self.rechazar("guardarrecursos no registrado")
         if not self.hora_valida(hora):
              return self.rechazar("art. 10: fecha u hora inválida")
         alerta.estado = "atendida"
         alerta.responsable = guardia
         alerta.hora_atencion = hora
         print(f"Alerta {codigo_alerta} atendida por {codigo_guardia}, {hora}")
         return True
     def atender_siguiente_alerta(self, codigo_guardarrecursos):
         # Verificar el responsable antes de retirar la alerta de la cola.
         if not self.codigo_guardia_valido(codigo_guardarrecursos):
              return self.rechazar("art. 7: código de guardarrecursos inválido")
         guardia = self.buscar(self.guardarrecursos, "codigo", codigo_guardarrecursos)
         if guardia is None:
              return self.rechazar("guardarrecursos no registrado")

         # La atención manual de entregas anteriores puede haber atendido
         # alertas que aún estaban en la cola: se omiten sin volver a atender.
         while not self.cola_alertas.esta_vacia():
              alerta = self.cola_alertas.siguiente()
              if alerta.estado == "atendida":
                   self.cola_alertas.atender()
                   continue

              hora = datetime.now().strftime("%Y-%m-%d %H:%M")
              if self.atender_alerta(alerta.codigo, codigo_guardarrecursos, hora):
                   self.cola_alertas.atender()
                   self.bitacora.registrar(
                        f"Alerta {alerta.codigo} ({alerta.tipo}) atendida por "
                        f"{codigo_guardarrecursos} a las {hora}"
                   )
                   return alerta
              return None

         print("No hay alertas por atender")
         return None

     def cambiar_bateria(self, codigo_collar, codigo_guardia, nuevo, hora):
         if not self.codigo_guardia_valido(codigo_guardia):
              return self.rechazar("art. 7: código de guardarrecursos inválido")











         guardia = self.buscar(self.guardarrecursos, "codigo", codigo_guardia)
         collar = self.buscar(self.collares, "codigo", codigo_collar)
         if not guardia or not collar:
              return self.rechazar("collar o guardarrecursos inexistente")


         if not self.bateria_valida(nuevo):
              return self.rechazar("arts. 3 y 9: nuevo nivel fuera de 0 a 100")
         if not self.hora_valida(hora):
              return self.rechazar("art. 10: fecha u hora inválida")
         self.cambios_bateria.append(CambioBateria(collar, collar.bateria, nuevo, guardia, hora))
         collar.bateria = nuevo
         print(f"Batería {codigo_collar}: {nuevo}% por {codigo_guardia}, {hora}")
         return True
     def consultar_movimientos(self, codigo_animal):
         animal = self.buscar(self.animales, "codigo", codigo_animal)
         if not animal:
              self.rechazar("animal inexistente; sin resultados")
              return []
         movimientos = []
         for lectura in self.lecturas:
              if lectura.animal is animal:
                  movimientos.append(lectura)
         print(f"Movimientos de {codigo_animal}: {len(movimientos)}")
         for lectura in movimientos:
              print(f"    {lectura.hora} | {lectura.zona.nombre} | {lectura.origen}")
         return movimientos


     def contar_animales(self):
          total = 0
          for zona in self.zonas:
               total += zona.contar_animales()
          return total

     def buscar_sector(self, nombre):
          for zona in self.zonas:
               encontrada = zona.buscar_sector(nombre)
               if encontrada is not None:
                    return encontrada
          return None
