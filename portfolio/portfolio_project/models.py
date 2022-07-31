from django.db import models
from django.db.models import Count
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.urls import reverse


class Rubricks(MPTTModel):
    name = models.CharField(max_length=150, verbose_name='Імя')
    slug = models.CharField(max_length=150, unique=True, verbose_name='слаг')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Наслідування')


    def get_absolute_url(self):
        return reverse('categories', kwargs={'slug': self.slug})


    def __str__(self):
        return self.name


    class MPTTmeta:
        order_insertion_by = ['name']


    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'


class Tags(models.Model):
    name = models.CharField(max_length=150)
    slug = models.CharField(unique=True, max_length=150)


    def get_count(self):
        return len(Products.objects.filter(tag=self.pk))


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('tags', kwargs={'slug': self.slug})


    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']


class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name='Імя товару')
    describe = models.TextField(blank=True)
    slug = models.CharField(max_length=150, unique=True, verbose_name='слаг')
    tag = models.ManyToManyField(to=Tags, verbose_name='Фірми')
    rubrick = models.ForeignKey(Rubricks, on_delete=models.CASCADE, blank=True, null=True, related_name='rubricks')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='фотографія')
    price = models.IntegerField(verbose_name='Ціна в гривнях')
    avaibility = models.BooleanField(default=True)
    all_rating = models.IntegerField(verbose_name='Увесь рейтинг', default=0)
    number_of_rating = models.IntegerField(verbose_name='кількість людей які поклали оцінку', default=0)
    if_vip = models.BooleanField(verbose_name='ВІП', default=False)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Products, verbose_name='Імя продукту', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=150)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post}- {self.name}'

    class Meta:
        verbose_name = 'Коментрії'
        verbose_name_plural = 'Коментраіїї'
        ordering = ['-created_at']