from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from markers.models import Marker
from markers.serializers import MarkerSerializer

@csrf_exempt
def marker_list(request):
    if request.method == 'GET':
        markers = Marker.objects.all()
        serializer = MarkerSerializer(markers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MarkerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def marker_detail(request, pk):
    try:
        marker = Marker.objects.get(pk=pk)
    except Marker.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MarkerSerializer(marker)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MarkerSerializer(marker, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        marker.delete()
        return HttpResponse(status=204)

