from django.db import models

from apps.base import mixins


class Category(mixins.NameSlugMixin):

    class Meta:
        ordering = ('name',)
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(mixins.NameSlugMixin, mixins.UpdateCreateMixin):
    category = models.ForeignKey(
        'Category',
        related_name='products',
        verbose_name="Категория",
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='products/%Y/%m/%d/',
        blank=True,
        verbose_name="Изображение товара"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")

    class Meta:
        db_table = 'products'
        ordering = ('name',)
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
