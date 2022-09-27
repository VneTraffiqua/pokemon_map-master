from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    level = models.IntegerField(max_length=50)
    lat = models.FloatField(max_length=20)
    lon = models.FloatField(max_length=20)
    appeared_at = models.DateTimeField(blank=True, null=True)
    disappeared_at = models.DateTimeField(blank=True, null=True)
    health = models.IntegerField(max_length=50, blank=True, null=True)
    strength = models.IntegerField(max_length=50, blank=True, null=True)
    defence = models.IntegerField(max_length=50, blank=True, null=True)
    stamina = models.IntegerField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.pokemon.title} {self.level}lvl'

