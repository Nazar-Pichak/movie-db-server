from rest_framework import serializers
from .models import Person, Movie, CustomUser


class PersonSerializer(serializers.ModelSerializer):
    birthDate = serializers.DateField(source="birth_date", required=True)

    class Meta:
        model = Person
        fields = ["_id", "name", "biography", "birthDate", "country", "role"]


class MovieSerializer(serializers.ModelSerializer):
    isAvailable = serializers.BooleanField(source="is_available", required=True)
    dateAdded = serializers.DateTimeField(source="date_added", read_only=True)
    director = PersonSerializer(read_only=True)
    actors = PersonSerializer(many=True, read_only=True)
    directorID = serializers.PrimaryKeyRelatedField(queryset=Person.objects.filter(role="director"), source="director", write_only=False)
    actorIDs = serializers.PrimaryKeyRelatedField(queryset=Person.objects.filter(role="actor"), many=True, source="actors", write_only=False)

    class Meta:
        model = Movie
        fields = [
            "_id", "name", "year", "directorID", "actorIDs", "genres",
            "isAvailable", "dateAdded", "director", "actors"
        ]
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'is_staff']