from rest_framework import generics
from .models import Marker
from .serializers import MarkerSerializer


class MarkerListView(generics.ListCreateAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer

class MarkerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
