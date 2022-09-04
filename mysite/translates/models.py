from django.db import models
from django.urls import reverse


class Translates(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название произведения')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    title_in_the_original_language = models.CharField(max_length=200, verbose_name='Оригинальное название')
    year_of_release = models.CharField(max_length=4, verbose_name='Год релиза')
    #Добавляем категории
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория', blank=True)


    def get_absolute_url(self):
        return reverse('view_translates', kwargs={'translates_id': self.pk})


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'перевод'
        verbose_name_plural = 'переводы'
        ordering = ['-updated_at'] #порядок сортировки
''' 
    =id
    =photo                                картинка / фото
    =title                                название
        country                              страна
    =title in the original language       название на языке оригинала
    =year of release                      год релиза
    =description                          описание
    =created_at                           дата создания
    =updated_at                           дата изменения
        tag                                  теги
        categories                           категории
    =is_published                         опубликованно или нет
    
    #Добавить обязательно к главам при выводе в html фильтр |linebreaks
    
'''
#Создание категорий
class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Наименование категории')


    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'
        ordering = ['title'] #порядок сортировки