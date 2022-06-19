from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Категория',
                            unique=True)
    slug = models.SlugField(max_length=255,
                            unique=True,
                            db_index=True,
                            verbose_name="URL")

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Название статьи',
                             unique=True)
    content = models.TextField(verbose_name='Текст статьи')
    slug = models.SlugField(max_length=255,
                            unique=True,
                            db_index=True,
                            verbose_name="URL")
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='группа статьи')
    file = models.FileField(verbose_name='файл',
                            upload_to="files/%Y/%m/%d/",
                            null=True,
                            default=None)
    time_create = models.DateTimeField(verbose_name='Дата и время создания статьи',
                                       auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True,
                                       verbose_name="Время изменения")

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-time_create']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Media(models.Model):
    name_file = models.CharField(max_length=255,
                                 verbose_name='имя файла',
                                 unique=True)
    media_file = models.FileField(verbose_name='файл',
                                  upload_to="files/%Y/%m/%d/")
    publication = models.ForeignKey(Publication,
                                    on_delete=models.CASCADE,
                                    verbose_name='статья')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return self.name_file
