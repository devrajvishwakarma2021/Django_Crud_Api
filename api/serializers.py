from .models import Product
from rest_framework import serializers


class Productserializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'