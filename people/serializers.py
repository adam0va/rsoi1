from rest_framework import serializers
from people.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'age']

    def create(self, validated_data):
    	new = Person(**validated_data)
    	new.save()
    	return new
    
