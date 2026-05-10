from rest_framework.viewsets import ModelViewSet
from .models import Book, BookImage
from .serializer import BookSerializer, ImageSerializer
from rest_framework.permissions import IsAdminUser

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class image_view(ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        return BookImage.objects.filter(title_id=self.kwargs['book_pk'])
    def perform_create(self, serializer):
        serializer.save(title_id=self.kwargs['book_pk'])