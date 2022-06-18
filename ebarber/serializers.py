from asyncore import read
from email.policy import default
from itertools import product
from rest_framework import serializers
from directorio.models import User
from ebarber.models import Barber

class BarberSerializer(serializers.ModelSerializer):

    class Meta:

        model = Barber

        fields = ('__all__')

# class RatingSerializer(serializers.ModelSerializer):

#     user = serializers.PrimaryKeyRelatedField(
#         queryset=User.objects.filter(is_active=True))
#     product = serializers.PrimaryKeyRelatedField(
#         queryset=Product.objects.all())
#     rate = serializers.IntegerField(max_value=5, min_value=1)

#     class Meta:

#         model = Rating

#         fields = '__all__'

#     def create(self, validated_data):
#         user = validated_data['user']
#         rate = validated_data['rate']
#         product = validated_data['product']
#         return Rating.objects.update_or_create(user=user, product=product, defaults={'rate': rate})