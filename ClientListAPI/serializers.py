from rest_framework import serializers
from clientapp.models import Client
from decimal import Decimal
import datetime


class  ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=15)
    last_name = serializers.CharField(max_length=15)
    phone = serializers.CharField(max_length=16)
    email = serializers.EmailField(max_length=30, default='', allow_blank=True)
    birthday = serializers.DateField(format='%d %b %Y', input_formats=['%d %m %Y', '%m %d %Y'], allow_null=True, default=None)
    comment = serializers.CharField(max_length=150)
    image = serializers.ImageField(use_url=True, allow_null=True)

    def create(self, validated_data):
        return Client(**validated_data) # it just returns the model object without saving it to the db
                                        # for saving to the db use Client.objects.create()

    def update(self, instance, validated_data): # for partial updating or whole updating
        instance.id = validated_data.get('id', instance.id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
    
    def validate_birthday(self, value):
        if value > datetime.date.today():
            raise serializers.ValidationError('date is bigger than now')
        return value
    
    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError('only alphabetic characters')
        new_value = value.title()
        return new_value
    
    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError('only alphabetic characters')
        new_value = value.title()
        return new_value
    


# class ClientSerializer(serializers.ModelSerializer):
#     cell_phone = serializers.IntegerField(source='phone')
#     price_after_calculate = serializers.SerializerMethodField(method_name = 'calculate_price')
#     class Meta:
#         model = Client
#         fields = ['id', 'first_name', 'last_name', 'price_after_calculate', 'cell_phone', 'email', 'birthday', 'comment']

#     def calculate_price(self, product:Client):
#         return product.email * Decimal(1.1)