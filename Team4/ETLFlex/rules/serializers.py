from rest_framework import serializers
from rules.models import Rules

# Rules Serializer
class RulesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = '__all__'
