from rest_framework.routers import DefaultRouter
from books.views import BookViewSet
from category.views import CategoryViewSet
from Transections.views import BorrowViewSet

router = DefaultRouter()

router.register('books', BookViewSet, basename='book')
router.register('categorys', CategoryViewSet, basename='category')
router.register('Borrow', BorrowViewSet, basename='Borrows')

urlpatterns = router.urls
