from django.db.models import (
    Model,
    CharField,
    TextField,
    ForeignKey,
    CASCADE,
    ImageField,
    BooleanField
)


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
    family = ForeignKey(EquipmentFamily, related_name='categories', on_delete=CASCADE, null=True)

    def __str__(self):
        return self.name


class Equipment(Model):
    name = CharField(max_length=200, verbose_name='Название')
    label = CharField(max_length=300, verbose_name='Марка')
    description = TextField(verbose_name='Описание', null=True)
    in_stock = BooleanField(verbose_name="Акционный", default=False)
    type = ForeignKey(EquipmentCategory, related_name='equipments', on_delete=CASCADE, verbose_name='Тип')

    def __str__(self):
        return self.label
