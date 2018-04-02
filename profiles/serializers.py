from rest_framework import serializers
from profiles.models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name', 'address','gender')

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name', 'address','gender')
        extra_kwargs = {
            'name': {'read_only': True},
            'address': {'read_only': True}
        }
    #in this way the geb=nder field becomes editable

