# Generated by Django 4.1.7 on 2023-02-21 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.PositiveIntegerField(null=True, verbose_name='Автор'),
        ),
    ]