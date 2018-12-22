from django.urls import path
from markers import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('markers/', views.MarkerListView.as_view()),
    path('markers/<int:pk>/', views.MarkerDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)