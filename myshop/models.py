from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, db_index=True)  # имя товара
    slug = models.SlugField(max_length=200, db_index=True)  # URL продукта
    image = models.FileField(upload_to='\images', blank=True)
    description = models.TextField(blank=True)  # описание
    size = models.CharField(max_length=25, db_index=True, default=None)
    weight = models.CharField(max_length=25, db_index=True, default=None)
    age = models.CharField(max_length=25, db_index=True, default=None)
    material = models.CharField(max_length=50, db_index=True, default=None)
    features = models.CharField(max_length=100, db_index=True, default="Нет особенностей")
    set = models.CharField(max_length=100, db_index=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()  # хранение остатков
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)  # дата создания
    updated = models.DateTimeField(auto_now=True)  # время последнего обновления

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])