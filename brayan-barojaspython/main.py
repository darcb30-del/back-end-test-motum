from flask import Flask, jsonify #importamos flask y jsonify
from PruebaMotum import PokemonService # importamos la clase pruebamotum para utilizar el metodo pokemonservice

app = Flask(__name__)#Creeamos la variable app para la aplicaciòn flask

service = PokemonService()

@app.route("/pokemon/<name>", methods=["GET"])#se crea el API que vamos a utilizar
def get_pokemon(name):#

    result = service.get_abilities(name)#Llamamos al service para obtener las habilidades

    return jsonify(result)#devolvemos el resultado

if __name__ == "__main__":#se inicializa la app
    app.run(debug=True)