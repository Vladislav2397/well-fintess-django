from django.contrib import admin

from .models import Equipment, EquipmentCategory, EquipmentFamily, EquipmentGroup

admin.site.register(Equipment)
admin.site.register(EquipmentCategory)
admin.site.register(EquipmentFamily)
admin.site.register(EquipmentGroup)
