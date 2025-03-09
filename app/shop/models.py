from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Название категории
    slug = models.SlugField(unique=True)  # Уникальная ссылка для URL

    class Meta:
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)  # Название товара
    description = models.TextField(blank=True, null=True)  # Описание
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")  # Категория товара
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Картинка товара
    stock = models.PositiveIntegerField(default=0)  # Количество товара в наличии
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего изменения

    class Meta:
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
