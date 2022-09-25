from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(max_length=20)
    lon = models.FloatField(max_length=20)
    appeared_at = models.DateTimeField(blank=True, null=True)
    disappeared_at = models.DateTimeField(blank=True, null=True)
    level = models.IntegerField(max_length=50)
    health = models.IntegerField(max_length=50)
    strength = models.IntegerField(max_length=50)
    defence = models.IntegerField(max_length=50)
    stamina = models.IntegerField(max_length=50)

