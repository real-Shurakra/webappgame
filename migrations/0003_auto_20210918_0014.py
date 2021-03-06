# Generated by Django 3.2.7 on 2021-09-17 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webappgame', '0002_rename_accounts_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='moon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Delta Temperature', models.IntegerField()),
                ('Moon size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='moontemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Max temperature', models.IntegerField()),
                ('Min temperature', models.IntegerField()),
                ('Max size', models.IntegerField()),
                ('Min size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Delta Temperature', models.IntegerField()),
                ('Planet size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='planettemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Max temperature', models.IntegerField()),
                ('Min temperature', models.IntegerField()),
                ('Max size', models.IntegerField()),
                ('Min size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='solarsystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Orbits', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='Premium member',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='planetorbit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Planet orbit size', models.IntegerField()),
                ('orbitof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webappgame.planet')),
            ],
        ),
        migrations.CreateModel(
            name='moonorbit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Moon orbit size', models.IntegerField()),
                ('orbitof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webappgame.moon')),
            ],
        ),
    ]
