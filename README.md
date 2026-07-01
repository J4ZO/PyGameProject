# PyGameProject

## Descripción del proyecto

Este proyecto es un juego de supervivencia espacial desarrollado en Python con PyGame. El jugador controla una nave espacial y debe sobrevivir mientras destruye naves enemigas que aparecen en la escena.

## Funcionalidad principal

- El jugador puede moverse libremente por la pantalla usando el teclado.
- Puede disparar hacia la posición del mouse para destruir enemigos.
- Las naves enemigas aparecen automáticamente y avanzan hacia el jugador.
- Si un enemigo toca al jugador, este pierde vida.
- Si el jugador recibe suficiente daño, su nave es destruida y aparece la pantalla de game over.

## Estructura del proyecto

- `Code/main.py`: contiene el bucle principal del juego y la lógica general.
- `Code/Controllers/player.py`: controla el movimiento, disparo y daño del jugador.
- `Code/Controllers/enemy.py`: define el comportamiento de las naves enemigas.
- `Code/Controllers/bullet.py`: gestiona los proyectiles del jugador.
- `Code/Controllers/spawn.py`: genera los enemigos durante la partida.
- `Code/UI/menu.py`: muestra el menú principal.
- `Code/UI/game_over.py`: muestra la pantalla de fin de juego.
- `Code/settings.py`: almacena configuraciones globales del juego.

## Objetivo del juego

Sobrevivir el mayor tiempo posible, destruir las naves enemigas y evitar que estas toquen la nave del jugador, ya que en ese caso perderá vida y será destruido.