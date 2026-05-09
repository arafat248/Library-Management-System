from rest_framework.viewsets import ModelViewSet
from .models import Borrow
from .serializer import BorrowSerializer

class BorrowViewSet(ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer