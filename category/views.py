from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializer import CategorySreializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySreializer