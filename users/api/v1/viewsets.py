from rest_framework import authentication
from users.models import Model
from .serializers import ModelSerializer
from rest_framework import viewsets


class ModelViewSet(viewsets.ModelViewSet):
    serializer_class = ModelSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Model.objects.all()
