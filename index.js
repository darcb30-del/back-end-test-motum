const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();
const PORT = 3000;

const POKE_API_URL = "https://pokeapi.co/api/v2/pokemon";

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.json({
    message: "Backend funcionando correctamente"
  });
});

app.get("/pokemon/:name", async (req, res) => {
  const name = req.params.name.trim().toLowerCase();

  if (!name) {
    return res.status(400).json({
      message: "El nombre del Pokémon es obligatorio"
    });
  }

  try {
    const response = await axios.get(`${POKE_API_URL}/${name}`);
    const pokemon = response.data;

    const abilities = pokemon.abilities.map((item) => ({
      name: item.ability.name,
      url: item.ability.url,
      is_hidden: item.is_hidden,
      slot: item.slot
    }));

    res.json({
      pokemon: pokemon.name,
      id: pokemon.id,
      abilities: abilities
    });
  } catch (error) {
    res.status(404).json({
      message: "Pokémon no encontrado",
      pokemon: name
    });
  }
});

app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});