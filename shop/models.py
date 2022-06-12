from django.db.models import (
    Model,
    CharField,
    TextField,
    ForeignKey,
    CASCADE,
    ImageField,
    BooleanField,
    IntegerField,
)


# Ideas output static


class Brand(Model):
    name = CharField(max_length=255, verbose_name="Название бренда")
    image = ImageField(verbose_name="Логотип")

    def __str__(self):
        return self.name


class EquipmentGroup(Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class EquipmentFamily(Model):
    name = CharField(max_length=200, null=True)
    image = ImageField(verbose_name='Баннер', null=True)
    group = ForeignKey(EquipmentGroup, on_delete=CASCADE, null=True)

    def __str__(self):
        if self.name:
            return self.name

        return 'None'


class EquipmentCategory(Model):
    name = CharField(max_length=200)
    family = ForeignKey(
        EquipmentFamily,
        related_name='categories',
        on_delete=CASCADE,
        null=True
    )

    def __str__(self):
        return self.name


IN_STOCK_ENUM = (
    ('Нет в наличии', 0),
    ('Осталось мало', 1),
    ('В наличии', 2),
    ('В наличии', 3),
)


class Rating(Model):
    star_count = IntegerField(verbose_name="Рейтинг", default=0)

    def __str__(self):
        return str(self.star_count)


class Equipment(Model):
    name = CharField(max_length=200, verbose_name='Название')
    label = CharField(max_length=300, verbose_name='Марка')
    description = TextField(verbose_name='Описание', null=True)
    is_promo = BooleanField(verbose_name="Акционный", default=False)
    in_stock = CharField(
        choices=IN_STOCK_ENUM,
        max_length=100,
        verbose_name="Количество",
        default=0
    )
    rating = ForeignKey(
        Rating,
        related_name='rating',
        null=True,
        verbose_name='Рейтинг',
        on_delete=CASCADE
    )
    brand = ForeignKey(
        Brand,
        related_name='brand',
        null=True,
        on_delete=CASCADE,
        verbose_name='Бренд'
    )
    type = ForeignKey(
        EquipmentCategory,
        related_name='equipments',
        on_delete=CASCADE,
        verbose_name='Тип'
    )

    def __str__(self):
        return self.label
