from rest_framework.routers import DefaultRouter

from customer_club.api.views.category_view import CategoryViewset

router = DefaultRouter()
router.register(r'customer-club/category', CategoryViewset, basename='customer-club-category')

urlpatterns = router.urls
