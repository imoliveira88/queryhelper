# Generated by Django 4.2.1 on 2023-09-15 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, unique=True, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Sistema',
                'verbose_name_plural': 'Sistemas',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, unique=True, verbose_name='Nome')),
                ('query', models.CharField(max_length=2000, unique=True, verbose_name='Query')),
                ('sistema', models.ForeignKey(db_column='sistema_id', on_delete=django.db.models.deletion.PROTECT, to='aplicacao.sistema', verbose_name='Sistema')),
            ],
            options={
                'verbose_name': 'Query',
                'verbose_name_plural': 'Queryes',
                'ordering': ['nome'],
            },
        ),
    ]
