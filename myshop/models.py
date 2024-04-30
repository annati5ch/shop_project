from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products')  # отношение "многие к одному"
    name = models.CharField(max_length=200, db_index=True)  # имя товара
    slug = models.SlugField(max_length=200, db_index=True)  # URL продукта
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)  # изображение
    description = models.TextField(blank=True)  # описание
    price = models.DecimalField(max_digits=10, decimal_places=2)  # цена
    stock = models.PositiveIntegerField()  # хранение остатков
    available = models.BooleanField(default=True)  # значение, показывающее доступен продукт или нет
    created = models.DateTimeField(auto_now_add=True)  # дата создания
    updated = models.DateTimeField(auto_now=True)  # время последнего обновления

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
