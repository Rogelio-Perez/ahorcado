import random
import string
from pyfiglet import figlet_format

from palabras import palabras
from diagrama import vidas_diccionario_visual


def obtener_palabra_valida(palabras):
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()


def ahorcado():
    bienvenida = figlet_format("Bienvenido a Ahorcado", font="larry3d")
    print(bienvenida)

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(
            f"Te quedan {vidas} vidas ❤️ y has usado estas letras: {' '.join(letras_adivinadas)}")

        palabras_lista = [
            letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(palabras_lista)}")

        letra_usuario = input('Escribe una letra 👉: ').upper()

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f'\nTu letra, {letra_usuario}, no está en la palabra 🤔')
        elif letra_usuario in letras_adivinadas:
            print('\nYa escribiste esta letra 😯, Escoge una nueva')
        else:
          print('\nEsa letra no es válida 😕, Escoge una nueva')
    if vidas == 0:
      print(vidas_diccionario_visual[vidas])
      print('\nPerdiste 😭')
      print('\nLa palabra era:', palabra)
      print('Sigue jugando 😁')
      end = figlet_format("End Game", font="smslant")
      print(end)
    else:
      print('\nFelicidades!!🎉')
      print('\nGanaste 😎, la palabra era: ', palabra)
      end = figlet_format("End Game", font="smslant")
      print(end)

ahorcado()