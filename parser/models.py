from django.db import models


class BookParser(models.Model):
    GENRE = (
        ('FANTASTIC', 'ФАНТАСТИКА'),
        ('HORROR', 'ХОРОР'),
        ('ROMANCE', 'РОМАНТИКА'),
        ('COMEDY', 'КОМЕДИЯ'),
        ('NOVEL', 'НОВЕЛЛА'),
        ('DETECTIVE', 'ДЕТЕКТИВ')
    )

    title_url = models.CharField(max_length=100)
    title_text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    genre = models.CharField('Жанр', max_length=100, choices=GENRE)
    description = models.TextField('Описание книги')

    def __str__(self):
        return self.title_text
# Create your models here.
