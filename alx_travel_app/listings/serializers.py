from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'listing', 'start_date', 'end_date', 'user', 'total_price']
        read_only_fields = ['user', 'total_price']

    def create(self, validated_data):
        # Get the authenticated user from the request
        validated_data['user'] = self.context['request'].user

        # Calcuated total_price
        listing = validated_data['listing']
        start_date = validated_data['start_date']
        end_date = validated_data['end_date']
        num_days = (end_date - start_date).days
        validated_data['total_price'] = listing.price_per_night * num_days

        return super().create(validated_data)
