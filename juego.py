import random
from personaje import Personaje, Guerrero, Mago, Arquero

class Juego:
    """
    Clase que representa el juego "Gran Fantasía".
    """

    def jugar(self):
        """
        Método principal para iniciar el juego.
        """
        print("¡Bienvenido a Gran Fantasía!")
        nombre_personaje = input("Por favor, indique el nombre de su personaje:\n")

        # Solicitar al usuario que seleccione una clase para su personaje
        print("Seleccione una clase para su personaje:")
        print("1. Guerrero")
        print("2. Mago")
        print("3. Arquero")
        clase = input("Ingrese el número correspondiente a la clase deseada:\n")

        # Crear el personaje del jugador según la clase seleccionada
        if clase == "1":
            jugador = Guerrero(nombre_personaje)
        elif clase == "2":
            jugador = Mago(nombre_personaje)
        elif clase == "3":
            jugador = Arquero(nombre_personaje)
        else:
            print("Opción inválida.")
            return

        print(jugador.obtener_estado())

        # Crear un personaje "Orco" para enfrentar al jugador
        orco = Personaje("Orco")
        print(orco.obtener_estado())

        # Calcular la probabilidad de ganar contra el orco y solicitar acción al jugador
        probabilidad = Personaje.calcular_probabilidad(jugador, orco)
        opcion = Personaje.enfrentamiento_con_orco(jugador, orco, probabilidad)

        # Realizar enfrentamientos hasta que el jugador decida huir
        while opcion == "1":
            resultado = random.uniform(0, 1)
            if resultado <= probabilidad / 100:
                # El jugador gana
                print("¡Le has ganado al orco, felicidades!")
                jugador.asignar_estado(50)
                orco.asignar_estado(-30)
            else:
                # El orco gana
                print("¡Oh no! ¡El orco te ha ganado!")
                jugador.asignar_estado(-30)
                orco.asignar_estado(50)

            # Mostrar estados actualizados del jugador y el orco
            print(jugador.obtener_estado())
            print(orco.obtener_estado())

            # Calcular nuevamente la probabilidad de ganar y preguntar al jugador
            probabilidad = Personaje.calcular_probabilidad(jugador, orco)
            opcion = Personaje.enfrentamiento_con_orco(jugador, orco, probabilidad)

        print("¡Has huido! El orco ha quedado atrás.")

if __name__ == "__main__":
    # Iniciar el juego
    juego = Juego()
    juego.jugar()
