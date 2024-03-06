class Personaje:
    """
    Clase que representa a un personaje en el juego.
    """

    def __init__(self, nombre):
        """
        Constructor de la clase Personaje.

        Args:
            nombre (str): Nombre del personaje.
        """
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def obtener_estado(self):
        """
        Método para obtener el estado del personaje.

        Returns:
            str: Estado del personaje (nombre, nivel y experiencia).
        """
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"

    def asignar_estado(self, experiencia):
        """
        Método para asignar experiencia al personaje y calcular el nuevo nivel.

        Args:
            experiencia (int): Experiencia a asignar al personaje.
        """
        # Calcula el nuevo nivel y experiencia del personaje
        self.experiencia += experiencia
        nivel_anterior = self.nivel
        self.nivel = (self.experiencia // 100) + 1

        # Ajusta la experiencia si el personaje baja de nivel
        if self.nivel < nivel_anterior:
            self.experiencia = 0

    def __lt__(self, other):
        """
        Método para comparar si un personaje es menor que otro.

        Args:
            other (Personaje): Otro personaje para comparar.

        Returns:
            bool: True si el nivel del personaje es menor que el del otro, False de lo contrario.
        """
        return self.nivel < other.nivel

    def __gt__(self, other):
        """
        Método para comparar si un personaje es mayor que otro.

        Args:
            other (Personaje): Otro personaje para comparar.

        Returns:
            bool: True si el nivel del personaje es mayor que el del otro, False de lo contrario.
        """
        return self.nivel > other.nivel

    @staticmethod
    def calcular_probabilidad(jugador, orco):
        """
        Método estático para calcular la probabilidad de ganar contra el orco.

        Args:
            jugador (Personaje): Personaje del jugador.
            orco (Personaje): Personaje del orco.

        Returns:
            int: Probabilidad de ganar.
        """
        if jugador < orco:
            return 33
        elif jugador > orco:
            return 66
        else:
            return 50

    @staticmethod
    def enfrentamiento_con_orco(jugador, orco, probabilidad):
        """
        Método estático para simular el enfrentamiento con el orco.

        Args:
            jugador (Personaje): Personaje del jugador.
            orco (Personaje): Personaje del orco.
            probabilidad (int): Probabilidad de ganar.

        Returns:
            str: Opción escogida por el jugador (Atacar o Huir).
        """
        print(f"¡Oh no!, ¡Ha aparecido un Orco!\nCon tu nivel actual, tienes {probabilidad}% de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.\nSi pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        opcion = input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n")
        return opcion

class Guerrero(Personaje):
    """
    Clase que representa a un Guerrero en el juego.
    """

    def __init__(self, nombre):
        """
        Constructor de la clase Guerrero.

        Args:
            nombre (str): Nombre del guerrero.
        """
        super().__init__(nombre)

    def atacar(self):
        """
        Método para que el guerrero realice el ataque "Dash".
        """
        print(f"El Guerrero {self.nombre} realiza un Dash.")


class Mago(Personaje):
    """
    Clase que representa a un Mago en el juego.
    """

    def __init__(self, nombre):
        """
        Constructor de la clase Mago.

        Args:
            nombre (str): Nombre del mago.
        """
        super().__init__(nombre)

    def atacar(self):
        """
        Método para que el mago realice el ataque "Bola de Fuego".
        """
        print(f"El Mago {self.nombre} lanza una Bola de Fuego.")


class Arquero(Personaje):
    """
    Clase que representa a un Arquero en el juego.
    """

    def __init__(self, nombre):
        """
        Constructor de la clase Arquero.

        Args:
            nombre (str): Nombre del arquero.
        """
        super().__init__(nombre)

    def atacar(self):
        """
        Método para que el arquero realice el ataque "Disparo Certero".
        """
        print(f"El Arquero {self.nombre} realiza un Disparo Certero.")
