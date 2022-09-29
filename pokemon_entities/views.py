import folium
from django.utils import timezone
import urllib.parse
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
    url_parts = urllib.parse.urlparse(request.build_absolute_uri())
    pokemon = Pokemon.objects.get(id=pokemon_id)
    previous_evolution = {}
    next_evolution = {}
    if pokemon.previous_evolution:
        previous_evolution = {
            "title_ru": pokemon.previous_evolution.title,
            "pokemon_id": pokemon.previous_evolution.id,
            "img_url":
                f'{url_parts.scheme}://{url_parts.netloc}/'
                f'{pokemon.previous_evolution.image}'
            }
    next_evolutions = pokemon.evolutions.all()
    for evolved_pokemon in next_evolutions:
        next_evolution = {
            "title_ru": evolved_pokemon.title,
            "pokemon_id": evolved_pokemon.id,
            "img_url":  f'{url_parts.scheme}://{url_parts.netloc}/'
                        f'{evolved_pokemon.image}'
        }

    pokemon_parameters = {
        'pokemon_id': pokemon.id,
        'img_url': f'{url_parts.scheme}://{url_parts.netloc}/{pokemon.image}',
        'title_ru': pokemon.title,
        'description': pokemon.description,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'previous_evolution': previous_evolution,
        'next_evolution': next_evolution
    }

    pokemon_entities = pokemon.pokemons.filter(
        appeared_at__lt=timezone.now(),
        disappeared_at__gt=timezone.now()
    )
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemon_entities:
        add_pokemon(
            folium_map, pokemon.lat,
            pokemon.lon,
            f'{url_parts.scheme}://{url_parts.netloc}/{pokemon.pokemon.image}'
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_parameters
    })
