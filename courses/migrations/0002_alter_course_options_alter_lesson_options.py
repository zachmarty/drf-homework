# Generated by Django 5.0.4 on 2024-04-17 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['name'], 'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['name'], 'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
    ]
