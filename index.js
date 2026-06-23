const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app =express();

app.use(cors());
app.use(express.json());

app.get("/pokemon/:name", async (req, res)=>{
    try{
        const name = req.params.name;
        const response = await axios.get (`https://pokeapi.co/api/v2/pokemon/${name}`);

        const abilities = response.data.abilities.map(ability => ability.ability.name);

        res.json({pokemon:name, abilities:abilities});
      
    }catch (error){
        res.status(404).json({message:"Pokemon no encontrado"});

    }

});

app.listen(3000,() =>{
    console.log("Servidor corriendo en puerto 3000");

});