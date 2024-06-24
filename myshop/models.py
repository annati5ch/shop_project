from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def get_absolute_url(self):
        return reverse('post-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', default=None, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=200, db_index=True)  # имя товара
    slug = models.SlugField(max_length=200, db_index=True)  # URL продукта
    image = models.FileField(upload_to='MEDIA_ROOT\images', blank=True)
    description = models.TextField(blank=True)  # описание
    size = models.CharField(max_length=25, db_index=True, default=None)
    weight = models.CharField(max_length=25, db_index=True, default=None)
    age = models.CharField(max_length=25, db_index=True, default=None)
    material = models.CharField(max_length=100, db_index=True, default=None)
    features = models.CharField(max_length=150, db_index=True, default="Нет особенностей")
    set = models.CharField(max_length=250, db_index=True, default=None)
    orig_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    discount = models.IntegerField(blank=True, default=0)
    discounted_price = models.DecimalField(blank=True, decimal_places=2)
    stock = models.PositiveIntegerField()  # хранение остатков
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)  # дата создания
    updated = models.DateTimeField(auto_now=True)  # время последнего обновления

    @property
    def discount_in_percentage(self):
        return f"{self.discount} %"

    @property
    def discounted_price(self):
        return (self.orig_price * self.discount)/100

    @property
    def sell_price(self):
        return (self.orig_price - self.discounted_price)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myshop:product_detail', args=[self.id, self.slug])



