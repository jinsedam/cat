from rest_framework import viewsets
from .models import Data
from .serializers import DataSerializer

class DataViewset(viewsets.ModelViewSet):

    serializer_class = DataSerializer
    queryset = Data.objects.all()
