from rest_framework import serializers
from Order.models import BoxData
from Order.models import Order

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model=BoxData
        fields = '__all__'