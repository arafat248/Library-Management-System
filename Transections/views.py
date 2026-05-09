from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.utils import timezone
from rest_framework import viewsets
from .models import Borrow
from .serializer import BorrowSerializer

class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        borrow = self.get_object()
        if borrow.is_returned:
            return Response({"message": "Already returned"})
        borrow.return_date = timezone.now()
        borrow.is_returned = True
        borrow.save()
        return Response({
            "message": "Book returned successfully",
            "fine": borrow.fine_amount
        })