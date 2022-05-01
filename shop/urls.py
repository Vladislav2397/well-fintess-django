from django.urls import path  # , include
# from rest_framework import routers

from . import views

# router = routers.SimpleRouter()
# router.register(r'groups', views.EquipmentGroupsAPIView.as_view())
# router.register('groups/<int:group_id>/families', views.EquipmentFamiliesViewSet)
# router.register(r'equipments', views.EquipmentsViewSet)

urlpatterns = [
    path(
        'groups/',
        views.EquipmentGroupsAPIView.as_view()
    ),
    path(
        'groups/<int:pk>/',
        views.EquipmentGroupDetailAPIView.as_view()
    ),
    path(
        'groups/<int:group_id>/families/',
        views.EquipmentFamiliesAPIView.as_view()
    ),
    path(
        'groups/<int:group_id>/families/<int:pk>/',
        views.EquipmentFamilyDetailAPIView.as_view()
    ),
    # path(
    #     'groups/<int:group_id>/families/<int:family_id>/equipments/',
    #     views.EquipmentsAPIView.as_view()
    # ),
    path(
        'groups/<int:group_id>/families/<int:family_id>/equipments/<int:pk>/',
        views.EquipmentDetailAPIView.as_view()
    ),
    # FIXME: Rename EquipmentModel type to category
    path(
        'equipments/',
        views.EquipmentsAPIView.as_view()
    ),
    path(
        'categories/',
        views.EquipmentCategoriesAPIView.as_view()
    ),
    path(
        'categories/<int:pk>/',
        views.EquipmentCategoryAPIView.as_view()
    )
    # path('', include(router.urls))
]
