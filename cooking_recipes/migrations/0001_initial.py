# Generated by Django 3.1.6 on 2021-02-05 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='CookingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('uses', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('prep_time', models.IntegerField()),
                ('cook_time', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooking_recipes.author')),
                ('cook_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooking_recipes.cookingtype')),
                ('cuisine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooking_recipes.cuisine')),
            ],
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField()),
                ('desc', models.TextField(unique=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooking_recipes.recipe')),
            ],
        ),
    ]
