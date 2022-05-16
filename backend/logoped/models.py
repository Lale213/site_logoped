from django.db import models


# Create your models here.


class Category(models.Model):
    group = models.CharField(max_length=100,
                             verbose_name='Категория',
                             unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.group


class Publication(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Название статьи',
                             unique=True)
    content = models.TextField(verbose_name='Текст статьи')

    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='группа статьи')
    time_create = models.DateTimeField(verbose_name='Дата и время создания статьи',
                                       auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True,
                                       verbose_name="Время изменения")

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Media(models.Model):
    name_file = models.CharField(max_length=100,
                                 verbose_name='имя файла',
                                 unique=True)
    media_file = models.FileField(verbose_name='файл')
    publication = models.ForeignKey(Publication,
                                    on_delete=models.CASCADE,
                                    verbose_name='статья')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return self.name_file
