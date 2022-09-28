import folium
import json
from django.utils import timezone
from django.http import HttpResponseNotFound, HttpRequest
from django.shortcuts import render
from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemon_entities = PokemonEntity.objects.filter(
        appeared_at__lt=timezone.now(),
        disappeared_at__gt=timezone.now()
    )
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemon_entities:
        add_pokemon(
            folium_map, pokemon.lat,
            pokemon.lon,
            request.build_absolute_uri(f'{pokemon.pokemon.image}')
        )

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(f'{pokemon.image}'),
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    with open('pokemon_entities/pokemons.json', encoding='utf-8') as database:
        pokemons = json.load(database)['pokemons']

    pokemon = Pokemon.objects.get(id=pokemon_id)
    pok = {
            'pokemon_id': pokemon.id,
            'img_url': f'http://127.0.0.1:8000/{pokemon.image}',
            'title_ru': pokemon.title,
            'description': pokemon.description,
        }

    pokemon_entities = PokemonEntity.objects.filter(pokemon__id=pokemon_id)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemon_entities:
        add_pokemon(
            folium_map, pokemon.lat,
            pokemon.lon,
            f'http://127.0.0.1:8000/{pokemon.pokemon.image}'
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pok
    })
