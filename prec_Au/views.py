from rest_framework import viewsets
from .models import Info
from .serializers import InfoSerializer

class InfoViewset(viewsets.ModelViewSet):

    serializer_class = InfoSerializer
    queryset = Info.objects.all()
