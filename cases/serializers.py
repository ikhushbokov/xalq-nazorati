from rest_framework import serializers
from .models import Case, CaseTypes
from users.models import User

class CaseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseTypes
        fields = ['id', 'title']

class CaseSerializer(serializers.ModelSerializer):
    case_type = CaseTypeSerializer()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Case
        fields = [
            'id', 'user', 'case_type', 'description', 'manual_address', 'latitude', 'longitude',
            'case_number', 'created_time', 'updated_time'
        ]

    def create(self, validated_data):
        case_type_data = validated_data.pop('case_type')
        case_type = CaseTypes.objects.create(**case_type_data)
        return Case.objects.create(case_type=case_type, **validated_data)

