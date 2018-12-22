from django.urls import path
from markers import views

urlpatterns = [
    path('markers/', views.marker_list),
    path('markers/<int:pk>/', views.marker_detail),
]