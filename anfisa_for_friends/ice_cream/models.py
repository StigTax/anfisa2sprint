from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Topping(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'

    def __str__(self):
        return self.title


class Wrapper(PublishedModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Название',
        help_text='Уникальное завание упаковки, не более 256 символов'
    )

    class Meta:
        verbose_name = 'Упаковка'
        verbose_name_plural = 'Упаковки'

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    is_on_main = models.BooleanField(
        default=False,
        verbose_name='На главную'
    )
    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения'
    )
    price = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        verbose_name='Цена'
    )
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        verbose_name='Упаковка',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    toppings = models.ManyToManyField(Topping, verbose_name='Топпинг')

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'
        ordering = ('output_order', 'title')

    def __str__(self):
        return self.title
