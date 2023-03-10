# Generated by Django 4.1.7 on 2023-02-28 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название книги')),
                ('description', models.TextField(verbose_name='Описание книги')),
                ('image', models.ImageField(upload_to='', verbose_name='Фотографие книги')),
                ('quantity', models.PositiveIntegerField(null=True, verbose_name='Колл-во')),
                ('genre', models.CharField(choices=[('FANTASTIC', 'ФАНТАСТИКА'), ('HORROR', 'ХОРОР'), ('ROMANCE', 'РОМАНТИКА'), ('COMEDY', 'КОМЕДИЯ'), ('NOVEL', 'НОВЕЛЛА'), ('DETECTIVE', 'ДЕТЕКТИВ')], max_length=100, verbose_name='Жанр')),
                ('video', models.URLField()),
                ('price', models.PositiveIntegerField(null=True, verbose_name='Цена книги')),
                ('author', models.TextField(verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(max_length=255)),
                ('choise_show', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='book.book')),
            ],
        ),
    ]
