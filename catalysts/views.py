from rest_framework import viewsets
from .models import Catalyst
from .serializers import CatalystSerializer

class CatalystViewset(viewsets.ModelViewSet):

    serializer_class = CatalystSerializer
    queryset = Catalyst.objects.all()
