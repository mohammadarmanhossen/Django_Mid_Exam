from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:id>', views.buy_car, name="buy_car"),
    path('details/<int:id>', views.DetailCarView.as_view(), name="car_details"),
]