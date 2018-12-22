from rest_framework import serializers
from markers.models import Marker

class MarkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marker
        fields = ('id', 'phone', 'latitude', 'longitude', 'message', 'picture')