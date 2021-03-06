# В это файле описываются сериалайзеры - структуры на основе которых информация об объекте переводится в формат json
# По сути тут описываются поля объекта, который мы получим потом с помощью функций API

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Event

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('author', 'title', 'text', 'hazard_lvl', 'event_date', 'id')