from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'last_login', 'date_joined']

#class GroupSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Group
#        fields = ['url', 'name']
