from rest_framework import serializers

from api.models import Route, Suggestion, AnketaTest


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class SuggestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Suggestion
        fields = '__all__'


class AnketaTestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnketaTest
        fields = '__all__'
