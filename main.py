from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI(title="PokeAPI Wrapper - Motum Test API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/pokemon/{pokemon_name}/abilities")
def get_pokemon_abilities(pokemon_name: str):
    name = pokemon_name.strip().lower()
    
    pokeapi_url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    
    response = requests.get(pokeapi_url)
    
    if response.status_code == 200:
        data = response.json()
        abilities = [ability['ability']['name'] for ability in data.get('abilities', [])]
        
        return {
            "pokemon": name,
            "abilities": abilities
        }
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Pokemón no encontrado en la PokeAPI")
    else:
        raise HTTPException(status_code=500, detail="Error interno del servidor al consultar la PokeAPI")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)