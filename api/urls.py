from rest_framework.routers import DefaultRouter
from books.views import BookViewSet
from category.views import CategoryViewSet
from borrow.views import BorrowViewSet

router = DefaultRouter()

router.register('books', BookViewSet, basename='book')
router.register('categorys', CategoryViewSet, basename='category')
router.register('borrow', BorrowViewSet, basename='borrows')

urlpatterns = router.urls
