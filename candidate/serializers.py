import re
from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
        # exclude = ('status',)

    def validate_phone_number(self, value):
        # Regex to Validate phone number
        if not re.match(r'^\d{10}$', value):
            raise serializers.ValidationError("Enter a valid 10 digit phone number.")
        return value

    def validate_email(self, value):
        # Regex to Validate email address
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
            raise serializers.ValidationError("Enter a valid email address.")
        return value
    
    def create(self, validated_data):
        # When creating candidate status should be set to default
        validated_data.setdefault('status', 'Applied')
        return super().create(validated_data)