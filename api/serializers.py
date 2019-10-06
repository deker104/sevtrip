from rest_framework import serializers

from api.models import Route, Suggestion, AnketaTest


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = '__all__'


class AnketaTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnketaTest
        fields = '__all__'
