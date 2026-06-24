package com.example.pokemon.model;
import java.util.List;

public class PokemonResponse {

    private String pokemon;
    private List<String> abilities;

    public PokemonResponse(String pokemon,
                           List<String> abilities) {
        this.pokemon = pokemon;
        this.abilities = abilities;
    }

    public String getPokemon() {
        return pokemon;
    }

    public void setPokemon(String pokemon) {
        this.pokemon = pokemon;
    }

    public List<String> getAbilities() {
        return abilities;
    }

    public void setAbilities(List<String> abilities) {
        this.abilities = abilities;
    }
}