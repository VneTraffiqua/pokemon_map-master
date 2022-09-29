from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.CharField(max_length=20, blank=True, null=True)
    title_jp = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    description = models.TextField(max_length=400, blank=True, null=True)
    previous_evolution = models.ForeignKey(
        'Pokemon',
        on_delete=models.CASCADE,
        related_name='evolutions',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, related_name='pokemons'
    )
    level = models.IntegerField()
    lat = models.FloatField(max_length=20)
    lon = models.FloatField(max_length=20)
    appeared_at = models.DateTimeField(blank=True, null=True)
    disappeared_at = models.DateTimeField(blank=True, null=True)
    health = models.IntegerField(blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    defence = models.IntegerField(blank=True, null=True)
    stamina = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.pokemon.title} {self.level}lvl'

