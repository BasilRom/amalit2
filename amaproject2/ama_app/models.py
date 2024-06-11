from django.db import models

from django.urls import reverse


class Text(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название текста')
    picture = models.ImageField(blank=True, upload_to='photos', verbose_name='Фото')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    description = models.TextField('Описание')
    # author = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True, verbose_name='Автор')
    region = models.ForeignKey('Region', on_delete=models.PROTECT, null=True, verbose_name='Регион')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'

    def get_absolute_url(self):
        return reverse('text', kwargs={'text_id': self.pk})



    def __str__(self):
        return self.title



class Category(models.Model):
    cat = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.cat


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def get_absolute_url(self):
        return reverse('categs', kwargs={'cat_id': self.pk})

class Author(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Имя автора')
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


    def get_absolute_url(self):
        return reverse('authors', kwargs={'name_id': self.pk})


class Region(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Регион')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


    def get_absolute_url(self):
        return reverse('regions', kwargs={'name_id': self.pk})