# Hangman Game

¡Bienvenido al juego de Hangman (Ahorcado) hecho en Python!

## Descripción

El juego de Hangman es un clásico juego de adivinanzas en el que el jugador debe adivinar una palabra secreta letra por letra. Cada intento incorrecto acerca al jugador a ser "ahorcado". El objetivo es adivinar la palabra antes de agotar todos los intentos.

## Características

- Varios niveles con palabras y pistas.
- Mensajes de error manejados para mejorar la experiencia del usuario.

## Estructura del Proyecto

- `main.py`: Archivo principal que contiene la lógica del juego.
- `helpers.py`: Archivo que contiene utilidades para la lógica del juego.
- `helpers.py`: Archivo que contiene la lógica de niveles del juego.
- `words.py`: Archivo que contiene las palabras y pistas para cada nivel.
- `README.md`: Descripción del proyecto y guías de uso.

## Instalación

Sigue estos pasos para instalar y ejecutar el juego en tu máquina local.

### Requisitos

- Python 3.x
- Git (opcional, para clonar el repositorio)

### Clonar el repositorio

Puedes clonar este repositorio usando Git:

```bash
git clone git@github.com:juanpavasgarzon/HangmanGame.git
cd HangmanGame
```

### Crear un entorno virtual (opcional pero recomendado)
```bash
python3 -m venv venv
source venv/bin/activate
```

### Uso
```bash
python3 main.py
```