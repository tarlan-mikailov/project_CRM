from rest_framework import serializers
from recordapp.models import Record


class  RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = '__all__'
        depth = 1
