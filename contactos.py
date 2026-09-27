def mostrar_menu():
    print("\n---- Agenda de Contactos ----")
    print("Menú:")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

def gestionar_contactos():
    contactos = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del contacto: ")
            telefono = input("Teléfono del contacto: ")
            contactos.append({"nombre": nombre, "telefono": telefono})
            print("¡Contacto registrado!")
        
        elif opcion == "2":
            if contactos:
                print("\nContactos:")
                for contacto in contactos:
                    print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")
            else:
                print("\nNingún contacto registrado.")
        
        elif opcion == "3":
            nombre_buscar = input("Escribe el nombre del contacto a buscar: ")
            encontrado = False
            for contacto in contactos:
                if contacto["nombre"].lower() == nombre_buscar.lower():
                    print(f"Contacto encontrado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")
                    encontrado = True
                    break
            if not encontrado:
                print("Contacto no encontrado.")
        
        elif opcion == "4":
            nombre_eliminar = input("Escribe el nombre del contacto a eliminar: ")
            encontrado = False
            for i, contacto in enumerate(contactos):
                if contacto["nombre"].lower() == nombre_eliminar.lower():
                    del contactos[i]
                    print("¡Contacto eliminado con éxito!")
                    encontrado = True
                    break
            if not encontrado:
                print("Contacto no encontrado.")
        
        elif opcion == "5":
            print("Saliendo de la agenda de contactos.")
            break
        
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    gestionar_contactos()