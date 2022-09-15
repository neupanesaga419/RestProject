from dataclasses import fields
from rest_framework import serializers
from myapp.models import Parents, Person, Student


class PersonSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):

    student_related_to = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Student
        fields = "__all__"


class ParentsSerializer(serializers.ModelSerializer):

    related_to = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Parents
        fields = "__all__"


