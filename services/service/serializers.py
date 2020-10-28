from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

    def create(self, validated_data):
        obj, created = Person.objects.get_or_create(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            age=validated_data.get('age'),
            defaults={
                # "first_name": validated_data.get('first_name'),
                # "last_name": validated_data.get('last_name'),
                # "age": validated_data.get('age')
            }  # this field for update
        )
        return obj