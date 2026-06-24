package com.example.pokemon.service;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class PokemonService {

    private static final String URL =
            "https://pokeapi.co/api/v2/pokemon/";

    public List<String> obtenerAbilities(String pokemon) {

        RestTemplate restTemplate = new RestTemplate();

        Map<String, Object> response =
                restTemplate.getForObject(
                        URL + pokemon,
                        Map.class);

        List<Map<String, Object>> abilities =
                (List<Map<String, Object>>) response.get("abilities");

        List<String> resultado = new ArrayList<>();

        for (Map<String, Object> item : abilities) {

            Map<String, String> ability =
                    (Map<String, String>) item.get("ability");

            resultado.add(ability.get("name"));
        }

        return resultado;
    }
}