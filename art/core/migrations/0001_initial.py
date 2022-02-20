# Generated by Django 3.2.8 on 2021-10-20 01:12

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('image', stdimage.models.StdImageField(upload_to='obras', verbose_name='Imagem')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Obra')),
                ('data', models.DateField(verbose_name='Data da Obra')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
