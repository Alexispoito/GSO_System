from django.urls import path
from . import views

urlpatterns = [
    # Inventory Views
    path('gso-inventory/', views.gso_inventory, name='gso_inventory'),

    # CRUD (AJAX)
    path('add/', views.add_inventory_item, name='add_inventory_item'),
    path('update/<int:item_id>/', views.update_inventory_item, name='update_inventory_item'),
    path('remove/<int:item_id>/', views.remove_inventory_item, name='remove_inventory_item'),
]
