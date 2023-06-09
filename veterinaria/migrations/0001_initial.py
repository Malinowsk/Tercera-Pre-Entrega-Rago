# Generated by Django 4.2.1 on 2023-05-06 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('raza', models.CharField(max_length=256)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=7)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=7)),
                ('vacunado', models.BooleanField(default=False)),
                ('dueño', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('num_piso', models.CharField(max_length=32)),
                ('metros_cuadrados', models.DecimalField(decimal_places=2, max_digits=7)),
                ('con_tetoscopio', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=256)),
                ('nombre', models.CharField(max_length=256)),
                ('dni', models.CharField(max_length=32)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('puesto', models.CharField(max_length=128)),
            ],
        ),
    ]
