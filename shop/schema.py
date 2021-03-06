import graphene
from graphene_django import DjangoObjectType

from django.db.models import Count
from .models import (
    EquipmentGroup,
    EquipmentFamily,
    EquipmentCategory,
    Equipment,
    Brand,
    Rating,
)


class BrandType(DjangoObjectType):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'image')


class EquipmentType(DjangoObjectType):
    brand = graphene.Field(BrandType)
    promotion = graphene.String()
    rating = graphene.Int()

    def resolve_promotion(self, info):
        return self.promotion_id

    def resolve_brand(self, info):
        return Brand.objects.get(pk=self.brand_id)

    def resolve_rating(self, info):
        return Rating.objects.get(pk=self.rating_id).star_count

    class Meta:
        model = Equipment
        fields = (
            'id',
            'name',
            'label',
            'promotion',
            'in_stock',
            'description',
            'brand',
            'rating',
        )


class EquipmentCategoryType(DjangoObjectType):
    equipments = graphene.List(EquipmentType)
    count = graphene.Int()

    class Meta:
        model = EquipmentCategory
        fields = ("id", "name", "family")

    def resolve_count(self, info):
        return self.equipment_count()

    def resolve_equipments(self, info):
        return Equipment.objects.filter(type=self.id)


class EquipmentFamilyType(DjangoObjectType):
    categories = graphene.List(EquipmentCategoryType)

    class Meta:
        model = EquipmentFamily
        fields = ("id", "name", "image", "group")

    def resolve_categories(self, info):
        return EquipmentCategory.objects.filter(
            family_id=self.id
        )


class EquipmentGroupType(DjangoObjectType):
    families = graphene.List(EquipmentFamilyType)

    class Meta:
        model = EquipmentGroup
        fields = ("id", "name")

    def resolve_families(self, info):
        return EquipmentFamily.objects.filter(
            group_id=self.id
        )


class Query(graphene.ObjectType):
    groups = graphene.List(EquipmentGroupType)
    group_by_id = graphene.Field(EquipmentGroupType, id=graphene.Int())

    families = graphene.List(EquipmentFamilyType)
    family_by_id = graphene.Field(EquipmentFamilyType, id=graphene.Int())
    families_by_group_id = graphene.List(
        EquipmentFamilyType, id=graphene.Int()
    )

    categories = graphene.List(EquipmentCategoryType)

    equipments = graphene.List(EquipmentType)
    equipments_by_category_id = graphene.List(
        EquipmentType, id=graphene.Int()
    )
    equipments_by_promotion = graphene.List(
        EquipmentType, id=graphene.Int()
    )

    brands = graphene.List(BrandType)
    
    def resolve_groups(self, info):
        # We can easily optimize query count in the resolve method
        return EquipmentGroup.objects.all()
    
    def resolve_group_by_id(self, info, id):
        # Querying a single group
        return EquipmentGroup.objects.get(pk=id)

    def resolve_families(self, info):
        # We can easily optimize query count in the resolve method
        return EquipmentFamily.objects.all()

    def resolve_family_by_id(self, info, id):
        return EquipmentFamily.objects.get(pk=id)

    def resolve_families_by_group_id(self, info, id):
        return EquipmentFamily.objects.filter(group_id=id)

    def resolve_categories(self, info):
        return EquipmentCategory.objects.all().annotate(
            Count('equipments')
        )

    def resolve_equipments(self, info):
        return Equipment.objects.all()

    def resolve_equipments_by_category_id(self, info, id):
        return Equipment.objects.filter(type=id)

    def resolve_equipments_by_promotion(self, info, id):
        return Equipment.objects.filter(promotion_id=id)

    def resolve_brands(self, info):
        return Brand.objects.all()


schema = graphene.Schema(query=Query)