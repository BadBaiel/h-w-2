# Generated by Django 4.1.7 on 2023-02-21 17:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='Автор'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('FANTASTIC', 'ФАНТАСТИКА'), ('HORROR', 'ХОРОР'), ('ROMANCE', 'РОМАНТИКА'), ('COMEDY', 'КОМЕДИЯ'), ('NOVEL', 'НОВЕЛЛА'), ('DETECTIVE', 'ДЕТЕКТИВ')], max_length=100, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.PositiveIntegerField(null=True, verbose_name='Колл-во'),
        ),
    ]
