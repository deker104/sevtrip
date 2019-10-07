from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from django.template.loader import render_to_string

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
            personal = serializer['personal']
            phys_ready = serializer['physReady']
            if invalid2 or invalid or age >= 60 or phys_ready == 1 or time == 1:
                difficulty = 1
            elif age >= 40 or phys_ready == 2 or child == 1 or time == 2:
                difficulty = 2
            else:
                difficulty = 3
            routes = Route.objects.all().filter(difficulty__lte=difficulty).order_by('-difficulty', '-id')
            routes = RouteSerializer(routes, many=True).data
            return Response({'html': render_to_string('route.html', context={
                'routes': routes,
                'difficulty': difficulty
            })})
        return Response({'html': '<h1>fail</h1>'})

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
