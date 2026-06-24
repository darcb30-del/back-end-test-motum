import requests #Agregue la libreria request para realizar la peticiòn HTTP

class PokemonService: #Cree la clase PokemonService para realizar la lògica del API

    def get_abilities(self, name): #Metodo que recibe el nombre del pokemon seleccionado
        api = f"https://pokeapi.co/api/v2/pokemon/{name}"#declaramos la variable api para que
        #el url reciba el parametro name
        response = requests.get(api)#Realizamos la peticion al API para obtener sus datos

        data = response.json()#convertimos el JSON a una varible de python

        abilities = []#creeamos una lista para guardar los datos
        for item in data["abilities"]:#Utilizo el ciclo for para identificar todas las habilidades
            abilities.append(item["ability"]["name"])#se añade con .append las habilidades y nombre

        return {#retornamos la informacion solicitada
            "pokemon": name,
            "abilities": abilities
        }