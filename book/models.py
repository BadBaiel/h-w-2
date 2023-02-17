from django.db import models

# Create your models here.
class Book(models.Model):

    GENRE = (
        ('FANTASTIC', 'ФАНТАСТИКА'),
        ('HORROR', 'ХОРОР'),
        ('ROMANCE', 'РОМАНТИКА'),
        ('COMEDY', 'КОМЕДИЯ'),
        ('NOVEL', 'НОВЕЛЛА'),
        ('DETECTIVE', 'ДЕТЕКТИВ')
    )

    title = models.CharField('Название книги', max_length=100)
    description = models.TextField('Описание книги')
    image = models.ImageField('Фотографие книги', upload_to='')
    quantity = models.PositiveIntegerField('Колличество книг')
    genre = models.CharField(max_length=100, choices=GENRE)
    video = models.URLField()
    price = models.PositiveIntegerField('Цена книги', null=True)

    # create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title