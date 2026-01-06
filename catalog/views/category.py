from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from catalog.models import Category
from catalog.serializers import CategorySerializer
from catalog.permissions import IsAdminOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name", "slug")
    ordering_fields = ("name", "created_at")

    permission_classes = [IsAdminOrReadOnly]

    def get_permissions(self):
        if getattr(self, "action", None) == "list":
            return [AllowAny()]
        return super().get_permissions()
