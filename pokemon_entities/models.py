from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название на русском')
    title_en = models.CharField(max_length=20, blank=True, null=True, verbose_name='Название на ангийском')
    title_jp = models.CharField(max_length=20, blank=True, null=True, verbose_name='Название на японском')
    image = models.ImageField(upload_to='media/', blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(max_length=400, blank=True, null=True, verbose_name='Описание')
    previous_evolution = models.ForeignKey(
        'Pokemon',
        on_delete=models.CASCADE,
        related_name='evolutions',
        blank=True,
        null=True,
        verbose_name='предыдущая эволюция'
    )

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='pokemons',
        verbose_name='Покемон'
    )
    level = models.IntegerField(verbose_name='Уровень')
    lat = models.FloatField(max_length=20, verbose_name='Широта')
    lon = models.FloatField(max_length=20, verbose_name='Долгота')
    appeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Появился')
    disappeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Исчез')
    health = models.IntegerField(blank=True, null=True, verbose_name='Здоровье')
    strength = models.IntegerField(blank=True, null=True, verbose_name='Сила')
    defence = models.IntegerField(blank=True, null=True, verbose_name='Защита')
    stamina = models.IntegerField(blank=True, null=True, verbose_name='Выносливость')

    def __str__(self):
        return f'{self.pokemon.title} {self.level}lvl'

