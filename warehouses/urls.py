from django.urls import path
from . import views

urlpatterns = [
    path('warehouses/list', views.warehouses_get_list),
    path('warehouses', views.warehouses_post_create),
    path('warehouses/<int:warehouse_id>', views.warehouses_get_by_id),
    path('warehouses/<int:warehouse_id>', views.warehouses_put),
    path('warehouses/<int:warehouse_id>', views.warehouses_delete),
]