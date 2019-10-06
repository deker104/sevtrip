from rest_framework import viewsets

from api.serializers import RouteSerializer
from api.models import Route


class RouteViewSet(viewsets.ModelViewSet):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()
