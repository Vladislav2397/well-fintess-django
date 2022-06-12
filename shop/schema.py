import graphene
from graphene_django import DjangoObjectType

from .models import EquipmentGroup, EquipmentFamily, EquipmentCategory


class EquipmentGroupType(DjangoObjectType):
    class Meta:
        model = EquipmentGroup
        fields = ("id", "name")


class EquipmentFamilyType(DjangoObjectType):
    class Meta:
        model = EquipmentFamily
        fields = ("id", "name", "image", "group")


class EquipmentCategoryType(DjangoObjectType):
    class Meta:
        model = EquipmentCategory
        fields = ("id", "name")


class Query(graphene.ObjectType):
    groups = graphene.List(EquipmentGroupType)
    group_by_id = graphene.Field(EquipmentGroupType, id=graphene.Int())

    families = graphene.List(EquipmentFamilyType)
    families_by_group_id = graphene.List(EquipmentFamilyType, id=graphene.Int())

    categories = graphene.List(EquipmentCategoryType)
    
    def resolve_groups(root, info):
        # We can easily optimize query count in the resolve method
        return EquipmentGroup.objects.all()
    
    def resolve_group_by_id(root, info, id):
        # Querying a single group
        return EquipmentGroup.objects.get(pk=id)

    def resolve_families(root, info):
        # We can easily optimize query count in the resolve method
        return EquipmentFamily.objects.all()

    def resolve_families_by_group_id(root, info, id):
        return EquipmentFamily.objects.filter(group_id=id)

    def resolve_categories(root, info):
        return EquipmentCategory.objects.all()


schema = graphene.Schema(query=Query)