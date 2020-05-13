from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id','user_id','latitude','longitude','address' ,'status', 'drone_id', 'order_name')