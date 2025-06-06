from .models import Franchise
from .serializers import FranchiseListSerializer, FranchiseSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

class FranchiseViewSet(ReadOnlyModelViewSet):
    queryset = Franchise.objects.all()
    filterset_fields = ['genre', 'rating']
    ordering_fields = ['release_date', 'title']
    ordering = ['release_date']

    def get_serializer_class(self):
        if self.action == 'list':
            return FranchiseListSerializer
        return FranchiseSerializer