from rest_framework import serializers
from .models import StudentEnquiry

class StudentEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEnquiry
        fields = '__all__'

    def validate_email(self, value):
        """Check if email already exists"""
        if StudentEnquiry.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists!")
        return value

    def validate_mobile(self, value):
        """Check if mobile already exists"""
        if StudentEnquiry.objects.filter(mobile=value).exists():
            raise serializers.ValidationError("Mobile number already exists!")
        return value
