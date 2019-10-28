from rules.models import Rules
from rest_framework import viewsets, permissions
from .serializers import RulesSerializer

# Rules Viewset
class RulesViewSet(viewsets.ModelViewSet):
    queryset = Rules.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RulesSerializer
