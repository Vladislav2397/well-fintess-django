from django.contrib import admin

from .models import (
    Equipment,
    EquipmentCategory,
    EquipmentFamily,
    EquipmentGroup,
    Promotion,
    Brand,
    Rating,
)

admin.site.register(Equipment)
admin.site.register(EquipmentCategory)
admin.site.register(EquipmentFamily)
admin.site.register(EquipmentGroup)

admin.site.register(Promotion)
admin.site.register(Brand)
admin.site.register(Rating)
