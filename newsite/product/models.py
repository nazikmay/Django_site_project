from django.db import models

class Category(models.Model):
    objects = None
    name = models.CharField('Категория', max_length=20, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    objects = None
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение',upload_to='images/', blank=True, null=True)
    price = models.PositiveIntegerField('Цена',default=0)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    create_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    author = models.CharField('Имя', max_length=50)
    text = models.TextField('Отзыв', max_length=5000)
    created_data = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.author}-{self.product}'





