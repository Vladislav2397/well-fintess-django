from rest_framework.serializers import ModelSerializer, IntegerField
from .models import Equipment, EquipmentGroup, EquipmentFamily, EquipmentCategory


class EquipmentSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class EquipmentCategorySerializer(ModelSerializer):
    count = IntegerField(source='equipments.count', read_only=True)

    class Meta:
        model = EquipmentCategory
        fields = ('id', 'name', 'count')


class EquipmentCategoryWithEquipmentsSerializer(ModelSerializer):
    count = IntegerField(source='equipments.count', read_only=True)
    equipments = EquipmentSerializer(many=True)

    class Meta:
        model = EquipmentCategory
        fields = ('id', 'name', 'count', 'equipments')


class EquipmentGroupSerializer(ModelSerializer):
    class Meta:
        model = EquipmentGroup
        fields = '__all__'


class EquipmentFamilySerializer(ModelSerializer):
    categories = EquipmentCategorySerializer(many=True)

    class Meta:
        model = EquipmentFamily
        fields = ('id', 'categories', 'name', 'image')


class EquipmentFamilyByGroupSerializer(ModelSerializer):
    class Meta:
        model = EquipmentFamily
        fields = ('name', 'image')
