# Generated by Django 2.1.2 on 2018-10-22 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.IntegerField(unique=True)),
                ('nomCompleto', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('fono', models.IntegerField()),
                ('fechaNaci', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomComuna', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomEstado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomGenero', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fechaIngreso', models.DateField()),
                ('fechaNacimiento', models.DateField()),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Estado')),
                ('Genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Genero')),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomRaza', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomRegion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regiones',
            },
        ),
        migrations.CreateModel(
            name='TipoVivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='automovil',
            name='marca',
        ),
        migrations.DeleteModel(
            name='Automovil',
        ),
        migrations.DeleteModel(
            name='Marca',
        ),
        migrations.AddField(
            model_name='mascota',
            name='Raza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Raza'),
        ),
        migrations.AddField(
            model_name='comuna',
            name='Region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Vivienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TipoVivienda'),
        ),
    ]
