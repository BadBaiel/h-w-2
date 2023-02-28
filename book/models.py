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
    quantity = models.PositiveIntegerField('Колл-во', null=True)
    genre = models.CharField('Жанр', max_length=100, choices=GENRE)
    video = models.URLField()
    price = models.PositiveIntegerField('Цена книги', null=True)
    author = models.TextField('Автор')
    # create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Coment(models.Model):
    choise_show = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment', null=True, blank=True)
    comments = models.TextField(max_length=255, )

# class Ratingstar(models.Model):
#     value = models.SmallAutoField('значение', default=0)
#
#     def __str__(self):
#         return self.value
#
#     class Meta:
#         verbose_name = "Звезда рейтинга"
#         verbose_name_plural = "Звезды рейтинга"
#         ordering = ["-valie"]
# class Rating(Book):
#     ip = models.CharField('Ip address', max_length=15)
#     star = models.ForeignKey(Ratingstar, on_delete=models.CASCADE, verbose_name="звезда")
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="книга")
#
#     def __str__(self):
#         return f'{self.star} - {self.book}'
#
#     class Meta:
#         verbose_name = "Рейтинг"
#         verbose_name_plural = "Рейтинги"
