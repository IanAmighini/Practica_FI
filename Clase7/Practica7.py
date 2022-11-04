#Practica de Web Ejercicio.md
import os, requests

#a) ¿Cuál es el dominio al que estamos consultando?

#pokeapi.co

#b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué Content-Type? Obtené la información correspondiente al campo "forms".

#El status_code devuelve ok. El Content-Type es application/json. 

#c) Haces un json de la url sin /pikachu y obtenes un parametro que dice count. 1154

#d) ¿Cómo esperás que sea la URL para obtener las habilidades de los Pokemons (abilities)? ¿y cómo será la url para obtener la información sobre la habilidad 2?

#https://pokeapi.co/api/v2/abilities. https://pokeapi.co/api/v2/abilities2 o https://pokeapi.co/api/v2/abilities?ability=2

#f) Guardar los datos correspondientes a Pikachu y Sylveon en un archivo de nombre "ficha_tecnica_pokemon.txt".

r = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
r2 = requests.get('https://pokeapi.co/api/v2/pokemon/sylveon')

with open('ficha_tecnica_pokemon.txt', 'a') as salida:
    salida.write(str(r.json()))
    salida.write(str(r2.json()))

#g) Describí la arquitectura cliente-servidor y los roles de cada parte