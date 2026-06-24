package com.example.pokemon.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.example.pokemon.model.PokemonResponse;
import com.example.pokemon.service.PokemonService;

@RestController
@RequestMapping("/pokemon")
public class PokemonController {

    @Autowired
    private PokemonService pokemonService;

    @GetMapping("/{nombre}")
    public PokemonResponse obtenerPokemon(
            @PathVariable String nombre) {

        return new PokemonResponse(
                nombre,
                pokemonService.obtenerAbilities(nombre));
    }
}