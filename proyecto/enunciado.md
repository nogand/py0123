### Proyecto BlackJack

Escribir un juego de BlackJack en línea que permita a una persona jugar contra la casa, con un monto inicial de dinero para apostar.
El juego sigue hasta que la persona decide retirarse o se queda sin dinero.

## Implementación

El juego debe estar escrito como un API REST y un cliente web y de modo texto.

El API debe contemplar al menos las siguientes operaciones:

* **NuevoJuego**: Arranca un nuevo juego, creando un nuevo mazo de naipes y entregándole las fichas al jugador.
* **EstadoJuego**: Recibe el identificador del juego y devuelve su estado actual.
* **NuevaPartida**: Reparte las cartas iniciales al jugador y la casa, a partir del estado actual del juego. No debe funcionar si hay una partida en juego.
* **TerminarPartida**: Determina el estado del juego y recoge la apuesta o paga la ganancia al jugador y deja el juego listo para una nueva partida.
  * Entre estos dos estados deben diseñarse y permitirse las operaciones requeridas para el juego de BlackJack.
