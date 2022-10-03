# Generated by Django 3.1.14 on 2022-10-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0019_auto_20221003_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, default='1900-1-1 1:1', verbose_name='Появился'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(blank=True, default=0, verbose_name='Защита'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True, default='1900-1-1 1:1', verbose_name='Исчез'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(blank=True, default=0, verbose_name='Здоровье'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(blank=True, default=0, verbose_name='Выносливость'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(blank=True, default=0, verbose_name='Сила'),
            preserve_default=False,
        ),
    ]