from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('title', 'address', 'county', 'town', 'price', 'sale_type', 'home_type', 'slug',
                  'bedrooms', 'bathrooms', 'square_foot')


class ListingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        lookup_field = 'slug'
