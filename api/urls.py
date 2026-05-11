from rest_framework.routers import DefaultRouter
from books.views import BookViewSet, ImageView
from category.views import CategoryViewSet
from Transections.views import BorrowViewSet
from rest_framework_nested import routers

router = DefaultRouter()

router.register('books', BookViewSet, basename='book')
router.register('categorys', CategoryViewSet, basename='category')
router.register('Borrow', BorrowViewSet, basename='Borrows')

book_router= routers.NestedDefaultRouter(router, 'books', lookup='bk')
book_router.register('image', ImageView, basename='images')

urlpatterns = router.urls
urlpatterns += book_router.urls