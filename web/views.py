from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from django.template.loader import render_to_string
from django.db.models import Q

from api.serializers import RouteSerializer, SuggestionSerializer, AnketaTestSerializer
from api.models import Route, Suggestion, AnketaTest


class AnketaViewSet(viewsets.GenericViewSet):
    def list(self, request):
        return render(request, 'index.html')

    def create(self, request):
        serializer = AnketaTestSerializer(data=request.POST)
        if serializer.is_valid():
            serializer = serializer.data
            age = int(serializer['age'])
            time = serializer['Time']
            child = serializer['child']
            invalid = serializer['invalid']
            invalid2 = serializer['invalid2']
            personal1 = serializer['personal1']
            personal2 = serializer['personal2']
            personal3 = serializer['personal3']
            personal4 = serializer['personal4']
            phys_ready = serializer['physReady']
            if invalid2 or invalid or age >= 60 or phys_ready == 1 or 0 < age <= 10:
                lte = 1
            elif age >= 40 or phys_ready == 2 or child == 1:
                lte = 2
            else:
                lte = 3
            if time == 1:
                eq = [1]
            elif time == 2:
                eq = [2]
            elif time == 3:
                eq = [3]
            else:
                eq = [1, 2, 3]
            routes_all = Route.objects.all().filter(difficulty__lte=lte, difficulty__in=eq)
            routes = Route.objects.none()
            if personal1:
                routes = routes | routes_all.filter(personal1=True)
            if personal2:
                routes = routes | routes_all.filter(personal2=True)
            if personal3:
                routes = routes | routes_all.filter(personal3=True)
            if personal4:
                routes = routes | routes_all.filter(personal4=True)
            if not personal1 and not personal2 and not personal3 and not personal4:
                routes = routes_all
            routes = RouteSerializer(routes, many=True).data
            return Response({'html': render_to_string('route.html', context={
                'routes': routes
            })})
        return Response({'html': '<h1>fail</h1>'})

    def retrieve(self, request, pk):
        route = Route.objects.get(pk=pk)
        serializer = RouteSerializer(route).data
        return render(request, 'route-detail.html', {
            'route': serializer
        })

    def get_permissions(self):
        return [AllowAny()]


class SuggestionViewSet(viewsets.GenericViewSet,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin):
    queryset = Suggestion.objects.all()
    serializer_class = SuggestionSerializer

    def list(self, request):
        suggestions = Suggestion.objects.all().order_by('-id')
        suggestions = SuggestionSerializer(suggestions, many=True, context={
            'request': request,
        })
        return render(request, 'suggestion-list.html', {
            'suggestions': suggestions.data,
        })

    @action(detail=False)
    def form(self, request):
        return render(request, 'suggestion.html')

    def get_permissions(self):
        return [AllowAny()]
