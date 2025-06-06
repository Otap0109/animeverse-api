from .models import Character
from .serializers import CharacterListSerializer, CharacterSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

class CharViewSet(ReadOnlyModelViewSet):
    queryset = Character.objects.all()
    filterset_fields = ['anime', 'age']
    ordering_fields = ['name']
    ordering = ['name']

    def get_serializer_class(self):
        if self.action == 'list':
            return CharacterListSerializer
        return CharacterSerializer