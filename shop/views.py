# from rest_framework import viewsets
# from rest_framework.decorators import action
from rest_framework import generics
# from rest_framework.response import Response

from . import models
from . import serializers


# TODO: Сделать вручную все роуты
#       groups/:group_id/families/:family_id/equipments/:equipment_id/


class EquipmentGroupsAPIView(generics.ListAPIView):
    queryset = models.EquipmentGroup.objects.all()
    serializer_class = serializers.EquipmentGroupSerializer


class EquipmentGroupDetailAPIView(generics.RetrieveAPIView):
    queryset = models.EquipmentGroup.objects.all()
    serializer_class = serializers.EquipmentGroupSerializer


class EquipmentFamiliesAPIView(generics.ListAPIView):
    queryset = models.EquipmentFamily.objects.all()
    serializer_class = serializers.EquipmentFamilySerializer

    def get_queryset(self):
        group_id = self.kwargs['group_id']

        if group_id:
            return models.EquipmentFamily.objects.filter(group=group_id)

        return models.EquipmentFamily.objects.all()


class EquipmentFamilyDetailAPIView(generics.RetrieveAPIView):
    queryset = models.EquipmentFamily.objects.all()
    serializer_class = serializers.EquipmentFamilySerializer


class EquipmentsAPIView(generics.ListAPIView):
    queryset = models.Equipment.objects.all()
    serializer_class = serializers.EquipmentSerializer

    def get_queryset(self):
        # family_id = self.kwargs.get('family_id', None)

        is_promo = self.request.query_params.get('is_promo', None)
        category = self.request.query_params.get('category', None)
        brand = self.request.query_params.get('brand', None)

        # if family_id:
        #     return models.Equipment.objects.filter(type=family_id)

        if is_promo:
            return models.Equipment.objects.filter(is_promo=is_promo)

        if category:
            return models.Equipment.objects.filter(type=category)

        if brand:
            return models.Equipment.objects.filter(brand=brand)

        return models.Equipment.objects.all()


class EquipmentCategoryAPIView(generics.RetrieveAPIView):
    queryset = models.EquipmentCategory.objects.all()
    serializer_class = serializers.EquipmentCategoryWithEquipmentsSerializer


class EquipmentCategoriesAPIView(generics.ListAPIView):
    queryset = models.EquipmentCategory.objects.all()
    serializer_class = serializers.EquipmentCategoryWithEquipmentsSerializer


class EquipmentDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Equipment.objects.all()
    serializer_class = serializers.EquipmentSerializer


# class EquipmentGroupsViewSet(viewsets.ModelViewSet):
#     queryset = models.EquipmentGroup.objects.all()
#     serializer_class = serializers.EquipmentGroupSerializer
#
#     @action(methods=['get'], detail=True, url_path='families')
#     def by_group(self, request, pk=None):
#         families = models.EquipmentFamily.objects.all()
#         print('families', families)
#         serializer = serializers.EquipmentFamilyByGroupSerializer(families)
#         print('serializer', serializer)
#
#         return Response(serializer.data)
#
#
# class EquipmentFamiliesViewSet(viewsets.ModelViewSet):
#     queryset = models.EquipmentFamily.objects.all()
#     serializer_class = serializers.EquipmentFamilySerializer
#
#
# class EquipmentsViewSet(viewsets.ModelViewSet):
#     queryset = models.Equipment.objects.all()
#     serializer_class = serializers.EquipmentSerializer
